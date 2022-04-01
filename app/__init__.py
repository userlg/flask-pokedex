from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .utils.db import db
from .routes.views import views
import uuid


def init_app() -> Flask:
    app = Flask(__name__)
    app.config['SECRET_KEY'] = str(uuid.uuid4())
    app.config['ENV'] = 'development'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/pokedex.sql'
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    #Register of the Blueprints

    app.register_blueprint(views)

    #Creation of database in sqlite3

    

    SQLAlchemy(app)

    return app

app = init_app()

with app.app_context():
      db.create_all()

port = 7500
