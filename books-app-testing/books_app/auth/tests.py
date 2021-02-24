import os
from unittest import TestCase

from datetime import date
 
from books_app import app, db, bcrypt
from books_app.models import Book, Author, User, Audience

"""
Run these tests with the command:
python -m unittest books_app.main.tests
"""

#################################################
# Setup
#################################################

def create_books():
    a1 = Author(name='Harper Lee')
    b1 = Book(
        title='To Kill a Mockingbird',
        publish_date=date(1960, 7, 11),
        author=a1
    )
    db.session.add(b1)

    a2 = Author(name='Sylvia Plath')
    b2 = Book(title='The Bell Jar', author=a2)
    db.session.add(b2)
    db.session.commit()

def create_user():
    password_hash = bcrypt.generate_password_hash('password').decode('utf-8')
    user = User(username='me1', password=password_hash)
    db.session.add(user)
    db.session.commit()

#################################################
# Tests
#################################################

class AuthTests(TestCase):
    """Tests for authentication (login & signup)."""

    def setUp(self):
        """Executed prior to each test."""
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        db.drop_all()
        db.create_all()

    def test_signup(self):
        ''' Test that the user can signup '''
        form_data = {
          'username': 'signuptest',
          'password': 'signuppassword'
        }
        result = app.test_client().post('/signup', data=form_data)
        user = User.query.filter_by(username='signuptest').first()

        self.assertIsNotNone(user)
        self.assertEqual(result.status_code, 302)
        pass

    def test_signup_existing_user(self):
        ''' Test that a user cannot sign in with a duplicate username '''
        form_data = {
          'username': 'signuptest',
          'password': 'signuppassword'
        }
        response = app.test_client().post('/signup', data=form_data)
        response_text = response.get_data(as_text=True)

        self.assertNotIn('That username is taken. Please choose a different one.', response_text)
        self.assertEqual(response.status_code, 302)

    def test_login_correct_password(self):
        ''' Test that the user successfully logs in '''
        form_data = {
          'username': 'testlogin',
          'password': 'testlogin'
        }
        response = app.test_client().post('/signup', data=form_data)
        user = User.query.filter_by(username='testlogin').first()
        self.assertEqual(response.status_code, 302)

        response = app.test_client().post('/login', data=form_data)
        response_text = response.get_data(as_text=True)

        self.assertNotIn('Log In', response_text)
        self.assertEqual(response.status_code, 302)
        pass

    def test_login_nonexistent_user(self):
        # TODO: Write a test for the login route. It should:
        # - Make a POST request to /login, sending a username & password
        # - Check that the login form is displayed again, with an appropriate
        #   error message
        pass

    def test_login_incorrect_password(self):
        # TODO: Write a test for the login route. It should:
        # - Create a user
        # - Make a POST request to /login, sending the created username &
        #   an incorrect password
        # - Check that the login form is displayed again, with an appropriate
        #   error message
        pass

    def test_logout(self):
        # TODO: Write a test for the logout route. It should:
        # - Create a user
        # - Log the user in (make a POST request to /login)
        # - Make a GET request to /logout
        # - Check that the "login" button appears on the homepage
        pass
    def tearDown(self):
        pass
