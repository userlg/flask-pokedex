from flask import Flask, flash, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from .models.models import Trainer
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin
from flask_wtf.csrf import CSRFProtect
from .utils.db import db
from .routes import views, api, auth
from os import path
import uuid

def status_401(error):
    return redirect(url_for('login'))


def status_404(error):
    return "<h1>Página no encontrada</h1>", 404


login_manager = LoginManager()
csrf = CSRFProtect()


@login_manager.user_loader
def load_user(user_id):
    #Trainer.query.get(user_id)
    #result = Trainer.query.filter_by(id=user_id).first()
    #return str(result.id)
    return Trainer.query.get(int(user_id))

@login_manager.unauthorized_handler
def unauthorized_callback():
    flash('You must be login')
    return redirect('/login')


def init_app() -> Flask:
    app = Flask(__name__)
    app.config['SECRET_KEY'] = str(uuid.uuid4())
    app.config['ENV'] = 'development'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/pokedex.sql'
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    #Csrf Protection
    csrf.init_app(app)


    #login manager use

    login_manager.init_app(app)

    #Register of the Blueprints
    app.register_blueprint(api.api_bp)
    app.register_blueprint(views.views)
    app.register_blueprint(auth.auth_bp)
    
    #Sqlalchemy Register App

    #Error Handler

    app.register_error_handler(404,status_404)
    app.register_error_handler(401,status_401)

    SQLAlchemy(app)

    return app

app = init_app()


if path.exists('app/database/pokedex.sql'):
    print("Database already exist")
else:
  with app.app_context():
      print('Database no exist <--> begin creation process')
      db.create_all()

port = 7000
