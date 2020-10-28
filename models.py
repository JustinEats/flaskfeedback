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
    first_name = db.Column(db.Text(length=30), nullable=False)
    last_name = db.Column(db.Text(length=30), nullable=False)

def connect_db(app):
    db.app = app
    db.init_app(app)