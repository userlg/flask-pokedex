
from ..utils.db import db
from datetime import datetime as dt
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin



class Trainer(db.Model, UserMixin):
    __tablename__ = 'trainer'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    created_ad = db.Column(db.DateTime, nullable=False, default=dt.now())
    captured = db.relationship('Captured', backref='trainer', lazy=True)


    def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash(password)

    def verify_password(self, password) -> bool:
        if (check_password_hash(self.password,password)):
            return True
        return False

    def is_authenticated(self):
        return True
    def is_active(self):
        return True
    def is_anonymous(self):
        return False
    def get_id(self):
        return str(self.id)


class Captured(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pokemon = db.Column(db.String(55), nullable=False)
    created_ad = db.Column(db.DateTime,default=dt.now())
    id_trainer = db.Column(db.Integer,db.ForeignKey('trainer.id'), nullable=False)




class Pokemon(db.Model):
    __tablename__ = 'pokemon'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    type1 = db.Column(db.String(25), nullable=False)
    type2 = db.Column(db.String(25), nullable=False)
    description = db.Column(db.Text, nullable=False,default="Description of Pokemon")
    created_ad = db.Column(db.DateTime, default=dt.now())

    def __init__(self, name, type1, type2 ,description):
        self.name = name
        self.description = description
        self.type1 = type1
        self.type2 = type2