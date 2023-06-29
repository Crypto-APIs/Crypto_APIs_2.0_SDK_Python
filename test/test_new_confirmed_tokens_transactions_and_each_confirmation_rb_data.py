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
from cryptoapis.models.new_confirmed_tokens_transactions_and_each_confirmation_rb_data import NewConfirmedTokensTransactionsAndEachConfirmationRBData  # noqa: E501
from cryptoapis.rest import ApiException

class TestNewConfirmedTokensTransactionsAndEachConfirmationRBData(unittest.TestCase):
    """NewConfirmedTokensTransactionsAndEachConfirmationRBData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test NewConfirmedTokensTransactionsAndEachConfirmationRBData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NewConfirmedTokensTransactionsAndEachConfirmationRBData`
        """
        model = cryptoapis.models.new_confirmed_tokens_transactions_and_each_confirmation_rb_data.NewConfirmedTokensTransactionsAndEachConfirmationRBData()  # noqa: E501
        if include_optional :
            return NewConfirmedTokensTransactionsAndEachConfirmationRBData(
                item = cryptoapis.models.new_confirmed_tokens_transactions_and_each_confirmation_rb_data_item.NewConfirmedTokensTransactionsAndEachConfirmationRB_data_item(
                    address = '0x033ef6db9fbd0ee60e2931906b987fe0280471a0', 
                    allow_duplicates = True, 
                    callback_secret_key = 'yourSecretKey', 
                    callback_url = 'https://example.com', 
                    confirmations_count = 3, )
            )
        else :
            return NewConfirmedTokensTransactionsAndEachConfirmationRBData(
                item = cryptoapis.models.new_confirmed_tokens_transactions_and_each_confirmation_rb_data_item.NewConfirmedTokensTransactionsAndEachConfirmationRB_data_item(
                    address = '0x033ef6db9fbd0ee60e2931906b987fe0280471a0', 
                    allow_duplicates = True, 
                    callback_secret_key = 'yourSecretKey', 
                    callback_url = 'https://example.com', 
                    confirmations_count = 3, ),
        )
        """

    def testNewConfirmedTokensTransactionsAndEachConfirmationRBData(self):
        """Test NewConfirmedTokensTransactionsAndEachConfirmationRBData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
