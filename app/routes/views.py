from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..models.models import Pokemon
#from  app.utils.db import db

views = Blueprint("views", __name__)


@views.route('/')
def index():
    return render_template('index.html')
