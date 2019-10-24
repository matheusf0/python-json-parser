import json


with open("data.json") as json_data:
    read_content = json.loads(json_data.read())
for users in read_content:
    print(users['guid'])

