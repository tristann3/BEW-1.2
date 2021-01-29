"""Create database models to represent tables."""
from events_app import db
from sqlalchemy.orm import backref
import enum
from datetime import datetime

# class EventType(enum.Enum):
#   PARTY = 1
#   STUDY = 2
#   NETWORKING = 3

class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable = False)
    email = db.Column(db.String(50), nullable = False)
    phone = db.Column(db.String(20), nullable = False)
    events_attending = db.relationship('Event', secondary='guest_event', back_populates='guests')

    def __repr__(self):
      return f'Name: {self.name}, ID: {self.id}'
    

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable = False)
    description = db.Column(db.String(50), nullable = False)
    date_and_time = db.Column(db.DateTime, nullable = False)
    num_guests = db.Column(db.Integer)
    guests = db.relationship('Guest', secondary='guest_event', back_populates='events_attending')
    # event_type = db.Column(db.Enum(EventType), default=EventType.ALL)
    
    def __repr__(self):
      return f'Title: {self.title}, ID: {self.id}'


guest_event_table = db.Table('guest_event',
  db.Column('guest_id', db.Integer, db.ForeignKey('guest.id')),
  db.Column('event_id', db.Integer, db.ForeignKey('event.id'))
)