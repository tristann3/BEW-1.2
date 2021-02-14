from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, FloatField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, URL
from grocery_app.models import ItemCategory, GroceryStore, GroceryItem

class GroceryStoreForm(FlaskForm):
    """Form for adding/updating a GroceryStore."""
    title = StringField('Title', validators=[DataRequired(), Length(min=3, max=80)])
    address = StringField('Address', validators=[DataRequired(), Length(min=3, max=150)])    
    submit = SubmitField('Submit')

class GroceryItemForm(FlaskForm):
    """Form for adding/updating a GroceryItem."""
    name = StringField('Name', validators=[DataRequired(), Length(min=3, max=80)])
    price = FloatField('Price', validators=[DataRequired()])
    category = SelectField('Category', choices=ItemCategory.choices())
    photo_url = StringField('Photo', validators=[DataRequired(), Length(min=3, max=80)])
    store = QuerySelectField('Store', query_factory=lambda: GroceryStore.query)    
    submit = SubmitField('Submit')
