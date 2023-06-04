import piazza_api
import creds
import json

p = piazza_api.Piazza()
p.user_login(email=creds.email, password=creds.password)
classes = p.get_user_classes()
math33 = p.network("lfyncuotk4s1ze")

# feed = json.dumps(math33.get_feed(limit=5, offset=1), indent=4, sort_keys=True)
# post = json.dumps(math33.get_post("ligr0x5l86u2pd"), indent=4, sort_keys=True)

# post a reply anonymously
update = math33.create_followup({"id": "lif8p1zl41z8l"}, "Is this the same for Lec 2")
# print(update)