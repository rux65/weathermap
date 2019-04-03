import requests
import json

endpoint = "http://api.openweathermap.org/data/2.5/weather"


payload = {"q": "London,UK", "units":"metric", "appid":"2bb229a44403af08980fc4be234f94a9"}

response = requests.get(endpoint, params=payload)

print (response.url)
print (response.status_code)
print (response.headers["content-type"])
print(response.text)

##200 means ok
#404 or 400 - means bad
##304 - you hit thi api before and you are not having anything new


print (json.loads(response.text)["coord"]["lat"])

for weather in json.loads(response.text)["weather"]:
	print(weather["main"])
	
	