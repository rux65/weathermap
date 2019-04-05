import requests
import json
from flask import Flask , render_template, request


app=Flask("myApp")
	
@app.route("/location", methods=["POST"])
def request():
	form_data=request.form
	var=form_data["City,Country"]
	#return "all ok"
	return var, render_template("location.html", name=name)
	
app.run(debug=True) # always run with debug true 

var=request()
print(var)

endpoint = "http://api.openweathermap.org/data/2.5/weather"


payload = {"q": var, "units":"metric", "appid":"2bb229a44403af08980fc4be234f94a9"}

response = requests.get(endpoint, params=payload)

#print (response.url)#
#print (response.status_code)
#print (response.headers["content-type"])
print(response.text)

##200 means ok
#404 or 400 - means bad
##304 - you hit thi api before and you are not having anything new


#print (json.loads(response.text)["coord"]["lat"])

#for weather in json.loads(response.text)["weather"]:
#	print(weather["main"])
	




@app.route("/postcode")
def weather_reply():
	api = json.loads(response.text)
	coord = [api["coord"]]
	weather= api["weather"]
	
	return render_template("weatherApi.html", api=api,coord=coord, weather=weather)






	