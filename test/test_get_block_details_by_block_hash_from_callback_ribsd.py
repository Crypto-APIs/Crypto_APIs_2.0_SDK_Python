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
from cryptoapis.models.get_block_details_by_block_hash_from_callback_ribsd import GetBlockDetailsByBlockHashFromCallbackRIBSD  # noqa: E501
from cryptoapis.rest import ApiException

class TestGetBlockDetailsByBlockHashFromCallbackRIBSD(unittest.TestCase):
    """GetBlockDetailsByBlockHashFromCallbackRIBSD unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetBlockDetailsByBlockHashFromCallbackRIBSD
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetBlockDetailsByBlockHashFromCallbackRIBSD`
        """
        model = cryptoapis.models.get_block_details_by_block_hash_from_callback_ribsd.GetBlockDetailsByBlockHashFromCallbackRIBSD()  # noqa: E501
        if include_optional :
            return GetBlockDetailsByBlockHashFromCallbackRIBSD(
                bits = '421808151', 
                chainwork = '0000000000000000000000000000000000000000000065cbab6e72cb49a0c2f7', 
                difficulty = '118376853.4818659', 
                merkle_root = '1cee8c0df02427cbcfd2d2a88678848b4c08eb89d580df34a52464a6fed4df7f', 
                nonce = 3850564744, 
                size = 26171, 
                version = 536870912, 
                version_hex = '20000000'
            )
        else :
            return GetBlockDetailsByBlockHashFromCallbackRIBSD(
                bits = '421808151',
                chainwork = '0000000000000000000000000000000000000000000065cbab6e72cb49a0c2f7',
                difficulty = '118376853.4818659',
                merkle_root = '1cee8c0df02427cbcfd2d2a88678848b4c08eb89d580df34a52464a6fed4df7f',
                nonce = 3850564744,
                size = 26171,
                version = 536870912,
                version_hex = '20000000',
        )
        """

    def testGetBlockDetailsByBlockHashFromCallbackRIBSD(self):
        """Test GetBlockDetailsByBlockHashFromCallbackRIBSD"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
