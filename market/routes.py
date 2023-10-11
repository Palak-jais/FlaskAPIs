from market import app
from flask import render_template,redirect,url_for,flash
from market.models import User
from market.forms import RegisterForm,LoginForm
from market import db

@app.route('/') #Decorator
def home_page():
    return render_template('home_page.html')

@app.route('/about') #Decorator
def about_page():
    return render_template('about_page.html')

@app.route('/expense') #Decorator
def expense_page():
    return render_template('expense_page.html')

@app.route('/login',methods=['GET','POST'])  #Decorator
def login_page():
    form=LoginForm()
   # if form.validate_on_submit():
    #    attempted_user=User.query.get(form.username.data).first()
     #   if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
      #      flash("Sucess! You are logged In")
     #       return redirect(url_for('expense_page'))
     #   else:
      #      flash('Username or Password not Matched!')
    return render_template('login_page.html',form=form)

@app.route('/register',methods=['GET','POST']) #Decorator
def register_page():
    form=RegisterForm()
    if form.validate_on_submit():
        user_to_create=User(username=form.username.data,
                            email_address=form.email_address.data,
                            password=form.password1.data)##This line go to model and set hash password before saving to db
        
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('expense_page'))
    if form.errors!={}:
        for err in form.errors.values():
            flash(err)

    return render_template('register_page.html',form=form)