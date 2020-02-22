import requests
import json
from flask import Flask , render_template, request

from flask import url_for, flash, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
#import gmaps

#imputting a secrety key to make more secure- n=random changing variable would be better

app=Flask("myApp")
app.config['SECRET_KEY'] = 'xxxxxxxxxxxxxxxx'

#setting up apps for the registationa and login forms that will be used in the main python document

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


@app.route("/home")
def home():
    return render_template('home.html', home='home')

@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/postcode", methods=["POST", "GET"])
def location():
	return render_template("weatherApi.html", title="postcode")

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

	dates=[(api2["list"][0]["dt_txt"][0:10])]
	for i in range(0, len(api2["list"])):
		if api2["list"][i]["dt_txt"][0:10] not in dates:
			dates.append(api2["list"][i]["dt_txt"][0:10])
	#print (dates)


	#print(red.text)
	i=0

	day0=dates[0]
	day1=dates[1]
	day2=dates[2]
	day3=dates[3]
	day4=dates[4]
	try:
		day5 = dates[5]
	except IndexError:
		day5 = 'null'


	means_temp_low=[]
	means_temp=[]
	means_temp_high=[]
	means_humidity=[]
	condition=[]
	status=[]

	def series(day):
		count=0
		mean_temp=0
		mean_temp_low=0
		mean_temp_high=0
		mean_hum=0
		for i in range(0,len(api2["list"])):
			if day=="nul":
				pass
			else:
				if api2["list"][i]["dt_txt"][0:10]==day:
					mean_temp=mean_temp+float(api2["list"][i]["main"]["temp"])
					mean_temp_low=mean_temp_low+float(api2["list"][i]["main"]["temp_min"])
					mean_temp_high=mean_temp_high+float(api2["list"][i]["main"]["temp_max"])
					mean_hum=mean_hum+float(api2["list"][i]["main"]["humidity"])
					count+=1
					#print(mean_temp_low)
					#print (api2["list"][i]["main"]["temp_min"])
					print (api2["list"][i]["main"]["temp_max"])
					if "12" in api2["list"][i]["dt_txt"][11:13]:
						#print (api2["list"][i]["dt_txt"][11:13])
						ind=api2["list"][i]["dt_txt"].index("12")+1
						ind2=ind+8
						condition.append(api2["list"][ind]["weather"][0]["main"])
						status.append(api2["list"][ind]["weather"][0]["description"])
						condition.append(api2["list"][ind2]["weather"][0]["main"])
						status.append(api2["list"][ind2]["weather"][0]["description"])

		if count>0:
			total=round(mean_temp/count,2)
			means_temp.append(total)
			print(mean_temp_low, "haha")
			total1=round(mean_temp_low/count,2)
			print(total1,"la")
			means_temp_low.append(total1)
			print(mean_temp_high, "haha")
			total=round(mean_temp_high/count,2)
			means_temp_high.append(total)
			total=round(mean_hum/count,2)
			means_humidity.append(total)
		else:
			pass

		return mean_temp_low

	series(day1)
	series(day2)
	#series(day3)



	print(means_temp, means_temp_low, means_temp_high, means_humidity)

	print(condition, status)

	#r=requests.get("http://api.openweathermap.org/data/2.5/weather?lat=%f&lon=%f" %(api['coord']['lat']+0.2, api['coord']['lon']+0.2))
	#print(r.text)
	#print(weather)
	#print(response.text)
	return render_template("location.html", api=api,coord=coord, weather=weather[0],main=main, wind=wind, means_temp=means_temp,means_temp_low=means_temp_low, means_temp_high=means_temp_high, means_humidity=means_humidity, day2=day2, status=status, condition=condition )
	#return render_template("location.html", api=api)



@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Account created!', 'success')
        return redirect(url_for('home'))
    return render_template('Register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        #no database create therefore can only login with this and no other email or password 'created' on the registration form
        if form.email.data == 'weathermap@gmail.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('Login.html', title='Login', form=form)
#app.run(debug=True) # always run with debug true
