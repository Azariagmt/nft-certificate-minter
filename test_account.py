import pytest

#
from algosdk.v2client import algod

#
from initial_transaction import transaction_function


def test_transaction_function():
    """
    Account 1 (246712931):
    My address: FVG763EJQCT74WRYMEDKDJDGY24YXSMM27RX2ICTE2DKVZ35Z7Z6HY7TRE
    My private key: Sqt3Lokcyc0omgLHTTOa2nk9G02a5JOP0dWgNKB4TDktTf9siYCn/lo4YQahpGbGuYvJjNfjfSBTJoaq533P8w==
    My passphrase: harsh team now silk mutual cricket spend action rib snake escape oval kit egg sponsor tonight venue economy helmet energy document bullet skill ability claw

    Account 2 (0.2):
        My address: 5JMAXYRBMLOADUSFQOIY5DCJP2BX3C7AWBTTD7Y2VHBSCLSWGQJIJI6HI4
        My private key: ZmF1LjdHUW8YMUElxD7uMi+Gx2OcBMGqBlbzaHydf9jqWAviIWLcAdJFg5GOjEl+g32L4LBnMf8aqcMhLlY0Eg==
        My passphrase: coast stereo now inflict penalty bridge match donkey lucky wild jacket veteran arrange vehicle toast afraid flag boy prison monkey web trap sentence absorb what

    """

    algod_address = "http://localhost:4001"
    algod_token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    algod_client = algod.AlgodClient(algod_token, algod_address)

    senders_address = "FVG763EJQCT74WRYMEDKDJDGY24YXSMM27RX2ICTE2DKVZ35Z7Z6HY7TRE"
    rec_address = "5JMAXYRBMLOADUSFQOIY5DCJP2BX3C7AWBTTD7Y2VHBSCLSWGQJIJI6HI4"

    init_senders_balance = algod_client.account_info(
        senders_address).get('amount')
    init_rec_balance = algod_client.account_info(rec_address).get('amount')

    transaction_function(
        algod_client=algod_client,
        private_key="Sqt3Lokcyc0omgLHTTOa2nk9G02a5JOP0dWgNKB4TDktTf9siYCn/lo4YQahpGbGuYvJjNfjfSBTJoaq533P8w==",
        my_address=senders_address,
        rec_address=rec_address,
        amount_snd=1000000
    )

    final_senders_balance = algod_client.account_info(
        senders_address).get('amount')
    final_rec_balance = algod_client.account_info(rec_address).get('amount')

    assert (init_senders_balance +
            init_rec_balance) == (final_senders_balance+final_rec_balance + 1000)
