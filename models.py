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

    @classmethod
    def register(cls, username, password,email,firstname,lastname):
        '''Register a user by hashing their password'''
        hashed = bcrypt.generate_password_hash(password)
        hashed_utf8 = hashed.decode("utf8")
        return cls(username=username, password=hashed_utf8, email=email, first_name=firstname,last_name=lastname)

def connect_db(app):
    db.app = app
    db.init_app(app)