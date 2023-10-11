from flask_wtf import FlaskForm
from market.models import User
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Length,EqualTo,Email,DataRequired,ValidationError

class RegisterForm(FlaskForm):
    def validate_username(self,username_to_check):
        user=User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError("Username already exists")
        
    def validate_email_address(self,email_address_to_check):
        user=User.query.filter_by(username=email_address_to_check.data).first()
        if user:
            raise ValidationError("Email already exists")    
               
    username=StringField(label='username:',validators=[Length(min=5,max=30),DataRequired()])
    email_address=StringField(label='email:',validators=[Email(),DataRequired()])
    password1=PasswordField(label='Your password:',validators=[Length(min=8),DataRequired()])
    password2=PasswordField(label="Confirm Password:",validators=[EqualTo('password1'),DataRequired()])
    submit=SubmitField(label='Create Account')

class LoginForm(FlaskForm):
    username=StringField(label='username:',validators=[DataRequired()])
    password=PasswordField(label='Your password:',validators=[DataRequired()])
    submit=SubmitField(label='Sign In')
