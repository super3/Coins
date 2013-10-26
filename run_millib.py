import sqlite3
from microacc import MicroAcc
from contextlib import closing
from flask import Flask, request, session, g
from flask import abort, render_template, flash, redirect, url_for

# Flask Config -----------------------------------------------------------------
DATABASE = '/root/millib.db'
DEBUG = True

# Load Flask -------------------------------------------------------------------
app = Flask(__name__)
app.config.from_object(__name__)


# Database Functions -----------------------------------------------------------
def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

@app.before_request
def before_request():
	g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
	if hasattr(g, 'db'):
		g.db.close()

# Routes -----------------------------------------------------------------------
@app.route('/')
def index():
	acc = MicroAcc(connect_db(), "NoHash")
	return render_template('index.html', acc_hash=acc.get_acc_hash(), balance=acc.get_balance())

@app.route('/account/<acc_hash>')
def account(acc_hash):
	acc = MicroAcc(connect_db(), acc_hash)
	return render_template('index.html', acc_hash=acc.get_acc_hash(), balance=acc.get_balance())
@app.route('/give/<acc_hash>')
def give(acc_hash):
	acc = MicroAcc(connect_db(), acc_hash).give()
	return render_template('index.html', acc_hash=acc.get_acc_hash(), balance=acc.get_balance())

@app.route('/withdraw/<acc_hash>')
def withdraw(acc_hash):
	acc = MicroAcc(connect_db(), acc_hash)
	return render_template('withdraw.html', acc_hash=acc.get_acc_hash(), balance=acc.get_balance())
@app.route('/cashout/<acc_hash>')
def cashout(acc_hash):
	acc = MicroAcc(connect_db(), acc_hash).cashout()
	return render_template('withdraw.html', acc_hash=acc.get_acc_hash(), balance=acc.get_balance())


if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)