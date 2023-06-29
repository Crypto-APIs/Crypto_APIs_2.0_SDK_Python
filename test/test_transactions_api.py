# coding: utf-8

"""
    CryptoAPIs

    Crypto APIs is a complex and innovative infrastructure layer that radically simplifies the development of any Blockchain and Crypto related applications. Organized around REST, Crypto APIs can assist both novice Bitcoin/Ethereum enthusiasts and crypto experts with the development of their blockchain applications. Crypto APIs provides unified endpoints and data, raw data, automatic tokens and coins forwardings, callback functionalities, and much more.  # noqa: E501

    The version of the OpenAPI document: 2021-03-20
    Contact: developers@cryptoapis.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest

import cryptoapis
from cryptoapis.api.transactions_api import TransactionsApi  # noqa: E501
from cryptoapis.rest import ApiException


class TestTransactionsApi(unittest.TestCase):
    """TransactionsApi unit test stubs"""

    def setUp(self):
        self.api = cryptoapis.api.transactions_api.TransactionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_coins_transaction_from_address_for_whole_amount(self):
        """Test case for create_coins_transaction_from_address_for_whole_amount

        Create Coins Transaction From Address For Whole Amount  # noqa: E501
        """
        pass

    def test_create_coins_transaction_request_from_address(self):
        """Test case for create_coins_transaction_request_from_address

        Create Coins Transaction Request from Address  # noqa: E501
        """
        pass

    def test_create_coins_transaction_request_from_wallet(self):
        """Test case for create_coins_transaction_request_from_wallet

        Create Coins Transaction Request from Wallet  # noqa: E501
        """
        pass

    def test_create_fungible_token_transaction_request_from_address_without_fee_priority(self):
        """Test case for create_fungible_token_transaction_request_from_address_without_fee_priority

        Create Fungible Token Transaction Request From Address Without Fee Priority  # noqa: E501
        """
        pass

    def test_create_fungible_tokens_transaction_request_from_address(self):
        """Test case for create_fungible_tokens_transaction_request_from_address

        Create Fungible Tokens Transaction Request from Address  # noqa: E501
        """
        pass

    def test_create_single_transaction_request_from_address_without_fee_priority(self):
        """Test case for create_single_transaction_request_from_address_without_fee_priority

        Create Single Transaction Request From Address Without Fee Priority  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
