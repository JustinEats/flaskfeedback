from flask import Flask, render_template, redirect, flash, session
from models import db, connect_db, User
from secrets import KEY
from forms import RegisterUser, LoginUser

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
        db.session.add(new_user)
        db.session.commit()
        #stores the new registered user
        session["username"] = new_user.id 
        return redirect('/secret')
    return render_template('register.html', form=form)

@app.route('/login', methods=["GET", "POST"])
def user_login():
    form = LoginUser()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user_login = User.authenticate(username, password)
        if user_login:
            session["username"] = user_login.id
            return redirect('/secret')
        else: 
            form.username.errors =['Invalid Username/Password']
    return render_template('login.html', form=form)

@app.route('/secret')
def secret_page():
    '''Only way to access this route is through registering or logging in a registered User'''
    if "username" not in session:
        #allows only the registered user in session to access.
        flash("Unauthorized. Please register/login first.")
        return redirect('/login')
    return render_template('secrets.html')
