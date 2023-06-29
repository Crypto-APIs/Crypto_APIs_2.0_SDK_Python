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
from cryptoapis.models.new_confirmed_coins_transactions_rb_data_item import NewConfirmedCoinsTransactionsRBDataItem  # noqa: E501
from cryptoapis.rest import ApiException

class TestNewConfirmedCoinsTransactionsRBDataItem(unittest.TestCase):
    """NewConfirmedCoinsTransactionsRBDataItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test NewConfirmedCoinsTransactionsRBDataItem
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NewConfirmedCoinsTransactionsRBDataItem`
        """
        model = cryptoapis.models.new_confirmed_coins_transactions_rb_data_item.NewConfirmedCoinsTransactionsRBDataItem()  # noqa: E501
        if include_optional :
            return NewConfirmedCoinsTransactionsRBDataItem(
                address = 'mho4jHBcrNCncKt38trJahXakuaBnS7LK5', 
                allow_duplicates = True, 
                callback_secret_key = 'yourSecretKey', 
                callback_url = 'https://example.com', 
                receive_callback_on = 3
            )
        else :
            return NewConfirmedCoinsTransactionsRBDataItem(
                address = 'mho4jHBcrNCncKt38trJahXakuaBnS7LK5',
                callback_url = 'https://example.com',
        )
        """

    def testNewConfirmedCoinsTransactionsRBDataItem(self):
        """Test NewConfirmedCoinsTransactionsRBDataItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
