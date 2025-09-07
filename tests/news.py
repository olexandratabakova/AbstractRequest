from secrets import API_KEY_newsdata
from newsdataapi import NewsDataApiClient
import json

api = NewsDataApiClient (apikey=API_KEY_newsdata)

response = api.latest_api(q="pizza", max_result=5)

json_str = json.dumps(response, indent=4)
with open("text1.json", "w") as f:
    f.write(json_str)

print("Текст записано.")

