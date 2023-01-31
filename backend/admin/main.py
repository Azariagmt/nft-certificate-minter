from utils import *
from create_account import create_account
from closeout_account import closeout_account
import json
import hashlib
import os

from algosdk import mnemonic
from algosdk.v2client import algod
from algosdk.future.transaction import AssetConfigTxn, AssetTransferTxn, wait_for_confirmation

import sys
sys.path.append(os.path.abspath('../'))

#

# only the staff account will be creating this asset
# For ease of reference, add account public and private keys to
# an accounts dict.
print("--------------------------------------------")
print("Creating account...")
accounts = {}
# m = create_account()
# TODO sub with wallet authentication
m = "tissue box sorry craft gauge taste file hollow frown green cereal hat struggle chase paddle gossip address regular onion turn marriage father flash above useful"
accounts[1] = {}
accounts[1]['pk'] = mnemonic.to_public_key(m)
accounts[1]['sk'] = mnemonic.to_private_key(m)

# Change algod_token and algod_address to connect to a different client
algod_token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
algod_address = "http://localhost:4001"
algod_client = algod.AlgodClient(algod_token, algod_address)


def create_non_fungible_token():
    print("--------------------------------------------")
    print("Creating Asset...")
    # CREATE ASSET
    # Get network params for transactions before every transaction.
    params = algod_client.suggested_params()
    # comment these two lines if you want to use suggested params
    # params.fee = 1000
    # params.flat_fee = True

    # JSON file
    dir_path = os.path.dirname(os.path.realpath(__file__))
    f = open(dir_path + '/azariaNFTmetadata.json', "r")

    # Reading from file
    metadataJSON = json.loads(f.read())
    metadataStr = json.dumps(metadataJSON)

    hash = hashlib.new("sha256")
    hash.update(b"arc0003/amj")
    hash.update(metadataStr.encode("utf-8"))
    json_metadata_hash = hash.digest()

    # Account 1 creates an asset called latinum and
    # sets Account 1 as the manager, reserve, freeze, and clawback address.
    # Asset Creation transaction
    txn = AssetConfigTxn(
        sender=accounts[1]['pk'],
        sp=params,
        total=1,
        default_frozen=False,
        unit_name="AZARIAB4",
        asset_name="Azaria's completion certificate",
        manager=accounts[1]['pk'],
        reserve=None,
        freeze=None,
        clawback=None,
        strict_empty_address_check=False,
        url="https://gateway.pinata.cloud/ipfs/QmW22vrt2pGZi48aJUjXhwPkQf58LJraCLr63Cys2cHopm",
        metadata_hash=json_metadata_hash,
        decimals=0)

    # Sign with secret key of creator
    stxn = txn.sign(accounts[1]['sk'])

    # Send the transaction to the network and retrieve the txid.
    txid = algod_client.send_transaction(stxn)
    print("Asset Creation Transaction ID: {}".format(txid))

    # Wait for the transaction to be confirmed
    confirmed_txn = wait_for_confirmation(algod_client, txid, 4)
    print("TXID: ", txid)
    print("Result confirmed in round: {}".format(
        confirmed_txn['confirmed-round']))
    try:
        # Pull account info for the creator
        # account_info = algod_client.account_info(accounts[1]['pk'])
        # get asset_id from tx
        # Get the new asset's information from the creator account
        ptx = algod_client.pending_transaction_info(txid)
        asset_id = ptx["asset-index"]
        print_created_asset(algod_client, accounts[1]['pk'], asset_id)
        print_asset_holding(algod_client, accounts[1]['pk'], asset_id)
    except Exception as e:
        print(e)


def delete_non_fungible_token(accounts, algod_client, params, asset_id):
    print("--------------------------------------------")
    print("You have successfully created your own Non-fungible token! For the purpose of the demo, we will now delete the asset.")
    print("Deleting Asset...")

    # Asset destroy transaction
    txn = AssetConfigTxn(
        sender=accounts[1]['pk'],
        sp=params,
        index=asset_id,
        strict_empty_address_check=False
    )

    # Sign with secret key of creator
    stxn = txn.sign(accounts[1]['sk'])
    # Send the transaction to the network and retrieve the txid.
    txid = algod_client.send_transaction(stxn)
    print("Asset Destroy Transaction ID: {}".format(txid))

    # Wait for the transaction to be confirmed
    confirmed_txn = wait_for_confirmation(algod_client, txid, 4)
    print("TXID: ", txid)
    print("Result confirmed in round: {}".format(
        confirmed_txn['confirmed-round']))
    # Asset was deleted.
    try:
        print_asset_holding(algod_client, accounts[1]['pk'], asset_id)
        print_created_asset(algod_client, accounts[1]['pk'], asset_id)
        print("Asset is deleted.")
    except Exception as e:
        print(e)


def transfer_non_fungible_token(algod_client, sender, recipient, asset_id):
    # TRANSFER ASSET
    # transfer asset of 10 from account 1 to account 3
    params = algod_client.suggested_params()
    # comment these two lines if you want to use suggested params
    # params.fee = 1000
    # params.flat_fee = True
    txn = AssetTransferTxn(
        sender=sender['pk'],
        sp=params,
        receiver=recipient["pk"],
        amt=1,
        index=asset_id)
    stxn = txn.sign(sender['sk'])
    # Send the transaction to the network and retrieve the txid.
    try:
        txid = algod_client.send_transaction(stxn)
        print("Signed transaction with txID: {}".format(txid))
        # Wait for the transaction to be confirmed
        confirmed_txn = wait_for_confirmation(algod_client, txid, 4)
        print("TXID: ", txid)
        print("Result confirmed in round: {}".format(
            confirmed_txn['confirmed-round']))
    except Exception as err:
        print(err)
    # The balance should now be 10.
    print_asset_holding(algod_client, recipient['pk'], asset_id)


# this is tha account that has opted in...
r = "detect say border huge core electric perfect diagram industry kiss quit film cattle coast arrow sphere earth destroy perfect prefer evidence dice color ability moral"
accounts[3] = {}
accounts[3]['pk'] = mnemonic.to_public_key(r)
accounts[3]['sk'] = mnemonic.to_private_key(r)

create_non_fungible_token()
# transfer_non_fungible_token(algod_client, accounts[1], accounts[3], 2)
