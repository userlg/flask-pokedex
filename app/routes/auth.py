from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify

from ..models.models import Pokemon
from ..utils.db import db



auth_bp = Blueprint("auth_bp", __name__)

@auth_bp.route('/auth')
def login():
    return 'Welcome to the login view'


@auth_bp.route('/signup')
def signup():
    return render_template('signup.html')