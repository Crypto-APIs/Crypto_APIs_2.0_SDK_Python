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
from cryptoapis.models.get_block_details_by_block_hash_ribsl import GetBlockDetailsByBlockHashRIBSL  # noqa: E501
from cryptoapis.rest import ApiException

class TestGetBlockDetailsByBlockHashRIBSL(unittest.TestCase):
    """GetBlockDetailsByBlockHashRIBSL unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetBlockDetailsByBlockHashRIBSL
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetBlockDetailsByBlockHashRIBSL`
        """
        model = cryptoapis.models.get_block_details_by_block_hash_ribsl.GetBlockDetailsByBlockHashRIBSL()  # noqa: E501
        if include_optional :
            return GetBlockDetailsByBlockHashRIBSL(
                difficulty = '209515044.4071968', 
                bits = '191670a9', 
                chainwork = '000000000000000000000000000000000000000000004f7606f3d619a200dc2d', 
                merkle_root = '95439d11e918c9fd9a901dcf22203d60f538d660ae74efb7cb566825420fd3b7', 
                nonce = '1535290446', 
                size = 3892, 
                stripped_size = 895429, 
                version = 536870912, 
                version_hex = '20000000', 
                weight = 37248
            )
        else :
            return GetBlockDetailsByBlockHashRIBSL(
                difficulty = '209515044.4071968',
                bits = '191670a9',
                chainwork = '000000000000000000000000000000000000000000004f7606f3d619a200dc2d',
                merkle_root = '95439d11e918c9fd9a901dcf22203d60f538d660ae74efb7cb566825420fd3b7',
                nonce = '1535290446',
                size = 3892,
                stripped_size = 895429,
                version = 536870912,
                version_hex = '20000000',
                weight = 37248,
        )
        """

    def testGetBlockDetailsByBlockHashRIBSL(self):
        """Test GetBlockDetailsByBlockHashRIBSL"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
