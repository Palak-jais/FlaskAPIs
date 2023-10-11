from market import app
from flask import render_template
from market.models import Item
from market.forms import RegisterForm
@app.route('/') #Decorator
def home_page():
    return render_template('home_page.html')


@app.route('/about') #Decorator
def about_page():
    return render_template('about_page.html')

@app.route('/expense') #Decorator
def expense_page():

    item=Item.query.all()
    return render_template('expense_page.html',data_value=item)

@app.route('/register') #Decorator
def register_page():
    form=RegisterForm()
    return render_template('register_page.html',form=form)