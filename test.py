import json

with open("resources/hi.json", "r") as fin:
    data = json.load(fin)

data = data[0]["tasks"][0]

print(data)