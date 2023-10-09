from flask import Flask,render_template
app=Flask(__name__)
app.static_folder = 'static'

@app.route('/') #Decorator
def home_page():
    return render_template('home_page.html')


@app.route('/about') #Decorator
def about_page():
    return render_template('about_page.html')

@app.route('/expense') #Decorator
def expense_page():
    item=[
        {"id":1,"saving":2000,"item":"Car"},
           {"id":2,"saving":89000,"item":"Clothes"},
             {"id":3,"saving":45000,"item":"Pot"},
               {"id":4,"saving":90000,"item":"Bike"},
    ]
    return render_template('expense_page.html',data_value=item)

@app.route('/register') #Decorator
def register_page():
    return render_template('register_page.html')