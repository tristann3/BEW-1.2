from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from datetime import date, datetime
from students_app.models import  User
# from students_app.main.forms import BookForm, AuthorForm, GenreForm
from students_app import bcrypt

# Import app and db
from students_app import app, db
main = Blueprint('main', __name__)

# Create your routes here.
@main.route('/')
def homepage():
    all_users = User.query.all()
    return render_template('home.html',
        all_users=all_users)