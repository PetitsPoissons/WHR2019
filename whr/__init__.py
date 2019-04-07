from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '2705f6e3100c28bb206e6651b0e0eb89'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///whr_site.db'
db = SQLAlchemy(app)

from whr import routes