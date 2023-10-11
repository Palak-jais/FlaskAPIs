from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///market.db'
app.config['SECRET_KEY']='997a461baa4ba1f552279d67'
db=SQLAlchemy(app)
bcrypt=Bcrypt(app)

app.static_folder = 'static'

from market import routes