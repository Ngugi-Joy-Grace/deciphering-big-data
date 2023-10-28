import json

with open('../../data/unit 1/data-text.json', 'r') as json_file:
    data = json.load(json_file)

for item in data:
    print(item)
