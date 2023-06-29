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
from cryptoapis.models.get_block_details_by_block_height_ribsbsc import GetBlockDetailsByBlockHeightRIBSBSC  # noqa: E501
from cryptoapis.rest import ApiException

class TestGetBlockDetailsByBlockHeightRIBSBSC(unittest.TestCase):
    """GetBlockDetailsByBlockHeightRIBSBSC unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetBlockDetailsByBlockHeightRIBSBSC
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetBlockDetailsByBlockHeightRIBSBSC`
        """
        model = cryptoapis.models.get_block_details_by_block_height_ribsbsc.GetBlockDetailsByBlockHeightRIBSBSC()  # noqa: E501
        if include_optional :
            return GetBlockDetailsByBlockHeightRIBSBSC(
                difficulty = '209515044.4071968', 
                extra_data = '0xd983010203844765746887676f312e342e328777696e646f7773', 
                gas_limit = '3141592', 
                gas_used = '21000', 
                mined_in_seconds = 5, 
                nonce = '1535290446', 
                sha3_uncles = '0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347', 
                size = 3892, 
                total_difficulty = '20104747399762079739558'
            )
        else :
            return GetBlockDetailsByBlockHeightRIBSBSC(
                difficulty = '209515044.4071968',
                extra_data = '0xd983010203844765746887676f312e342e328777696e646f7773',
                gas_limit = '3141592',
                gas_used = '21000',
                mined_in_seconds = 5,
                nonce = '1535290446',
                sha3_uncles = '0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347',
                size = 3892,
                total_difficulty = '20104747399762079739558',
        )
        """

    def testGetBlockDetailsByBlockHeightRIBSBSC(self):
        """Test GetBlockDetailsByBlockHeightRIBSBSC"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
