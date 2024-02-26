from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import json

# Load configuration from config.json
with open('config.json', 'r') as c:
    params = json.load(c)["params"]

# Create Flask app
app = Flask(__name__)
app.secret_key = 'super-secret-key'

# Configure SQLAlchemy to use MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
db = SQLAlchemy(app)

# Define Shop model with an explicit table name
class Shop(db.Model):
    __tablename__ = 'shops'
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50), nullable=False)
    shop_name = db.Column(db.String(50), unique=True, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(15), unique=True, nullable=False)

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



@app.route("/")
def Home():
    return render_template('add_shop.html',params=params)
# Run the app
if __name__ == '__main__':
    app.run(debug=True)
