from sqlalchemy_utils import URLType
from grocery_app import db
from grocery_app.utils import FormEnum
from flask_login import UserMixin

class ItemCategory(FormEnum):
    """Categories of grocery items."""
    PRODUCE = 'Produce'
    DELI = 'Deli'
    BAKERY = 'Bakery'
    PANTRY = 'Pantry'
    FROZEN = 'Frozen'
    OTHER = 'Other'

class GroceryStore(db.Model):
    ''' GroceryStore Model '''
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    items = db.relationship('GroceryItem', back_populates='store')
    created_by_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_by = db.relationship('User')

    def __str__(self):
        return f'<Store: {self.title}>'

    def __repr__(self):
        return f'<Store: {self.title}>'

class GroceryItem(db.Model):
    ''' GroceryItem Model '''
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float(precision=2), nullable=False)
    category = db.Column(db.Enum(ItemCategory), default=ItemCategory.OTHER)
    photo_url = db.Column(URLType)
    # Grocery Store Foreign Key
    store_id = db.Column(
        db.Integer, db.ForeignKey('grocery_store.id'), nullable=False)
    store = db.relationship('GroceryStore', back_populates='items')
    # User ID Foreign Key
    created_by_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_by = db.relationship('User')
    # Shopping List Foreign Key
    users_who_added_to_cart = db.relationship(
       'User', secondary='user_item', back_populates='shopping_list_items')

class User(UserMixin, db.Model):
    ''' User Model '''
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    # Shopping list Foreign Key
    shopping_list_items = db.relationship(
       'GroceryItem', secondary='user_item', back_populates='users_who_added_to_cart')

    def __repr__(self):
        return f'{self.username}'

user_groceryItem_table = db.Table('user_item',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('grocery_item_id', db.Integer, db.ForeignKey('grocery_item.id'))
)
