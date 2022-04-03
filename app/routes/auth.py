from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify, session
from flask_login import LoginManager, login_user, logout_user, login_required
from ..models.models import Trainer
from ..utils.db import db

login_manager = LoginManager()


auth_bp = Blueprint("auth_bp", __name__)

@auth_bp.route('/login',methods=['GET','POST'])
def login():
     if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        trainer = Trainer.query.filter_by(username=username).first()
        if trainer:
            if Trainer.verify_password(trainer,password):  #Check the password user is the same
              login_user(trainer)
              return redirect('/protected')
            else:
              flash('Incorrect Credentials')
              print('Incorrect Password')
              return redirect('/login')
        else:
             flash('Incorrect Credentials')
             print('Trainer not exist')
             return redirect('/login')


     return render_template('login.html')


@auth_bp.route('/signup',methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if Trainer.query.filter_by(username=username).first():
            flash('User already exist')
            db.session.rollback()
            return redirect('/signup')
        if username and password:
            trainer = Trainer(username,password)
            db.session.add(trainer)
            db.session.commit()
            flash('User registered sucessfully')
            print('New Trainer register')
            return redirect('/login')

    return render_template('signup.html')




@auth_bp.route('/logout',methods=['GET'])
def logout():
    logout_user()
    #session.pop('username',None)
    if session.get('was_once_logged_in'):
        # prevent flashing automatically logged out message
        del session['was_once_logged_in']
    flash('You have successfully logged yourself out.')
    return redirect(url_for('views.home'))

