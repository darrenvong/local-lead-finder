from flask_sqlalchemy import SQLAlchemy
from setup import app

DBUSER = 'postgres'
DBPASS = 'postgres'
DBHOST = 'db'
DBPORT = '5432'
DBNAME = 'postgres'

app.config['SQLALCHEMY_DATABASE_URI'] = \
    'postgresql+psycopg2://{user}:{passwd}@{host}:{port}/{db}'.format(
        user=DBUSER,
        passwd=DBPASS,
        host=DBHOST,
        port=DBPORT,
        db=DBNAME)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "secret"

db = SQLAlchemy(app)