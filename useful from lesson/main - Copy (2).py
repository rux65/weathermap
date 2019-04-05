import requests
import json
from flask import Flask , render_template, request


app=Flask("myApp")
	
@app.route("/postcode", methods=["POST"])
def location():
	form_data=request.form
	var=form_data["text"]
	
	return render_template("weatherApi.html"),var

def get_data():
	form_data=request.form
	var=form_data["text"]
	
 



endpoint = "http://api.openweathermap.org/data/2.5/weather"


payload = {"q":"London, uk", "units":"metric", "appid":"2bb229a44403af08980fc4be234f94a9"}

response = requests.get(endpoint, params=payload)

#print (response.url)#
#print (response.status_code)
#print (response.headers["content-type"])
print(response.text)


@app.route("/location", methods=["post"])
def weather_reply():
	api = json.loads(response.text)
	coord = [api["coord"]]
	weather= api["weather"]
	return render_template("location.html", api=api,coord=coord, weather=weather)

app.run(debug=True) # always run with debug true 



	