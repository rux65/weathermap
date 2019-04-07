import requests
import json
from flask import Flask , render_template, request
import gmaps 

app=Flask("myApp")
	
@app.route("/postcode", methods=["POST", "GET"])
def location():
	return render_template("weatherApi.html")

def meh():
	form_data=request.form
	var=form_data["text"]
	
	print(var)


	
endpoint = "http://api.openweathermap.org/data/2.5/weather"#- corrent one
endpoint2 ="http://api.openweathermap.org/data/2.5/forecast/"
	#print (response.url)#
	#print (response.status_code)
	#print (response.headers["content-type"])
	#print(response.text)



@app.route("/location", methods=["post"])
def weather_reply():
	form_data=request.form
	var=form_data["text"]
	
	payload = {"q":var,"units":"metric","appid":"2bb229a44403af08980fc4be234f94a9"}
	response = requests.get(endpoint, params=payload) #- correct
	red = requests.get(endpoint2, params=payload)
	api = json.loads(response.text) #- correct
	api2 = json.loads(red.text)
	coord = [api["coord"]]
	weather= [api["weather"]]
	main=[api["main"]]
	wind=api["wind"]
	
	dates=[]
	for i in range(0, len(api2["list"])):
		dates.append(api2["list"][0]["dt_txt"][0:10])
		if api2["list"][i]["dt_txt"][0:10] not in dates:
			dates.append(api2["list"][i]["dt_txt"][0:10])
	print (dates)
		
	
	#print(red.text)
	i=0
	
	
	day0=api2["list"][0]["dt_txt"][0:10]#2019-04-07
	#print(api2["list"][0]["dt_txt"][9], "lala please print")
	#print (day0)
		
	if int(api2["list"][0]["dt_txt"][8:10])+1<10:
		day1=api2["list"][0]["dt_txt"][0:9]+str(int(float(api2["list"][0]["dt_txt"][9]))+1)#2019-04-08
		#print(day1)
	else:
		day1=api2["list"][0]["dt_txt"][0:8]+str(int(float(api2["list"][0]["dt_txt"][8:10]))+1)#2019-04-08
		
		
	if int(api2["list"][0]["dt_txt"][8:10])+2<10:
		day2=api2["list"][0]["dt_txt"][0:9]+str(int(float(api2["list"][0]["dt_txt"][9]))+2)#2019-04-08
		#print(day2)
	else:
		day2=api2["list"][0]["dt_txt"][0:8]+str(int(api2["list"][0]["dt_txt"][8:10])+2)#2019-04-08
		#print(day2)
	if int(api2["list"][0]["dt_txt"][8:10])+3<10:
		day3=api2["list"][0]["dt_txt"][0:9]+str(int(api2["list"][0]["dt_txt"][9])+3)#2019-04-08
		#print (api2["list"][0]["dt_txt"][8:10])
		#print(day3)
	else:
		day3=api2["list"][0]["dt_txt"][0:8]+str(int(api2["list"][0]["dt_txt"][8:10])+3)#2019-04-08
		#print(day3)
	if int(api2["list"][0]["dt_txt"][8:10])+4<10:
		day4=api2["list"][0]["dt_txt"][0:9]+str(int(api2["list"][0]["dt_txt"][9])+4)#2019-04-08
		#print(day4)
	else:
		day4=api2["list"][0]["dt_txt"][0:8]+str(int(api2["list"][0]["dt_txt"][8:10])+4)#2019-04-08
		#print(day4)
	if int(api2["list"][0]["dt_txt"][8:10])+5<10:
		day5=api2["list"][0]["dt_txt"][0:8]+str(int(api2["list"][0]["dt_txt"][9])+5)#2019-04-08
		#print(day5)
	else:
		if api2["list"][0]["dt_txt"][5:6] in "01,03,05,07,08,10,12" and int(api2["list"][0]["dt_txt"][8:10])+5>31:
			day5=api2["list"][0]["dt_txt"][0:4]+str(int(api2["list"][0]["dt_txt"][5:7])+1)+str(int(api2["list"][0]["dt_txt"][8:10])+5-31)#2019-04-08
		elif api2["list"][0]["dt_txt"][5:6] in "04,06,09,11" and int(api2["list"][0]["dt_txt"][8:10])+5>30:
			day5=api2["list"][0]["dt_txt"][0:4]+str(int(api2["list"][0]["dt_txt"][5:7])+1)+str(int(api2["list"][0]["dt_txt"][8:10])+5-30)#2019-04-08
		else:
			day5=api2["list"][0]["dt_txt"][0:8]+str(int(api2["list"][0]["dt_txt"][8:10])+5)#2019-04-08
		#print(day5)
	
		
	count=0
	mean_temp=0
	mean_temp_low=0
	mean_temp_high=0
	mean_hum=0
	
	means_temp_low=[]
	means_temp=[]
	means_temp_high=[]
	means_humidity=[]
	condition=[]
	status=[]
	
	for i in range(0,len(api2["list"])):
		if api2["list"][i]["dt_txt"][0:10]==day0:
			mean_temp=mean_temp+float(api2["list"][i]["main"]["temp"])
			mean_temp_low=mean_temp_low+float(api2["list"][i]["main"]["temp_min"])
			mean_temp_high=mean_temp_high+float(api2["list"][i]["main"]["temp_max"])
			mean_hum=mean_hum+float(api2["list"][i]["main"]["humidity"])
			count+=1	
	total=round(mean_temp/count,2)
	means_temp.append(total)
	total=round(mean_temp_low/count,2)
	means_temp_low.append(total)
	total=round(mean_temp_high/count,2)
	means_temp_high.append(total)
	total=round(mean_hum/count,2)
	means_humidity.append(total)
	
	count=0
	mean_temp=0
	mean_temp_low=0
	mean_temp_high=0
	mean_hum=0
	
	for i in range(0,len(api2["list"])):
		if api2["list"][i]["dt_txt"][0:10]==day1:
			mean_temp=mean_temp+float(api2["list"][i]["main"]["temp"])
			mean_temp_low=mean_temp_low+float(api2["list"][i]["main"]["temp_min"])
			mean_temp_high=mean_temp_high+float(api2["list"][i]["main"]["temp_max"])
			mean_hum=mean_hum+float(api2["list"][i]["main"]["humidity"])
			count+=1	
	total=round(mean_temp/count,2)
	means_temp.append(total)
	total=round(mean_temp_low/count,2)
	means_temp_low.append(total)
	total=round(mean_temp_high/count,2)
	means_temp_high.append(total)
	total=round(mean_hum/count,2)
	means_humidity.append(total)
	
	count=0
	mean_temp=0
	mean_temp_low=0
	mean_temp_high=0
	mean_hum=0
	
	for i in range(0,len(api2["list"])):
		if api2["list"][i]["dt_txt"][0:10]==day2:
			mean_temp=mean_temp+float(api2["list"][i]["main"]["temp"])
			mean_temp_low=mean_temp_low+float(api2["list"][i]["main"]["temp_min"])
			mean_temp_high=mean_temp_high+float(api2["list"][i]["main"]["temp_max"])
			mean_hum=mean_hum+float(api2["list"][i]["main"]["humidity"])
			count+=1	
	total=round(mean_temp/count,2)
	means_temp.append(total)
	total=round(mean_temp_low/count,2)
	means_temp_low.append(total)
	total=round(mean_temp_high/count,2)
	means_temp_high.append(total)
	total=round(mean_hum/count,2)
	means_humidity.append(total)
	
	count=0
	mean_temp=0
	mean_temp_low=0
	mean_temp_high=0
	mean_hum=0
	
	for i in range(0,len(api2["list"])):
		if api2["list"][i]["dt_txt"][0:10]==day3:
			mean_temp=mean_temp+float(api2["list"][i]["main"]["temp"])
			mean_temp_low=mean_temp_low+float(api2["list"][i]["main"]["temp_min"])
			mean_temp_high=mean_temp_high+float(api2["list"][i]["main"]["temp_max"])
			mean_hum=mean_hum+float(api2["list"][i]["main"]["humidity"])
			count+=1	
	total=round(mean_temp/count,2)
	means_temp.append(total)
	total=round(mean_temp_low/count,2)
	means_temp_low.append(total)
	total=round(mean_temp_high/count,2)
	means_temp_high.append(total)
	total=round(mean_hum/count,2)
	means_humidity.append(total)
	
	count=0
	mean_temp=0
	mean_temp_low=0
	mean_temp_high=0
	mean_hum=0
	
	for i in range(0,len(api2["list"])):
		if api2["list"][i]["dt_txt"][0:10]==day4:
			mean_temp=mean_temp+float(api2["list"][i]["main"]["temp"])
			mean_temp_low=mean_temp_low+float(api2["list"][i]["main"]["temp_min"])
			mean_temp_high=mean_temp_high+float(api2["list"][i]["main"]["temp_max"])
			mean_hum=mean_hum+float(api2["list"][i]["main"]["humidity"])
			count+=1	
	total=round(mean_temp/count,2)
	means_temp.append(total)
	total=round(mean_temp_low/count,2)
	means_temp_low.append(total)
	total=round(mean_temp_high/count,2)
	means_temp_high.append(total)
	total=round(mean_hum/count,2)
	means_humidity.append(total)
	
	count=0
	mean_temp=0
	mean_temp_low=0
	mean_temp_high=0
	mean_hum=0
	
	for i in range(0,len(api2["list"])):
		if api2["list"][i]["dt_txt"][0:10]==day5:
			mean_temp=mean_temp+float(api2["list"][i]["main"]["temp"])
			mean_temp_low=mean_temp_low+float(api2["list"][i]["main"]["temp_min"])
			mean_temp_high=mean_temp_high+float(api2["list"][i]["main"]["temp_max"])
			mean_hum=mean_hum+float(api2["list"][i]["main"]["humidity"])
			count+=1
	
	total=round(mean_temp/count,2)
	means_temp.append(total)
	total=round(mean_temp_low/count,2)
	means_temp_low.append(total)
	total=round(mean_temp_high/count,2)
	means_temp_high.append(total)
	total=round(mean_hum/count,2)
	means_humidity.append(total)
	
	

	
	
	print(means_temp, means_temp_low, means_temp_high, means_humidity)	

	
	
	#r=requests.get("http://api.openweathermap.org/data/2.5/weather?lat=%f&lon=%f" %(api['coord']['lat']+0.2, api['coord']['lon']+0.2))
	#print(r.text)
	#print(weather)
	#print(response.text)
	return render_template("location.html", api=api,coord=coord, weather=weather[0],main=main, wind=wind)
	#return render_template("location.html", api=api)
	
app.run(debug=True) # always run with debug true 

