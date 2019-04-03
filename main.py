import requests
import json
from flask import Flask , render_template, request

endpoint = "http://api.openweathermap.org/data/2.5/weather"


payload = {"q": "London,UK", "units":"metric", "appid":"2bb229a44403af08980fc4be234f94a9"}

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
	




app=Flask("myApp")
	
@app.route("/postcode")
def hello_someone():
	weather = json.loads(response.text)
	coords = weather["coord"]
	return render_template("weatherApi.html", weather=weather,coords=coords)

email=[]

@app.route("/signup", methods=["POST"])
def signup():
	form_data=request.form
	var=form_data["email"]
	#return "all ok"
	return var ## returns one or the other 
	print (var)
app.run(debug=True) # always run with debug true 



	