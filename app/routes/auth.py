from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify

from ..models.models import Pokemon, Trainer
from ..utils.db import db



auth_bp = Blueprint("auth_bp", __name__)

@auth_bp.route('/auth')
def login():
    return 'Welcome to the login view'


@auth_bp.route('/signup',methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username and password:
            trainer = Trainer(username,password)
            db.session.add(trainer)
            db.session.commit()
            print('New Trainer register')
        else:
            return redirect('/signup')
    return render_template('signup.html')