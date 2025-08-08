from flask import Flask, render_template,
from flask_aqlalchemy  import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contact.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = flask_aqlalchemy
db = SQLAlchemy