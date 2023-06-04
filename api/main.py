import piazza_api
import json
import creds
import time
import openai
import os

p = piazza_api.Piazza()

# Log in

p.user_login(email=creds.email, password=creds.password)

# Get all the classes the user is enrolled in

classes = p.get_user_classes()
math33 = p.network("lfyncuotk4s1ze")

print(math33)

# math33.pos

# posts = math33.iter_all_posts(limit=10)

feed = math33.get_feed(limit=30, offset=30)

post_questions = {
    "data": []
}

for post in feed["feed"]:
    math33.get_post(post["id"])
    post_questions["data"].append(math33.get_post(post["id"])["history"][0]["content"])
    time.sleep(1)

print(json.dumps(post_questions, indent=4, sort_keys=True))

#write the json to a file

with open('testJsons/full/full2.json', 'w') as outfile:
    json.dump(post_questions, outfile)



# for post in posts:
#     post_questions["data"].append(post["history"][0]["content"])
#     # print(post)
#     # #print pretty json

# print(json.dumps(post_questions, indent=4, sort_keys=True))