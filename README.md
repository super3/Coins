MilliB
=====
A site dedicated to earning and playing with Bitcoin. Users are able to earn Bitcoin through faucets, referrals, ad programs, or deposits. They then can play with these coins against other players. APIs will be offered to other developers to develop games and other integration. Micro-transaction withdraws will be supported by Inputs.io and Coinbase. 

## Version 1 - Feature List##
The first version of MilliB will be a barebone faucet. This is to generate a small userbase, and test out withdrawal features. 

Only Coinbase withdrawals will be supported at first. The faucet will distribute at max 0.01 BTC a day, will allow 1 satoshi per drip, and drip intervals will be limited to 5 seconds each. This will support approximately 115.7 users at 100% request rate each day. These rates will be adjusted as time goes on.

## Setup Script

	apt-get upgrade && apt-get update
	apt-get install git flask python3
	git clone https://github.com/super3/millib.git

