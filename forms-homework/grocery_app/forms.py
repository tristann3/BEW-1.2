from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, FloatField, PasswordField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, ValidationError, URL
from grocery_app.models import ItemCategory, GroceryStore, GroceryItem, User

class GroceryStoreForm(FlaskForm):
    ''' Form for adding/updating a GroceryStore '''
    title = StringField('Title', validators=[DataRequired(), Length(min=3, max=80)])
    address = StringField('Address', validators=[DataRequired(), Length(min=3, max=150)])    
    submit = SubmitField('Submit')

class GroceryItemForm(FlaskForm):
    ''' Form for adding/updating a GroceryItem '''
    name = StringField('Name', validators=[DataRequired(), Length(min=3, max=80)])
    price = FloatField('Price', validators=[DataRequired()])
    category = SelectField('Category', choices=ItemCategory.choices())
    photo_url = StringField('Photo', validators=[DataRequired(), Length(min=3, max=80)])
    store = QuerySelectField('Store', query_factory=lambda: GroceryStore.query)    
    submit = SubmitField('Submit')

class SignUpForm(FlaskForm):
    ''' Form for adding a User '''
    username = StringField('User Name',
        validators=[DataRequired(), Length(min=3, max=50)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    ''' Form for logging in a User '''
    username = StringField('User Name',
        validators=[DataRequired(), Length(min=3, max=50)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')
