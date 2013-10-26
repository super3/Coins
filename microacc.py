import re
import time
import random
import hashlib
from decimal import *
getcontext().prec = 6
#from flask import Flask

# Load Settings  ---------------------------------------------------------------
#app = Flask(__name__)
#app.config.from_pyfile('settings.cfg')

# MicroAcc Class  --------------------------------------------------------------
class MicroAcc:
	"""A temporaty account to store a user's coins."""
	def __init__(self, conn, acc_hash): 
		# Grab db
		self.conn = conn # mysqlite db stuff
		self.cursor = self.conn.cursor()

		# Checking to make sure we have received a valid 10-char hash
		if self.is_hash(acc_hash):
			self.acc_hash = str(acc_hash).lower()
		# If not then we just generate a new hash. Basically ignoring 
		# the fail case of an incorrect hash, and moving on. Time will
		# tell if this will cause problems in the future. 
		else: 
			self.acc_hash = self.gen_hash()

		# Lookup account and load details, if account is not found then
		# create a new accout with the given acccount hash
		try:
			self.lookup_acc()
		except LookupError:
			self.create_acc()


	# Account Methods
	def lookup_acc(self):
		"""Check for a user account, and load details."""
		# look for account in micro_acc db
		query = "select * from micro_acc where acc_hash=? limit 1"
		self.cursor.execute(query, (self.acc_hash,))
		query_result = self.cursor.fetchone()

		# if the account is not found then raise an LookupError
		if query_result == None:
			print("Account not found")
			raise LookupError("Account hash not found.")
		# if the account is found then load db info into object
		else:
			self.acc_id = str(query_result[0])
			self.balance = float(query_result[2])
			print(self.acc_hash)
			print(self.balance)
			self.last_access = str(query_result[3])
			self.ip_addr = str(query_result[4])
			self.withdraw_addr = query_result[5]
			self.withdraw_flag = bool(query_result[6])

	def create_acc(self):
		"""Create a database entry for the account hash."""
		query = "INSERT INTO micro_acc (id, acc_hash, balance, last_access,"
		query += "ip_addr, withdraw_addr, withdraw_flag) VALUES "
		query += "(NULL, ?, 0, datetime('now','localtime'), NULL, NULL, 0)"

		self.cursor.execute(query, (self.acc_hash,))
		self.conn.commit()

		# now that the account is created we should be able to do a lookup
		self.lookup_acc()


	# Web Methods
	def give(self):	
		"""Give the user a satoshi."""
		self.balance += 0.00000001
		query = "update micro_acc set balance=(balance + 0.00000001) where id=?"
		self.cursor.execute(query, (self.acc_id,))
		self.conn.commit()
		return self

	def get_balance(self):
		return self.balance * 1000000 # convert BTC to mBTC
	def get_acc_hash(self):
		return self.acc_hash # for urls


	# Utility Methods
	def gen_hash(self):
		"""Generate a random 10-char hash."""
		ran_num = str(random.random()).encode('utf-8')
		return str(hashlib.sha1(ran_num).hexdigest())[:10].lower()
	def is_hash(self, a_hash):
		"""Check to make sure an inputted string is a hash."""
		return str(a_hash).isalnum() and len(a_hash) == 10
	def is_email(self, email):
		"""Check if the email is valid."""
		return re.match('[\.\w]{1,}[@]\w+[.]\w+', email)


	# Utility Testing
	def test_utilities(self):
		# Generate 50 hashes, and make sure there are not any duplicates
		test_hashes = []
		for i in range(50): test_hashes.append(self.gen_hash())
		assert(len(test_hashes) == len(list(set(test_hashes))))

		# Use generated data to test is_hash method
		for a_hash in test_hashes:
			assert(self.is_hash(a_hash))
		assert(not self.is_hash("Invalid Hash."))

		# Simple check of email function
		assert(self.is_email("spam@super3.org"))
		assert(not self.is_email("spamsuper3.org"))



if __name__ == "__main__":
	MicroAcc(None, "Invalid Hash.").test_utilities()
