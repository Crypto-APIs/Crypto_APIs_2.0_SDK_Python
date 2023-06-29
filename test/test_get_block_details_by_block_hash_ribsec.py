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
from cryptoapis.models.get_block_details_by_block_hash_ribsec import GetBlockDetailsByBlockHashRIBSEC  # noqa: E501
from cryptoapis.rest import ApiException

class TestGetBlockDetailsByBlockHashRIBSEC(unittest.TestCase):
    """GetBlockDetailsByBlockHashRIBSEC unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetBlockDetailsByBlockHashRIBSEC
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetBlockDetailsByBlockHashRIBSEC`
        """
        model = cryptoapis.models.get_block_details_by_block_hash_ribsec.GetBlockDetailsByBlockHashRIBSEC()  # noqa: E501
        if include_optional :
            return GetBlockDetailsByBlockHashRIBSEC(
                difficulty = '209515044.4071968', 
                extra_data = '0x307834383639373636353666366532303530366636663663', 
                gas_limit = '7999992', 
                gas_used = '21000', 
                mined_in_seconds = 12, 
                nonce = '1535290446', 
                sha3_uncles = '0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347', 
                size = 3892, 
                total_difficulty = '1088214928417257646845', 
                uncles = [
                    ''
                    ]
            )
        else :
            return GetBlockDetailsByBlockHashRIBSEC(
                difficulty = '209515044.4071968',
                extra_data = '0x307834383639373636353666366532303530366636663663',
                gas_limit = '7999992',
                gas_used = '21000',
                mined_in_seconds = 12,
                nonce = '1535290446',
                sha3_uncles = '0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347',
                size = 3892,
                total_difficulty = '1088214928417257646845',
                uncles = [
                    ''
                    ],
        )
        """

    def testGetBlockDetailsByBlockHashRIBSEC(self):
        """Test GetBlockDetailsByBlockHashRIBSEC"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
