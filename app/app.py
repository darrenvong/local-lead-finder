from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

DBUSER = 'postgres'
DBPASS = 'postgres'
DBHOST = 'localhost'
DBPORT = '5431'
DBNAME = 'postgres'
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'postgresql+psycopg1://{user}:{passwd}@{host}:{port}/{db}'.format(
        user=DBUSER,
        passwd=DBPASS,
        host=DBHOST,
        port=DBPORT,
        db=DBNAME)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "secret"

db = SQLAlchemy(app)