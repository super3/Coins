import re
import time
import random
import hashlib
#from flask import Flask

# Load Settings  ---------------------------------------------------------------
#app = Flask(__name__)
#app.config.from_pyfile('settings.cfg')

# MicroAcc Class  --------------------------------------------------------------
class MicroAcc:
		def __init__(self): pass

		# Real Methods
		def new(self):
			"""Create a new micro-account."""
			acc_hash = self.gen_hash()
			#last_access = 

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

		# Unit Testing Method
		def test(self):
			# Generate 50 hashes, and make sure there are not any duplicates
			test_hashes = []
			for i in range(50): test_hashes.append(self.gen_hash())
			assert(len(test_hashes) == len(list(set(test_hashes))))

			# Use generated data to test is_hash method
			for a_hash in test_hashes:
				assert(self.is_hash(a_hash))

			# Simple check of email function
			assert(self.is_email("spam@super3.org"))
			assert(not self.is_email("spamsuper3.org"))

if __name__ == "__main__":
	MicroAcc().test()