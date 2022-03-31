
from ..utils.db import db


class Pokemon(db.Model):
    __tablename__ = 'pokemon'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    type1 = db.Column(db.String(25))
    description = db.Column(db.Text)

    def __init__(self, name, type1, description):
        self.name = name
        self.description = description
        self.type1 = type1