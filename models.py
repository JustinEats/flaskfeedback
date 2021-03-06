from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(length=20), unique=True)
    password = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(length=50), unique=True, nullable=False)
    first_name = db.Column(db.Text(30), nullable=False)
    last_name = db.Column(db.Text(30), nullable=False)

    def __repr__(self):
        u = self
        return f"<User {u.username} {u.first_name} {u.last_name}>"

    @classmethod
    def register(cls, username, password,email,firstname,lastname):
        '''Register a user by hashing their password'''
        #hash the created password by the User and leave everything else as the same input
        hashed = bcrypt.generate_password_hash(password) 
        hashed_utf8 = hashed.decode("utf8")
        return cls(username=username, password=hashed_utf8, email=email, first_name=firstname,last_name=lastname)

    @classmethod
    def authenticate(cls, username, password):
        '''Authenticate/make sure it matches the registered user'''
        #Find the User first by filter then if it's the User, compare their password with the input
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            return user
        else: 
            return False

class Feedback(db.Model):
    __tablename__ = "feedbacks"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    username = db.Column(db.String(20), db.ForeignKey("users.username"))
    user = db.relationship("User", backref="feedback")

    def __repr__(self):
        f = self
        return f"<User {f.title} {f.content} {f.username}>"

def connect_db(app):
    db.app = app
    db.init_app(app)