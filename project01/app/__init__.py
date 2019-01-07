from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('app.settings')
# app.config.from_envvar('FLASKR_SETTINGS')


db = SQLAlchemy(app)