from flask import Blueprint, request, render_template, redirect, url_for, flash
from datetime import date, datetime
from grocery_app.models import GroceryStore, GroceryItem
from grocery_app.forms import GroceryStoreForm, GroceryItemForm

# Import app and db from events_app package so that we can run app
from grocery_app import app, db

main = Blueprint("main", __name__)

##########################################
#           Routes                       #
##########################################

@main.route('/')
def homepage():
    '''Route to deliver homepage to the front end'''
    all_stores = GroceryStore.query.all()
    return render_template('home.html', all_stores=all_stores)

@main.route('/new_store', methods=['GET', 'POST'])
def new_store():
    '''Route to deliver form inputs for user to enter a new store'''
    form = GroceryStoreForm()

    if form.validate_on_submit():
      new_store = GroceryStore(
        title = form.title.data,
        address = form.address.data,
      )
      db.session.add(new_store)
      db.session.commit()

      flash("New store was created successfully")
      return redirect(url_for('main.store_detail', store_id=new_store.id))

    return render_template('new_store.html', form=form)

@main.route('/new_item', methods=['GET', 'POST'])
def new_item():
    '''Route to deliver form inputs for user to enter a new item'''
    form = GroceryItemForm()
    
    if form.validate_on_submit():
      new_item = GroceryItem(
        name = form.name.data,
        price = form.price.data,
        category = form.category.data,
        photo_url = form.photo_url.data,
        store = form.store.data
      )
      db.session.add(new_item)
      db.session.commit()

      flash("New item was created successfully")
      return redirect(url_for('main.item_detail', item_id=new_item.id))

    return render_template('new_item.html', form=form)

@main.route('/store/<store_id>', methods=['GET', 'POST'])
def store_detail(store_id):
    '''Route to deliver store details by ID'''
    store = GroceryStore.query.get(store_id)

    form = GroceryStoreForm(obj=store)

    if form.validate_on_submit():
      store.query.filter_by(id=store_id)
      store.name = form.name.data
      store.address = form.address.data
      store.items = form.items.data

      db.session.add(store)
      db.session.commit()

    return render_template('store_detail.html', store=store, form=form)

@main.route('/item/<item_id>', methods=['GET', 'POST'])
def item_detail(item_id):
    '''Route to deliver item details by ID'''
    item = GroceryItem.query.get(item_id)
    form = GroceryItemForm(obj=item)

    if form.validate_on_submit():
      item.query.filter_by(id=item_id)
      item.name = form.name.data
      item.price = form.price.data
      item.category = form.category.data
      item.photo_url = form.photo_url.data
      item.store = form.store.data

      db.session.add(item)
      db.session.commit()

    return render_template('item_detail.html', item=item, form=form)

