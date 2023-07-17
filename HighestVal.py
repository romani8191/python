import json

with open("products.json") as json_file:
    data=json.load(json_file)

    print(data[0]['title'])

