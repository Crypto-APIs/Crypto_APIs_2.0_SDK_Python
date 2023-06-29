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
from cryptoapis.models.address_tokens_transaction_confirmed_each_confirmation_data_item import AddressTokensTransactionConfirmedEachConfirmationDataItem  # noqa: E501
from cryptoapis.rest import ApiException

class TestAddressTokensTransactionConfirmedEachConfirmationDataItem(unittest.TestCase):
    """AddressTokensTransactionConfirmedEachConfirmationDataItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AddressTokensTransactionConfirmedEachConfirmationDataItem
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AddressTokensTransactionConfirmedEachConfirmationDataItem`
        """
        model = cryptoapis.models.address_tokens_transaction_confirmed_each_confirmation_data_item.AddressTokensTransactionConfirmedEachConfirmationDataItem()  # noqa: E501
        if include_optional :
            return AddressTokensTransactionConfirmedEachConfirmationDataItem(
                blockchain = 'ethereum', 
                network = 'goerli', 
                address = '0x7495fede000c8a3b77eeae09cf70fa94cd2d53f5', 
                mined_in_block = cryptoapis.models.address_tokens_transaction_confirmed_data_item_mined_in_block.AddressTokensTransactionConfirmed_data_item_minedInBlock(
                    height = 657915, 
                    hash = '269b0de44db95beddb6aecc520b375ba8f91f3dc5558a24aa4c26979eb00c7e2', 
                    timestamp = 1586365500, ), 
                transaction_id = '0xbe38781783b1b9d480219255ff98e20335a39e13979a66112efa33f05fde0a33', 
                current_confirmations = 2, 
                target_confirmations = 3, 
                token_type = 'ERC-20', 
                token = cryptoapis.models.address_tokens_transaction_confirmed_each_confirmation_token.AddressTokensTransactionConfirmedEachConfirmationToken(), 
                direction = 'incoming'
            )
        else :
            return AddressTokensTransactionConfirmedEachConfirmationDataItem(
                blockchain = 'ethereum',
                network = 'goerli',
                address = '0x7495fede000c8a3b77eeae09cf70fa94cd2d53f5',
                mined_in_block = cryptoapis.models.address_tokens_transaction_confirmed_data_item_mined_in_block.AddressTokensTransactionConfirmed_data_item_minedInBlock(
                    height = 657915, 
                    hash = '269b0de44db95beddb6aecc520b375ba8f91f3dc5558a24aa4c26979eb00c7e2', 
                    timestamp = 1586365500, ),
                transaction_id = '0xbe38781783b1b9d480219255ff98e20335a39e13979a66112efa33f05fde0a33',
                current_confirmations = 2,
                target_confirmations = 3,
                token_type = 'ERC-20',
                token = cryptoapis.models.address_tokens_transaction_confirmed_each_confirmation_token.AddressTokensTransactionConfirmedEachConfirmationToken(),
                direction = 'incoming',
        )
        """

    def testAddressTokensTransactionConfirmedEachConfirmationDataItem(self):
        """Test AddressTokensTransactionConfirmedEachConfirmationDataItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
