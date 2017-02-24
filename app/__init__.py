from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import basedir
import os


app = Flask(__name__)
# app.config.from_object('config')

#from real python
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from app import views, models
