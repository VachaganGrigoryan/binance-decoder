from binance_decoder import binance_decoder
import json


def test_decoder_for_big_hash():
    from inputs import big_encoded_tx
    str_txn = binance_decoder(big_encoded_tx)
    assert str_txn
    assert isinstance(str_txn, str)
    transaction = json.loads(str_txn)

    assert transaction['hash'] == '4be704b2436c8df0bfb41fd51965b90eab909fbfb9a1deb9b1defd0cacd3a66b'


def test_decoder_for_bunch_of_txs():
    from inputs import encoded_txs
    for encoded_tx in encoded_txs:
        str_txn = binance_decoder(encoded_tx)
        assert str_txn
        assert isinstance(str_txn, str)
        transaction = json.loads(str_txn)
        assert transaction['hash']


if __name__ == '__main__':
    test_decoder_for_big_hash()
    test_decoder_for_bunch_of_txs()
