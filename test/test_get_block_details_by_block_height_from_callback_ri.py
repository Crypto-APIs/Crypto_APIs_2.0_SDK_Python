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
from cryptoapis.models.get_block_details_by_block_height_from_callback_ri import GetBlockDetailsByBlockHeightFromCallbackRI  # noqa: E501
from cryptoapis.rest import ApiException

class TestGetBlockDetailsByBlockHeightFromCallbackRI(unittest.TestCase):
    """GetBlockDetailsByBlockHeightFromCallbackRI unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetBlockDetailsByBlockHeightFromCallbackRI
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetBlockDetailsByBlockHeightFromCallbackRI`
        """
        model = cryptoapis.models.get_block_details_by_block_height_from_callback_ri.GetBlockDetailsByBlockHeightFromCallbackRI()  # noqa: E501
        if include_optional :
            return GetBlockDetailsByBlockHeightFromCallbackRI(
                hash = '00000000000000000002ad6f9c74faf503bb055c54e0d0746ef34f888f95890f', 
                height = 673852, 
                previous_block_hash = '00000000000000000008953625613e60b56194ea31f07aad43c7505fbddce77f', 
                timestamp = 1610365615, 
                transactions_count = 2755, 
                blockchain_specific = cryptoapis.models.get_block_details_by_block_height_from_callback_ribs.GetBlockDetailsByBlockHeightFromCallbackRIBS()
            )
        else :
            return GetBlockDetailsByBlockHeightFromCallbackRI(
                hash = '00000000000000000002ad6f9c74faf503bb055c54e0d0746ef34f888f95890f',
                height = 673852,
                previous_block_hash = '00000000000000000008953625613e60b56194ea31f07aad43c7505fbddce77f',
                timestamp = 1610365615,
                transactions_count = 2755,
                blockchain_specific = cryptoapis.models.get_block_details_by_block_height_from_callback_ribs.GetBlockDetailsByBlockHeightFromCallbackRIBS(),
        )
        """

    def testGetBlockDetailsByBlockHeightFromCallbackRI(self):
        """Test GetBlockDetailsByBlockHeightFromCallbackRI"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
