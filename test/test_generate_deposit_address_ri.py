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
from cryptoapis.models.generate_deposit_address_ri import GenerateDepositAddressRI  # noqa: E501
from cryptoapis.rest import ApiException

class TestGenerateDepositAddressRI(unittest.TestCase):
    """GenerateDepositAddressRI unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GenerateDepositAddressRI
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GenerateDepositAddressRI`
        """
        model = cryptoapis.models.generate_deposit_address_ri.GenerateDepositAddressRI()  # noqa: E501
        if include_optional :
            return GenerateDepositAddressRI(
                address = '0xe2b5f5e885a268e4b6faae53f99a663f3bb3e036', 
                created_timestamp = 1624028267, 
                label = 'yourLabelStringHere'
            )
        else :
            return GenerateDepositAddressRI(
                address = '0xe2b5f5e885a268e4b6faae53f99a663f3bb3e036',
                created_timestamp = 1624028267,
                label = 'yourLabelStringHere',
        )
        """

    def testGenerateDepositAddressRI(self):
        """Test GenerateDepositAddressRI"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
