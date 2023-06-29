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
from cryptoapis.models.get_block_details_by_block_hash_from_callback_ribsl import GetBlockDetailsByBlockHashFromCallbackRIBSL  # noqa: E501
from cryptoapis.rest import ApiException

class TestGetBlockDetailsByBlockHashFromCallbackRIBSL(unittest.TestCase):
    """GetBlockDetailsByBlockHashFromCallbackRIBSL unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetBlockDetailsByBlockHashFromCallbackRIBSL
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetBlockDetailsByBlockHashFromCallbackRIBSL`
        """
        model = cryptoapis.models.get_block_details_by_block_hash_from_callback_ribsl.GetBlockDetailsByBlockHashFromCallbackRIBSL()  # noqa: E501
        if include_optional :
            return GetBlockDetailsByBlockHashFromCallbackRIBSL(
                bits = '436301753', 
                chainwork = '0000000000000000000000000000000000000000000006c61f0fce4b57f08ff4', 
                difficulty = '11679731.14248383', 
                merkle_root = '0ea8cea078d2338ce92e62d3275c92682d0a1879ddf861a7ce16889a24deccd2', 
                nonce = 3021194134, 
                size = 300998, 
                strippedsize = 220208, 
                version = 536870916, 
                version_hex = '20000004', 
                weight = 961622
            )
        else :
            return GetBlockDetailsByBlockHashFromCallbackRIBSL(
                bits = '436301753',
                chainwork = '0000000000000000000000000000000000000000000006c61f0fce4b57f08ff4',
                difficulty = '11679731.14248383',
                merkle_root = '0ea8cea078d2338ce92e62d3275c92682d0a1879ddf861a7ce16889a24deccd2',
                nonce = 3021194134,
                size = 300998,
                strippedsize = 220208,
                version = 536870916,
                version_hex = '20000004',
                weight = 961622,
        )
        """

    def testGetBlockDetailsByBlockHashFromCallbackRIBSL(self):
        """Test GetBlockDetailsByBlockHashFromCallbackRIBSL"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
