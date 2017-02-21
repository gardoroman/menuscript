from flask import render_template, redirect, session, url_for, flash, request
from app import app, db
from .models import Store, Menu, Item
from wtforms import StringField
from wtforms.validators import DataRequired
from .forms import StoreForm, MenuForm, ItemForm

# view for all stores
@app.route('/')
@app.route('/index')
def index():
    stores = Store.query.all()
    return render_template('index.html',
                            stores=stores)

@app.route('/store/<store_name>')
def store(store_name):
    store = Store.query.filter_by(store_name=store_name).first()
    if store is None:
        flash('Store %s not found.' % store_name)
        return redirect(url_for('index'))
    return render_template('store.html', store=store)

@app.route('/menu/<menu_id>')
def menu(menu_id):
    menu = Menu.query.get(int(menu_id))
    store = Store.query.get(menu.store_id)
    if menu is None:
        flash('Menu %s not found.' % menu_id)
        return redirect(url_for('index'))
    return render_template('menu.html', menu=menu, store=store)

# route for updating Store
@app.route('/new_store', methods=['GET', 'POST'])
def new_store():
    form = StoreForm()
    if form.validate_on_submit():
        # there has to be a better way to update
        new_store = Store(store_name=request.form['store_name'],
                address=request.form['address'],phone=request.form['phone'],
                cuisine_type=request.form['cuisine_type'],opening_time=request.form['opening_time'],
                closing_time=request.form['closing_time'])
        db.session.add(new_store)
        db.session.commit()
        return redirect(url_for('store', store_name=new_store.store_name))
    return render_template('new_store.html', form=form)

@app.route('/new_menu/<int:store_id>', methods=['GET', 'POST'])
def new_menu(store_id):
    form = MenuForm()
    menu = Menu(store_id=store_id)
    if form.validate_on_submit():
        menu.category = request.form['category']
        db.session.add(menu)
        db.session.commit()
        return redirect(url_for('menu', menu_id=menu.id))
    return render_template('new_menu.html', form=form)

@app.route('/new_item/<int:menu_id>', methods=['GET', 'POST'])
def new_item(menu_id):
    form = ItemForm()
    item = Item(menu_id=menu_id)
    if form.validate_on_submit():
        item.item_name = request.form['item_name']
        item.description = request.form['description']
        item.section = request.form['section']
        db.session.add(item)
        db.session.commit()
        return redirect(url_for('menu', menu_id=menu_id))
    return render_template('new_item.html', form=form)
