import sqlite3
from flask import Flask, request, session, g
from flask import abort, render_template, flash, redirect, url_for

# Load Flask -------------------------------------------------------------------
app = Flask(__name__)
app.config.from_object(__name__)

# Flask Config -----------------------------------------------------------------
DATABASE = 'millib.db'

# Database Functions -----------------------------------------------------------
def connect_db():
	return sqlite3.connect(app.config['DATABASE'])