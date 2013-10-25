MilliB
=====
A site dedicated to earning and playing with Bitcoin. Users are able to earn Bitcoin through faucets, referrals, ad programs, or deposits. They then can play with these coins against other players. APIs will be offered to other developers to develop games and other integration. Micro-transaction withdraws will be supported by Inputs.io and Coinbase. 

## Version 1 - Feature List##
The first version of MilliB will be a barebone faucet. This is to generate a small userbase, and test out withdrawal features. 

Only Coinbase withdrawals will be supported at first. The faucet will distribute at max 0.01 BTC a day, will allow 1 satoshi per drip, and drip intervals will be limited to 5 seconds each. This will support ~60 users at 100% request rate each day. These rates will be adjusted as time goes on. Micro-accounts will hold user's balances. Balances not claimed after 48 hours will be returned to the website.

## Setup Script ##

	apt-get upgrade && apt-get update
	apt-get install git flask python3
	git clone https://github.com/super3/millib.git

## Database Setup ##
MilliB is run on Flask's flavor of [SQLite](http://flask.pocoo.org/docs/patterns/sqlite3/). If possible we want to keep a single table database (for simplicity's sake). Backing up regularly is good as well. 

	/*drop table if exists micro_acc;*/
	create table micro_acc (
	  id integer primary key autoincrement,
	  acc_hash text not null,
	  balance real not null,
	  last_access text not null,
	  withdraw_addr text null,
	  withdraw_flag integer not null
	);
Most of the fields are self explanatory, but here are some additional information on the uses of some of the fields.

- **acc_hash** - This is the database lookup key, and access key for a micro-account. With this hash the user has the ability to add and remove funds from the micro-account. This will generated at page load time, displayed to the user in plain-text, and be passed in GET on account actions. Normally this would be a problem, but accounts are assumed to contain negligible balances for short time periods. 
- **balance** - The Bitcoin balance that is owed to the user for that account. Denoted in BTC not mBTC.
- **last_access** - Used to limit bot attacks, by limiting the times a user can access an account a second. Will also be used to determine when to reclaim balances on micro-accounts. 
- **withdraw_addr** - Coinbase email that the balance will be paid to. 
- **withdraw_flag** - Python daemon will search for this flag, and payout the balance on this account. 

## Routes ##
The following is a listing for all coded routes.

	/*						- Website index page
	/account/<acc_hash>		- Website index page w/ micro-account balance
	/give/<acc_hash>		- Redirects to /account after increment balance
	/withdraw/<acc_hash>	- Allows user to set withdraw email address
	/cashout/<acc_hash>		- Redirects to /withdraw after setting withdraw_flag

## MicroAcc Object ##
Nothing here yet.