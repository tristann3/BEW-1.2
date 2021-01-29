"""Import packages and modules."""
import os
from flask import Blueprint, request, render_template, redirect, url_for, flash
from datetime import date, datetime
from books_app.models import Book, Author, Genre, User

# Import app and db from events_app package so that we can run app
from books_app import app, db

main = Blueprint("main", __name__)

##########################################
#           Routes                       #
##########################################

@main.route('/')
def homepage():
    # TODO: Make a query for all instances of 'User' and send to the template
    users = User.query.all()

    context = {
      "users": users
    }
    return render_template('home.html', **context)

@main.route('/profile/<username>')
def profile(username):
    # TODO: Make a query for the user with the given username, and send to the
    # template

    username = User.query.filter_by(username=username).one()
    
    context = {
      "username": username
    }
    return render_template('profile.html', **context)
