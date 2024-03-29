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
import datetime

import cryptoapis
from cryptoapis.models.address_coins_transaction_unconfirmed_data import AddressCoinsTransactionUnconfirmedData  # noqa: E501
from cryptoapis.rest import ApiException

class TestAddressCoinsTransactionUnconfirmedData(unittest.TestCase):
    """AddressCoinsTransactionUnconfirmedData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AddressCoinsTransactionUnconfirmedData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AddressCoinsTransactionUnconfirmedData`
        """
        model = cryptoapis.models.address_coins_transaction_unconfirmed_data.AddressCoinsTransactionUnconfirmedData()  # noqa: E501
        if include_optional :
            return AddressCoinsTransactionUnconfirmedData(
                product = 'BLOCKCHAIN_EVENTS', 
                event = 'ADDRESS_COINS_TRANSACTION_UNCONFIRMED', 
                item = cryptoapis.models.address_coins_transaction_unconfirmed_data_item.AddressCoinsTransactionUnconfirmed_data_item(
                    blockchain = 'bitcoin', 
                    network = 'testnet', 
                    address = '3CzKAnCXt7ePb5NCp5qrAEimrxjY81oLoT', 
                    transaction_id = '4b2159770f75a7200ea168eb56ebbf3303b025d838f743fb6e785bc32d5ac65b', 
                    amount = '0.6508984', 
                    unit = 'BTC', 
                    direction = 'incoming', 
                    first_seen_in_mempool_timestamp = 1610365615, )
            )
        else :
            return AddressCoinsTransactionUnconfirmedData(
                product = 'BLOCKCHAIN_EVENTS',
                event = 'ADDRESS_COINS_TRANSACTION_UNCONFIRMED',
                item = cryptoapis.models.address_coins_transaction_unconfirmed_data_item.AddressCoinsTransactionUnconfirmed_data_item(
                    blockchain = 'bitcoin', 
                    network = 'testnet', 
                    address = '3CzKAnCXt7ePb5NCp5qrAEimrxjY81oLoT', 
                    transaction_id = '4b2159770f75a7200ea168eb56ebbf3303b025d838f743fb6e785bc32d5ac65b', 
                    amount = '0.6508984', 
                    unit = 'BTC', 
                    direction = 'incoming', 
                    first_seen_in_mempool_timestamp = 1610365615, ),
        )
        """

    def testAddressCoinsTransactionUnconfirmedData(self):
        """Test AddressCoinsTransactionUnconfirmedData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
