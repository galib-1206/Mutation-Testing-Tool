# coding=utf-8

from flask import Flask
from flask_compress import Compress
from flask_sqlalchemy import SQLAlchemy
from flask_humanize import Humanize
import os.path
import sys

sys.path.append( os.path.dirname( os.path.abspath( __file__ ) ) )

app = Flask(__name__)
app.config.from_object('config')

Compress(app)

db = SQLAlchemy(app)

humanize = Humanize(app)

# noinspection PyPep8
from app import views, models
