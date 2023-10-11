from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField

class RegisterForm(FlaskForm):
    username=StringField(label='username')
    email_address=StringField(label='email')
    password1=PasswordField(label='Your password')
    password2=PasswordField(label="Confirm Password")
    submit=SubmitField(label='submit')
