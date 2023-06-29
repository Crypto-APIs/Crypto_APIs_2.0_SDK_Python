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
from cryptoapis.models.address_tokens_transaction_confirmed_data_item_mined_in_block import AddressTokensTransactionConfirmedDataItemMinedInBlock  # noqa: E501
from cryptoapis.rest import ApiException

class TestAddressTokensTransactionConfirmedDataItemMinedInBlock(unittest.TestCase):
    """AddressTokensTransactionConfirmedDataItemMinedInBlock unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AddressTokensTransactionConfirmedDataItemMinedInBlock
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AddressTokensTransactionConfirmedDataItemMinedInBlock`
        """
        model = cryptoapis.models.address_tokens_transaction_confirmed_data_item_mined_in_block.AddressTokensTransactionConfirmedDataItemMinedInBlock()  # noqa: E501
        if include_optional :
            return AddressTokensTransactionConfirmedDataItemMinedInBlock(
                height = 657915, 
                hash = '269b0de44db95beddb6aecc520b375ba8f91f3dc5558a24aa4c26979eb00c7e2', 
                timestamp = 1586365500
            )
        else :
            return AddressTokensTransactionConfirmedDataItemMinedInBlock(
                height = 657915,
                hash = '269b0de44db95beddb6aecc520b375ba8f91f3dc5558a24aa4c26979eb00c7e2',
                timestamp = 1586365500,
        )
        """

    def testAddressTokensTransactionConfirmedDataItemMinedInBlock(self):
        """Test AddressTokensTransactionConfirmedDataItemMinedInBlock"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
