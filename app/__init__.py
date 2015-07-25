from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

app = Flask(__name__, static_url_path='')
app.config.from_object('config')


db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


#late import
from app import views
from models import db
db.init_app(app)
