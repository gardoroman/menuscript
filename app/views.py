from flask import render_template, redirect, session, url_for, flash, request
from app import app, db
from .models import Store, Menu, Item
from wtforms import StringField
from wtforms.validators import DataRequired
from .forms import StoreForm

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

# routes for updating Store
@app.route('/new_store', methods=['GET', 'POST'])
def new_store():
    form = StoreForm()
    if form.validate_on_submit():
        new_store = Store(store_name=request.form['store_name'],
                address=request.form['address'],phone=request.form['phone'],
                cuisine_type=request.form['cuisine_type'],opening_time=request.form['opening_time'],
                closing_time=request.form['closing_time'])
        db.session.add(new_store)
        db.session.commit()
        return redirect(url_for('store', store=new_store.store_name))

    return render_template('new_store.html', form=form)
