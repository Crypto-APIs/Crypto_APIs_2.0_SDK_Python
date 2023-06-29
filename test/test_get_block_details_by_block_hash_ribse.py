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
from cryptoapis.models.get_block_details_by_block_hash_ribse import GetBlockDetailsByBlockHashRIBSE  # noqa: E501
from cryptoapis.rest import ApiException

class TestGetBlockDetailsByBlockHashRIBSE(unittest.TestCase):
    """GetBlockDetailsByBlockHashRIBSE unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetBlockDetailsByBlockHashRIBSE
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetBlockDetailsByBlockHashRIBSE`
        """
        model = cryptoapis.models.get_block_details_by_block_hash_ribse.GetBlockDetailsByBlockHashRIBSE()  # noqa: E501
        if include_optional :
            return GetBlockDetailsByBlockHashRIBSE(
                difficulty = '209515044.4071968', 
                extra_data = '0xd983010203844765746887676f312e342e328777696e646f7773', 
                gas_limit = '7999992', 
                gas_used = '21000', 
                mined_in_seconds = 12, 
                nonce = '1535290446', 
                sha3_uncles = '0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347', 
                size = 3892, 
                total_difficulty = '1088214928417257646845', 
                uncles = [
                    '0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347'
                    ]
            )
        else :
            return GetBlockDetailsByBlockHashRIBSE(
                difficulty = '209515044.4071968',
                extra_data = '0xd983010203844765746887676f312e342e328777696e646f7773',
                gas_limit = '7999992',
                gas_used = '21000',
                mined_in_seconds = 12,
                nonce = '1535290446',
                sha3_uncles = '0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347',
                size = 3892,
                total_difficulty = '1088214928417257646845',
                uncles = [
                    '0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347'
                    ],
        )
        """

    def testGetBlockDetailsByBlockHashRIBSE(self):
        """Test GetBlockDetailsByBlockHashRIBSE"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
