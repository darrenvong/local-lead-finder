from os import environ
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

DBUSER = 'postgres'
DBPASS = 'postgres'
DBHOST =  environ.get('DB_HOST', 'localhost')
DBPORT = '5432'
DBNAME = 'local-leader'
DBDRIVER = '+psycopg2'
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'postgresql{driver}://{user}:{passwd}@{host}:{port}/{db}'.format(
        driver=DBDRIVER,
        user=DBUSER,
        passwd=DBPASS,
        host=DBHOST,
        port=DBPORT,
        db=DBNAME)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "secret"

db = SQLAlchemy(app)
db.create_all()