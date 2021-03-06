from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Optional

class RegisterUser(FlaskForm):
    '''Register a user form'''
    username = StringField("Username:", validators=[InputRequired()])
    password = PasswordField("Password:", validators=[InputRequired()])
    email = StringField("E-mail:", validators=[InputRequired()])
    first_name = StringField("First Name:", validators=[InputRequired()])
    last_name = StringField("Last Name:", validators=[InputRequired()])

class LoginUser(FlaskForm):
    '''Logging in form for registered user'''
    username = StringField("Username:", validators=[InputRequired()])
    password = PasswordField("Password:", validators=[InputRequired()])

class FeedbackForm(FlaskForm):
    '''Add a feedback on user'''
    title = StringField("Title:", validators=[InputRequired()])
    feedback = StringField("Feedback:", validators=[InputRequired()])