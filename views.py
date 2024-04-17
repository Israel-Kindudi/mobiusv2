from flask import Blueprint, jsonify, request, render_template,send_from_directory
#from .models import User
from . import db
from flask import redirect,url_for
from werkzeug.security import generate_password_hash,check_password_hash
views = Blueprint('views',__name__)


@views.route('/', methods=['GET'])
def home():
    return render_template('index.html')