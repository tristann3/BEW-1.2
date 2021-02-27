from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user

from students_app import bcrypt

auth = Blueprint('auth', __name__)

# Create your routes here.