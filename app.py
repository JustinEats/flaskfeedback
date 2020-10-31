from flask import Flask, render_template, redirect, flash, session
from models import db, connect_db, User
from secrets import KEY
from forms import RegisterUser, LoginUser

app = Flask(__name__)

app.config['SECRET_KEY'] = KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///FlaskFeedback'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
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
        session["username"] = new_user.username 
        return redirect(f'/users/{new_user.username}')
    return render_template('register.html', form=form)

@app.route('/login', methods=["GET", "POST"])
def user_login():
    form = LoginUser()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user_login = User.authenticate(username, password)
        user = User.query.filter_by(username=username).first_or_404()
        if user_login:
            session["username"] = user_login.username
            return redirect(f'/users/{user_login.username}')
        else: 
            form.username.errors =['Invalid Username/Password']
    return render_template('login.html', form=form)

@app.route('/users/<username>')
def secret_page(username):
    '''Only way to access this route is through registering or logging in a registered User'''
    form = LoginUser()
    if "username" not in session:
        #allows only the registered user in session to access.
        flash("Unauthorized. Please register/login first.")
        return redirect('/login')
    user = User.query.filter_by(username=username).first_or_404()
    if user.username == session["username"]:
        #if it's the authorized user it accesses their own information page. Else flash error if you manually do it.
        return render_template('secrets.html', user=user)
    else:
        flash("Unauthorized. You are logged in on a different account.")
        #change template to show a proper/better route if this error occurs.
    return render_template('login.html', form=form)

@app.route('/logout')
def logout_user():
    session.pop("username")
    return redirect('/')