from flask import Flask, render_template, redirect
from models import db, connect_db, User
from secrets import KEY
from forms import RegisterUser

app = Flask(__name__)

app.config['SECRET_KEY'] = KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///FlaskFeedback'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False

connect_db(app)

@app.route('/')
def redirect_register():
    return redirect('/register')

@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterUser()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        new_user = User.register(username,password,email,first_name,last_name)
        return redirect('/secret')
    return render_template('register.html', form=form)