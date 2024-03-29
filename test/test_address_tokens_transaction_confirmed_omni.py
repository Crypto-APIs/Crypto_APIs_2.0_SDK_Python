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
from cryptoapis.models.address_tokens_transaction_confirmed_omni import AddressTokensTransactionConfirmedOmni  # noqa: E501
from cryptoapis.rest import ApiException

class TestAddressTokensTransactionConfirmedOmni(unittest.TestCase):
    """AddressTokensTransactionConfirmedOmni unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AddressTokensTransactionConfirmedOmni
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AddressTokensTransactionConfirmedOmni`
        """
        model = cryptoapis.models.address_tokens_transaction_confirmed_omni.AddressTokensTransactionConfirmedOmni()  # noqa: E501
        if include_optional :
            return AddressTokensTransactionConfirmedOmni(
                name = 'Tether-USDT', 
                property_id = '31', 
                transaction_type = 'Simple Send, DEx Purchase etc.', 
                created_by_transaction_id = 'be5be71feac9e7019fbcdea5a87098a7862a0ee8c60bd5809b4d3b0cda940ddc', 
                amount = '110.531723'
            )
        else :
            return AddressTokensTransactionConfirmedOmni(
                name = 'Tether-USDT',
                property_id = '31',
                transaction_type = 'Simple Send, DEx Purchase etc.',
                created_by_transaction_id = 'be5be71feac9e7019fbcdea5a87098a7862a0ee8c60bd5809b4d3b0cda940ddc',
                amount = '110.531723',
        )
        """

    def testAddressTokensTransactionConfirmedOmni(self):
        """Test AddressTokensTransactionConfirmedOmni"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
