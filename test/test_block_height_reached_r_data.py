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
from cryptoapis.models.block_height_reached_r_data import BlockHeightReachedRData  # noqa: E501
from cryptoapis.rest import ApiException

class TestBlockHeightReachedRData(unittest.TestCase):
    """BlockHeightReachedRData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test BlockHeightReachedRData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BlockHeightReachedRData`
        """
        model = cryptoapis.models.block_height_reached_r_data.BlockHeightReachedRData()  # noqa: E501
        if include_optional :
            return BlockHeightReachedRData(
                item = cryptoapis.models.block_height_reached_ri.BlockHeightReachedRI(
                    block_height_reached = 667900, 
                    callback_secret_key = 'yourSecretKey', 
                    callback_url = 'https://example.com', 
                    created_timestamp = 1611238648, 
                    is_active = True, 
                    reference_id = 'bc243c86-0902-4386-b30d-e6b30fa1f2aa', )
            )
        else :
            return BlockHeightReachedRData(
                item = cryptoapis.models.block_height_reached_ri.BlockHeightReachedRI(
                    block_height_reached = 667900, 
                    callback_secret_key = 'yourSecretKey', 
                    callback_url = 'https://example.com', 
                    created_timestamp = 1611238648, 
                    is_active = True, 
                    reference_id = 'bc243c86-0902-4386-b30d-e6b30fa1f2aa', ),
        )
        """

    def testBlockHeightReachedRData(self):
        """Test BlockHeightReachedRData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
