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
from cryptoapis.models.list_wallet_transactions_ri_value import ListWalletTransactionsRIValue  # noqa: E501
from cryptoapis.rest import ApiException

class TestListWalletTransactionsRIValue(unittest.TestCase):
    """ListWalletTransactionsRIValue unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ListWalletTransactionsRIValue
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListWalletTransactionsRIValue`
        """
        model = cryptoapis.models.list_wallet_transactions_ri_value.ListWalletTransactionsRIValue()  # noqa: E501
        if include_optional :
            return ListWalletTransactionsRIValue(
                amount = '0.001', 
                converted_amount = '150', 
                exchange_rate_unit = 'USD', 
                symbol = 'ETH'
            )
        else :
            return ListWalletTransactionsRIValue(
                amount = '0.001',
                converted_amount = '150',
                exchange_rate_unit = 'USD',
                symbol = 'ETH',
        )
        """

    def testListWalletTransactionsRIValue(self):
        """Test ListWalletTransactionsRIValue"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
