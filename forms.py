from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired, Optional

class Register(FlaskForm):
    '''Register a user'''
    username = StringField("Username:", validators=[InputRequired()])
    password = StringField("Password:", validators=[InputRequired()])
    email = StringField("E-mail", validators=[InputRequired()])
    first_name = StringField("First Name:", validators=[InputRequired()])
    last_name = StringField("Last Name:", validators=[InputRequired()])