from flask import Flask, render_template, request,session,redirect,flash,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from datetime import datetime
import json
import os
import pandas as pd

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import json
# import count_vect

from flask import Flask, jsonify, request
import numpy as np

import pandas as pd
import numpy as np



import re

with open('config.json', 'r') as c:
    params = json.load(c)["params"]

# load the model from disk


local_server = True
app = Flask(__name__,template_folder='templates')
app.secret_key = 'super-secret-key'

app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = params['gmail_user']
app.config['MAIL_PASSWORD'] = params['gmail_password']
mail = Mail(app)

if(local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']

db = SQLAlchemy(app)



# Define Shop model with an explicit table name
class Shop(db.Model):
    __tablename__ = 'shops'
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50), nullable=False)
    shop_name = db.Column(db.String(50), unique=True, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(15), unique=True, nullable=False)


class Register(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    uname = db.Column(db.String(50), nullable=False)
    mobile = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(10), nullable=False)
    cpassword = db.Column(db.String(10), nullable=False)

class Contact(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50),nullable=False)
    email=db.Column(db.String(50),nullable=False)
    subject=db.Column(db.String(50),nullable=False)
    message=db.Column(db.String(250),nullable=False)

from flask_sqlalchemy import SQLAlchemy

# Assuming you already have the 'db' instance created
# db = SQLAlchemy(app)

class Restaurants(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shop_name = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(15), nullable=False)

class Hotels(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shop_name = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(15), nullable=False)

class BeautySpa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shop_name = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(15), nullable=False)

from flask_sqlalchemy import SQLAlchemy

# Assuming you already have the 'db' instance created
# db = SQLAlchemy(app)

class HomeDecor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shop_name = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(15), nullable=False)

class WeddingRequisites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shop_name = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(15), nullable=False)

class Education(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shop_name = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(15), nullable=False)

class Hospitals(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shop_name = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(15), nullable=False)

class Contractors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shop_name = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(15), nullable=False)

class PetShops(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shop_name = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(15), nullable=False)

class Dentists(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shop_name = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(15), nullable=False)

class Gym(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shop_name = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(15), nullable=False)

class Consultants(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shop_name = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(15), nullable=False)

class EventOrganisers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shop_name = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(15), nullable=False)

class DrivingSchools(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shop_name = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(15), nullable=False)

class PackersMovers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shop_name = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(15), nullable=False)

class CourierService(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shop_name = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(15), nullable=False)


@app.route('/dashboard')
def dashboard():
    # Query shops for each category
    restaurants = Shop.query.filter_by(category='Restaurants').all()
    hotels = Shop.query.filter_by(category='Hotels').all()
    beauty_spa = Shop.query.filter_by(category='Beauty Spa').all()
    home_decor = Shop.query.filter_by(category='Home Decor').all()
    wedding_requisites = Shop.query.filter_by(category='Wedding Requisites').all()
    education = Shop.query.filter_by(category='Education').all()
    hospitals = Shop.query.filter_by(category='Hospitals').all()
    contractors = Shop.query.filter_by(category='Contractors').all()
    pet_shops = Shop.query.filter_by(category='Pet Shops').all()
    dentists = Shop.query.filter_by(category='Dentists').all()
    gym = Shop.query.filter_by(category='Gym').all()
    consultants = Shop.query.filter_by(category='Consultants').all()
    event_organisers = Shop.query.filter_by(category='Event Organisers').all()
    driving_schools = Shop.query.filter_by(category='Driving Schools').all()
    packers_movers = Shop.query.filter_by(category='Packers & Movers').all()
    courier_service = Shop.query.filter_by(category='Courier Service').all()

    return render_template('dashboard.html', params=params,
                           restaurants=restaurants,
                           hotels=hotels,
                           beauty_spa=beauty_spa,
                           home_decor=home_decor,
                           wedding_requisites=wedding_requisites,
                           education=education,
                           hospitals=hospitals,
                           contractors=contractors,
                           pet_shops=pet_shops,
                           dentists=dentists,
                           gym=gym,
                           consultants=consultants,
                           event_organisers=event_organisers,
                           driving_schools=driving_schools,
                           packers_movers=packers_movers,
                           courier_service=courier_service
                           )


@app.route("/logout", methods = ['GET','POST'])
def logout():
    session.pop('email')
    return redirect(url_for('Home'))




from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Assuming you already have models defined for all categories

@app.route('/add_shop1', methods=['GET', 'POST'])
def add_shop1():
    if request.method == 'POST':
        category = request.form['category']
        shop_name = request.form['shop_name']
        location = request.form['location']
        contact = request.form['contact']

        # Check if shop_name is not repeated in the specific category
        existing_shop = globals()[category.capitalize()].query.filter_by(shop_name=shop_name).first()
        if existing_shop:
            return "Shop name already exists in this category. Choose a different name."

        # Check if contact is not repeated in the specific category
        existing_contact = globals()[category.capitalize()].query.filter_by(contact=contact).first()
        if existing_contact:
            return "Contact number already exists in this category. Choose a different number."

        # Create a new shop entry based on the selected category
        new_shop = globals()[category.capitalize()](shop_name=shop_name, location=location, contact=contact)
        db.session.add(new_shop)
        db.session.commit()

        return "Shop added successfully!"

    return render_template('add_shop1.html')




@app.route("/")
def Home():
    return render_template('index.html',params=params)

@app.route("/about")
def About():
    return render_template('about.html',params=params)

@app.route("/register", methods=['GET','POST'])
def register():
    if(request.method=='POST'):
        name = request.form.get('name')
        uname = request.form.get('uname')
        mobile = request.form.get('mobile')
        email= request.form.get('email')
        password= request.form.get('password')
        cpassword= request.form.get('cpassword')

        user=Register.query.filter_by(email=email).first()
        if user:
            flash('Account already exist!Please login','success')
            return redirect(url_for('register'))
        if not(len(name)) >3:
            flash('length of name is invalid','error')
            return redirect(url_for('register')) 
        if (len(mobile))<10:
            flash('invalid mobile number','error')
            return redirect(url_for('register')) 
        if (len(password))<8:
            flash('length of password should be greater than 7','error')
            return redirect(url_for('register'))
        else:
             flash('You have registtered succesfully','success')
            
        entry = Register(name=name,uname=uname,mobile=mobile,email=email,password=password,cpassword=cpassword)
        db.session.add(entry)
        db.session.commit()
    return render_template('register.html',params=params)

@app.route("/login",methods=['GET','POST'])
def login():
    if (request.method== "GET"):
        if('email' in session and session['email']):
            return render_template('dashboard.html',params=params)
        else:
            return render_template("login.html", params=params)

    if (request.method== "POST"):
        email = request.form.get('email')
        password = request.form.get('password')
        
        login = Register.query.filter_by(email=email, password=password).first()
        if login is not None:
            session['email']=email
            return render_template('dashboard.html',params=params)
        else:
            flash("plz enter right password",'error')
            return render_template('login.html',params=params)



@app.route("/contact",  methods=['GET','POST'])
def contact():
    if(request.method =='POST'):
        name=request.form.get('name')
        email=request.form.get('email')
        subject=request.form.get('subject')
        message=request.form.get('message')
        entry=Contact(name=name,email=email,subject=subject,message=message)
        db.session.add(entry)
        db.session.commit()
    return render_template('contact.html',params=params)
"""
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')"""

from flask import render_template


# Route to add a new shop
@app.route("/add_shop", methods=['GET', 'POST'])
def add_shop():
    if request.method == 'POST':
        category = request.form.get('category')
        shop_name = request.form.get('shop_name')
        location = request.form.get('location')
        contact = request.form.get('contact')

        # Check if shop_name and contact are unique
        if Shop.query.filter_by(shop_name=shop_name).first() is not None:
            flash('Shop name already exists. Choose a different name.', 'error')
            return redirect(url_for('add_shop'))

        if Shop.query.filter_by(contact=contact).first() is not None:
            flash('Mobile number already exists. Choose a different number.', 'error')
            return redirect(url_for('add_shop'))

        # Create a new Shop instance and add it to the database
        new_shop = Shop(category=category, shop_name=shop_name, location=location, contact=contact)
        db.session.add(new_shop)
        db.session.commit()

        flash('Shop added successfully!', 'success')
        return redirect(url_for('shop_list'))

    return render_template('add_shop.html', params=params)

# Route to display a list of shops
@app.route("/shop_list")
def shop_list():
    shops = Shop.query.all()
    return render_template('shop_list.html', params=params, shops=shops)



"""@app.route("/")
def Home():
    return render_template('add_shop.html',params=params)"""


from flask import render_template

# Define routes for each category
@app.route('/restaurants')
def show_restaurants():
    restaurants = Restaurants.query.all()
    return render_template('restaurants.html', restaurants=restaurants)

@app.route('/hotels')
def hotels():
    hotels = Shop.query.filter_by(category='Hotels').all()
    return render_template('Hotels.html', params=params, shops=hotels)

@app.route('/beauty_spa')
def beauty_spa():
    beauty_spa = Shop.query.filter_by(category='Beauty Spa').all()
    return render_template('Beauty Spa.html', params=params, shops=beauty_spa)

# Add more routes for other categories as needed

@app.route('/home_decor')
def home_decor():
    home_decor = Shop.query.filter_by(category='Home Decor').all()
    return render_template('Home Decor.html', params=params, shops=home_decor)

@app.route('/wedding_requisites')
def wedding_requisites():
    wedding_requisites = Shop.query.filter_by(category='Wedding Requisites').all()
    return render_template('Wedding Requisites.html', params=params, shops=wedding_requisites)

@app.route('/education')
def education():
    education = Shop.query.filter_by(category='Education').all()
    return render_template('Education.html', params=params, shops=education)

@app.route('/hospitals')
def hospitals():
    hospitals = Shop.query.filter_by(category='Hospitals').all()
    return render_template('Hospitals.html', params=params, shops=hospitals)

@app.route('/contractors')
def contractors():
    contractors = Shop.query.filter_by(category='Contractors').all()
    return render_template('Contractors.html', params=params, shops=contractors)

@app.route('/pet_shops')
def pet_shops():
    pet_shops = Shop.query.filter_by(category='Pet Shops').all()
    return render_template('Pet Shops.html', params=params, shops=pet_shops)

@app.route('/dentists')
def dentists():
    dentists = Shop.query.filter_by(category='Dentists').all()
    return render_template('Dentists.html', params=params, shops=dentists)

@app.route('/gym')
def gym():
    gym = Shop.query.filter_by(category='Gym').all()
    return render_template('Gym.html', params=params, shops=gym)

@app.route('/consultants')
def consultants():
    consultants = Shop.query.filter_by(category='Consultants').all()
    return render_template('Consultants.html', params=params, shops=consultants)

@app.route('/event_organisers')
def event_organisers():
    event_organisers = Shop.query.filter_by(category='Event Organisers').all()
    return render_template('Event Organisers.html', params=params, shops=event_organisers)

@app.route('/driving_schools')
def driving_schools():
    driving_schools = Shop.query.filter_by(category='Driving Schools').all()
    return render_template('Driving Schools.html', params=params, shops=driving_schools)

@app.route('/packers_movers')
def packers_movers():
    packers_movers = Shop.query.filter_by(category='Packers & Movers').all()
    return render_template('Packers & Movers.html', params=params, shops=packers_movers)

@app.route('/courier_service')
def courier_service():
    courier_service = Shop.query.filter_by(category='Courier Service').all()
    return render_template('Courier Service.html', params=params, shops=courier_service)











if __name__ == '__main__':
    app.run(debug=True)