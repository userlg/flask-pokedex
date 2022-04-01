
from ..utils.db import db
from datetime import datetime as dt


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