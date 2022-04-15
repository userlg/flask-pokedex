from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify

from ..models.models import Pokemon
from ..utils.db import db

import requests

api_bp = Blueprint("api_bp", __name__)


@api_bp.route('/api',methods=['GET'])
def api():
    return render_template('signup.html')
