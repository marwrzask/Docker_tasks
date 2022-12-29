import json

with open("/app/config/config.json") as json_data_file:
    data = json.load(json_data_file)

if data["isWeatherGoodToday"]:
    print("The weather is good today")
else:
    print("The weather is bad today")