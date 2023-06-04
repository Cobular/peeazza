# set up SQLAlchemy not from flask

from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, insert
import sqlalchemy

# connect to existing database
engine = sqlalchemy.create_engine('postgresql://localhost', echo=True)
# create a table with the following columns - id (primary key) and data (json)

metadata = MetaData()

posts = Table(
    'posts', metadata,
    Column('post_id', String, primary_key=True),
    Column('snippet_text', String),
    Column('logs', String),
    Column('full_text', String, nullable=True),
    Column('bot_confidence', sqlalchemy.Float, nullable=True),
)

bot_responses = Table(
    'bot_responses', metadata,
    Column('bot_response_id', String, primary_key=True),
    Column('post_id', String),
    Column('bot_response', String),
    Column('generation_time', sqlalchemy.DateTime),
)

metadata.create_all(engine)

#drop all tables
# metadata.drop_all(engine)