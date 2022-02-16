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
DB_URI = f'postgresql{DBDRIVER}://{DBUSER}:{DBPASS}@{DBHOST}:{DBPORT}/{DBNAME}'

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "secret"

db = SQLAlchemy(app)
db.create_all()