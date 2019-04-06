#import requests
import json
from flask import Flask , render_template, request, url_for, flash, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
#import gmaps


#imputting a secrety key to make more secure- n=random changing variable would be better
app=Flask("myApp")
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

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

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', home='home')

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/postcode", methods=["POST", "GET"])
def location():
	return render_template("weatherApi.html", title='postcode' )

def meh():
	form_data=request.form
	var=form_data["text"]

	print(var)



endpoint = "http://api.openweathermap.org/data/2.5/weather"
endpoint2 = "http://api.openweathermap.org/data/2.5/weather"
	#print (response.url)#
	#print (response.status_code)
	#print (response.headers["content-type"])
	#print(response.text)


@app.route("/location", methods=["post"])
def weather_reply():
	form_data=request.form
	var=form_data["text"]
	payload = {"q":var, "units":"metric", "appid":"2bb229a44403af08980fc4be234f94a9"}
	response = requests.get(endpoint, params=payload, data={"key":"value"})
	api = json.loads(response.text)
	coord = [api["coord"]]
	weather= api["weather"]
	main=[api["main"]]
	wind=api["wind"]
	#print (api["coord"]["lon"]+1)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Account created!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

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
    return render_template('login.html', title='Login', form=form)

#r=requests.get("http://api.openweathermap.org/data/2.5/weather?lat=%f&lon=%f" %(api['coord']['lat']+0.2, api['coord']['lon']+0.2))
#print(r.text)

#print(response.text)
#return render_template("location.html", api=api,coord=coord, weather=weather,main=main, wind=wind)


app.run(debug=True) # always run with debug true
