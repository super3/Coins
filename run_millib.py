import sqlite3
from flask import Flask, request, session, g
from flask import abort, render_template, flash, redirect, url_for

# Load Flask -------------------------------------------------------------------
app = Flask(__name__)
app.config.from_object(__name__)

# Flask Config -----------------------------------------------------------------
DATABASE = 'millib.db'
DEBUG = True

# Database Functions -----------------------------------------------------------
def connect_db():
	return sqlite3.connect(app.config['DATABASE'])
def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

if __name__ == '__main__':
    app.run()