import time
from flask import Flask, render_template, flash, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
from app import app, db


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host='0.0.0.0')
