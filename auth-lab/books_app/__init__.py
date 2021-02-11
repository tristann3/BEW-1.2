from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from books_app.config import Config
import os

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = os.urandom(24)

db = SQLAlchemy(app)

###########################
# Authentication
###########################

# TODO: Add authentication setup code here!

bcrypt = None # remove me! (needed so that server will run)

###########################
# Blueprints
###########################

from books_app.main.routes import main
app.register_blueprint(main)

from books_app.auth.routes import auth
app.register_blueprint(auth)

with app.app_context():
    db.create_all()
