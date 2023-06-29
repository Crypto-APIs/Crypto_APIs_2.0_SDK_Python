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
from cryptoapis.models.address_coins_transaction_confirmed_each_confirmation_data import AddressCoinsTransactionConfirmedEachConfirmationData  # noqa: E501
from cryptoapis.rest import ApiException

class TestAddressCoinsTransactionConfirmedEachConfirmationData(unittest.TestCase):
    """AddressCoinsTransactionConfirmedEachConfirmationData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AddressCoinsTransactionConfirmedEachConfirmationData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AddressCoinsTransactionConfirmedEachConfirmationData`
        """
        model = cryptoapis.models.address_coins_transaction_confirmed_each_confirmation_data.AddressCoinsTransactionConfirmedEachConfirmationData()  # noqa: E501
        if include_optional :
            return AddressCoinsTransactionConfirmedEachConfirmationData(
                product = 'BLOCKCHAIN_EVENTS', 
                event = 'ADDRESS_COINS_TRANSACTION_CONFIRMED_EACH_CONFIRMATION', 
                item = cryptoapis.models.address_coins_transaction_confirmed_each_confirmation_data_item.AddressCoinsTransactionConfirmedEachConfirmation_data_item(
                    blockchain = 'bitcoin', 
                    network = 'testnet', 
                    address = '15282N4BYEwYh3j1dTgJu64Ey5qWn9Po9F', 
                    mined_in_block = cryptoapis.models.address_coins_transaction_confirmed_each_confirmation_data_item_mined_in_block.AddressCoinsTransactionConfirmedEachConfirmation_data_item_minedInBlock(
                        height = 667754, 
                        hash = 'dfe45f6724b550c281107ffaa5880cb280878fb4dbaa742aa21449f3d2340c13', 
                        timestamp = 1610365314, ), 
                    transaction_id = 'cbd3dea703bd2bc78bca69ee61ca14e6ffcdd809d07ebbc3b8fea3c30ea38f33', 
                    current_confirmations = 8, 
                    target_confirmations = 12, 
                    amount = '0.0611', 
                    unit = 'BTC', 
                    direction = 'incoming', )
            )
        else :
            return AddressCoinsTransactionConfirmedEachConfirmationData(
                product = 'BLOCKCHAIN_EVENTS',
                event = 'ADDRESS_COINS_TRANSACTION_CONFIRMED_EACH_CONFIRMATION',
                item = cryptoapis.models.address_coins_transaction_confirmed_each_confirmation_data_item.AddressCoinsTransactionConfirmedEachConfirmation_data_item(
                    blockchain = 'bitcoin', 
                    network = 'testnet', 
                    address = '15282N4BYEwYh3j1dTgJu64Ey5qWn9Po9F', 
                    mined_in_block = cryptoapis.models.address_coins_transaction_confirmed_each_confirmation_data_item_mined_in_block.AddressCoinsTransactionConfirmedEachConfirmation_data_item_minedInBlock(
                        height = 667754, 
                        hash = 'dfe45f6724b550c281107ffaa5880cb280878fb4dbaa742aa21449f3d2340c13', 
                        timestamp = 1610365314, ), 
                    transaction_id = 'cbd3dea703bd2bc78bca69ee61ca14e6ffcdd809d07ebbc3b8fea3c30ea38f33', 
                    current_confirmations = 8, 
                    target_confirmations = 12, 
                    amount = '0.0611', 
                    unit = 'BTC', 
                    direction = 'incoming', ),
        )
        """

    def testAddressCoinsTransactionConfirmedEachConfirmationData(self):
        """Test AddressCoinsTransactionConfirmedEachConfirmationData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
