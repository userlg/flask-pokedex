from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .utils.db import db
from .routes import views, api, auth
from os import path
import uuid


def init_app() -> Flask:
    app = Flask(__name__)
    app.config['SECRET_KEY'] = str(uuid.uuid4())
    app.config['ENV'] = 'development'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/pokedex.sql'
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    #Register of the Blueprints
    app.register_blueprint(api.api_bp)
    app.register_blueprint(views.views)
    app.register_blueprint(auth.auth_bp)
  

    

    SQLAlchemy(app)

    return app

app = init_app()


if path.exists('app/database/pokedex.sql'):
    print("Database already exist")
else:
  with app.app_context():
      print('Database no exist <--> begin creation process')
      db.create_all()

port = 8000
