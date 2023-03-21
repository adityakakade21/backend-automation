import json
import requests


with open("E:\\Backend Automation\\sample.json") as f:
    data = json.load(f)
    print(data["items"]["item"][1]["topping"][4]["type"])
    for element in data["items"]["item"]:
        if element['id'] == '0002':
            for topping in element['topping']:
                if topping['id'] == '5005':
                    print(topping['type'])



