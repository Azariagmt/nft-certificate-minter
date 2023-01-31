import json
import base64

#
from algosdk.v2client import algod

#
from algosdk import transaction
from algosdk import constants


def transaction_function(algod_client, private_key, my_address, rec_address, amount_snd):
    # build transaction
    params = algod_client.suggested_params()
    # comment out the next two (2) lines to use suggested fees
    params.flat_fee = True
    params.fee = constants.MIN_TXN_FEE
    receiver = rec_address
    note = "Hello World".encode()
    amount = amount_snd
    unsigned_txn = transaction.PaymentTxn(
        my_address, params, receiver, amount, None, note)

    # sign transaction
    signed_txn = unsigned_txn.sign(private_key)

    # submit transaction
    txid = algod_client.send_transaction(signed_txn)
    print("Successfully sent transaction with txID: {}".format(txid))

    # wait for confirmation
    try:
        confirmed_txn = transaction.wait_for_confirmation(
            algod_client, txid, 4)
    except Exception as err:
        print(err)
        return

    print("Transaction information: {}".format(
        json.dumps(confirmed_txn, indent=4)))
    print("Decoded note: {}".format(base64.b64decode(
        confirmed_txn["txn"]["txn"]["note"]).decode()))
    # print("Starting Account balance: {} microAlgos".format(account_info.get('amount')) )
    # print("Amount transfered: {} microAlgos".format(amount) )
    # print("Fee: {} microAlgos".format(params.fee) )

    # account_info = algod_client.account_info(my_address)
    # print("Final Account balance: {} microAlgos".format(account_info.get('amount')) + "\n")


def get_balance(algod_client, my_address):
    account_info = algod_client.account_info(my_address)
    print("Account balance: {} microAlgos".format(
        account_info.get('amount')) + "\n")
    return account_info.get('amount')


if __name__ == "__main__":
    algod_address = "http://localhost:4001"
    algod_token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    algod_client = algod.AlgodClient(algod_token, algod_address)

    # get_balance(algod_client=algod_client, my_address="FVG763EJQCT74WRYMEDKDJDGY24YXSMM27RX2ICTE2DKVZ35Z7Z6HY7TRE")

    # a -> 100
    # d -> 50
    # transfer (a->d | 10)
    # a -> 90
    # d -> 60

    transaction_function(algod_client=algod_client,
                         private_key="Sqt3Lokcyc0omgLHTTOa2nk9G02a5JOP0dWgNKB4TDktTf9siYCn/lo4YQahpGbGuYvJjNfjfSBTJoaq533P8w==",
                         my_address="FVG763EJQCT74WRYMEDKDJDGY24YXSMM27RX2ICTE2DKVZ35Z7Z6HY7TRE",
                         rec_address="5JMAXYRBMLOADUSFQOIY5DCJP2BX3C7AWBTTD7Y2VHBSCLSWGQJIJI6HI4",
                         amount_snd=100000
                         )
