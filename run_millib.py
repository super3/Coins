# Python Imports
import re
import sys
import sqlite3
import hashlib
from random import randint
from datetime import datetime

# Flask Imports
from flask import g
from flask import Flask
from flask import url_for
from flask import request
from flask import redirect
from flask import render_template
from contextlib import closing

# Logging Imports
import logging
from logging import Formatter
from logging.handlers import RotatingFileHandler

# Load Flask -------------------------------------------------------------------
app = Flask(__name__)
app.config.from_pyfile('settings.cfg')

# Database Functions -----------------------------------------------------------
def connect_db():
        return sqlite3.connect(app.config['DATABASE_FILE'])