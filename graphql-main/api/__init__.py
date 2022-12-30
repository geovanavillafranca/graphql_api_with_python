from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
# Database file is located
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.getcwd()}/todo.db/'
# disables tracking modifications of objects and sending signals to the application for every databse change
app.config['SWLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


@app.route('/')
def hello():
    return 'Hello'