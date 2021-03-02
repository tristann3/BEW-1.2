"""Create database models to represent tables."""
from students_app import db
from sqlalchemy.orm import backref
from flask_login import UserMixin
import enum

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    
    def __repr__(self):
        return f'<User: {self.username}>'

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
  
    def __repr__(self):
        return f'<Student: {self.first_name} {self.last_name}>'

class Professor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
  
    def __repr__(self):
        return f'<Professor: {self.first_name} {self.last_name}>'

class Class(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
  
    def __repr__(self):
        return f'<Class: {self.title}>'



