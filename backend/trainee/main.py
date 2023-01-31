"""
# optin for nft / maybe if that
# list of all available nfts --> owned/created
# so trainee opts in to own one of this list
# if staff approves you'll get nft if not that's ok
# this maybe is done at a specific time if optin assumption is made
# so all trainees have to optin before a specified period of time // this might be a smart contract which does that
# there should be an ICO of some sort to make sure that all trainees optin before the ICO ends: which will be used to sign the transactions
"""

from optin import optin_for_nft
import json
import hashlib
import os
from algosdk import mnemonic
from algosdk.v2client import algod
from algosdk.future.transaction import AssetConfigTxn, wait_for_confirmation

import sys
sys.path.append(os.path.abspath('../'))

#


# For ease of reference, add account public and private keys to
# an accounts dict.
print("--------------------------------------------")
print("Creating account...")
accounts = {}
# m = create_account()
# TODO sub with wallet authentication
m = "boy peace another song inch valve feature orient brown pass junk load grocery tobacco seat return tenant journey tenant nature struggle orphan this absorb copper"
accounts[1] = {}
accounts[1]['pk'] = mnemonic.to_public_key(m)
accounts[1]['sk'] = mnemonic.to_private_key(m)

# Change algod_token and algod_address to connect to a different client
algod_token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
algod_address = "http://localhost:4001"
algod_client = algod.AlgodClient(algod_token, algod_address)

# TODO this will be an option in the web UI we only optin if the trainee wants the nft
optin_for_nft(algod_client, account=accounts[1], asset_id=1)
