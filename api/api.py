from flask_cors import CORS
from flask import Flask, request, jsonify
import string
import piazza_api
import random
import creds
from bot import getConfidence, getFullText
import json
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, insert, update
import sqlalchemy
import datetime
import os

# setup flask

app = Flask(__name__)
CORS(app)

# connect to existing database
engine = sqlalchemy.create_engine(os.environ.get("POSTGRES_URL", "postgresql://localhost"), echo=True)
conn = engine.connect()
# create a table with the following columns - id (primary key) and data (json)

metadata = MetaData()

posts_table = Table(
    'posts', metadata,
    Column('post_id', String, primary_key=True),
    Column('snippet_text', String),
    Column('logs', String),
    Column('full_text', String, nullable=True),
    Column('bot_confidence', sqlalchemy.Float, nullable=True),
)

bot_responses_table = Table(
    'bot_responses', metadata,
    Column('bot_response_id', String, primary_key=True),
    Column('post_id', String),
    Column('generation_time', sqlalchemy.DateTime),
    Column('bot_response', String),

)

p = piazza_api.Piazza()
p.user_login(email=creds.email, password=creds.password)

classes = p.get_user_classes()
math33 = p.network("lfyncuotk4s1ze")


def reuturnArrayOfNewIds(posts):
    new_ids = []
    for post in posts:
        id = post["id"]
        # check if id is in database
        if conn.execute(posts_table.select().where(posts_table.c.post_id == id)).fetchone() is None:
            new_ids.append(id)
    return new_ids


def getSnippets(limit, offset):
    feed = math33.get_feed(limit=limit, offset=offset)
    posts = feed["feed"]
    new_ids = reuturnArrayOfNewIds(posts)

    for post in posts:
        text = post["content_snipet"]
        post_id = post["id"]
        logs = post["log"]
        if post_id in new_ids:
            snippet_text_stmt = insert(posts_table).values(
                post_id=post_id, snippet_text=text, logs=json.dumps(logs))
            conn.execute(snippet_text_stmt)
            # convert array to string
            conn.commit()
            getBotConfidence(text, post_id)


def getFullQuestionText(post_id):
    math33.get_post(post_id)
    return math33.get_post(post_id)["history"][0]["content"]


def generateRandomAlphaNumericString(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def getBotConfidence(text, post_id):
    bot_confidence = getConfidence(text)
    # update the bot confidence in the database
    # update the full text in the database with row id post_id
    bot_confidence_stmt = update(posts_table).where(posts_table.c.post_id == post_id).values(
        bot_confidence=bot_confidence)
    conn.execute(bot_confidence_stmt)
    conn.commit()
    if (bot_confidence > 0.5):

        full_text = getFullQuestionText(post_id)
        full_text_stmt = update(posts_table).where(
            posts_table.c.post_id == post_id).values(full_text=full_text)
        conn.execute(full_text_stmt)
        conn.commit()
        getFullBotResponse(post_id, full_text)
    # make a random number between 0 and 1
    return random.random()


def getFullBotResponse(post_id, full_text):
    bot_responses = getFullText(full_text)
    for bot_response in bot_responses:
        bot_response_stmt = insert(bot_responses_table).values(
            bot_response_id=generateRandomAlphaNumericString(20), post_id=post_id, bot_response=bot_response, generation_time=datetime.datetime.now())
        conn.execute(bot_response_stmt)
        conn.commit()

# make an endpoint that returns the snippets from the database


@app.route('/snippets', methods=['GET'])
def snippets():
    # filter query by bot_confidence
    get_snippets_stmt = posts_table.select().order_by(
        posts_table.c.bot_confidence.desc())
    result = conn.execute(get_snippets_stmt)
    snippets = []
    for row in result:
        snippets.append({"post_id": row[0], "snippet_text": row[1], "logs": row[2],
                        "full_text": row[3], "bot_confidence": row[4]})
    return jsonify(snippets)

# create a GET endpoint that returns the bot responses for a given post_id


@app.route('/bot_responses/<post_id>', methods=['GET'])
def bot_responses(post_id):
    get_bot_responses_stmt = bot_responses_table.select().where(
        bot_responses_table.c.post_id == post_id)
    result = conn.execute(get_bot_responses_stmt)
    bot_responses = []
    for row in result:
        bot_responses.append(
            {"bot_response_id": row[0], "post_id": row[1], "bot_response": row[3], "generation_time": row[2]})
    return jsonify(bot_responses)

@app.route('/bot_responses/post/<post_id>/<bot_response_id>', methods=['GET'])
def post_response(bot_response_id, post_id):
    get_postable_stmt = bot_responses_table.select().where(
        bot_responses_table.c.bot_response_id == bot_response_id)
    result = conn.execute(get_postable_stmt)
    bot_responses = []
    for row in result:
        bot_responses.append(
            {"bot_response_id": row[0], "post_id": row[1], "bot_response": row[3], "generation_time": row[2]})
    content = bot_responses[0]["bot_response"]
    print("DATA", post_id, content)
    # update = math33.create_followup({"id": post_id}, content=content)
    return {}

# serve the app
if __name__ == '__main__':
    app.run(debug=True, port=8000)
