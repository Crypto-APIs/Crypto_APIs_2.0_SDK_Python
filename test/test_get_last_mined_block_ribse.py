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
from cryptoapis.models.get_last_mined_block_ribse import GetLastMinedBlockRIBSE  # noqa: E501
from cryptoapis.rest import ApiException

class TestGetLastMinedBlockRIBSE(unittest.TestCase):
    """GetLastMinedBlockRIBSE unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetLastMinedBlockRIBSE
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetLastMinedBlockRIBSE`
        """
        model = cryptoapis.models.get_last_mined_block_ribse.GetLastMinedBlockRIBSE()  # noqa: E501
        if include_optional :
            return GetLastMinedBlockRIBSE(
                difficulty = '', 
                extra_data = '0x7070796520e4b883e5bda9e7a59ee4bb99e9b1bc080c', 
                gas_limit = '12499653', 
                gas_used = '12488144', 
                mined_in_seconds = 17, 
                nonce = '2113101077', 
                sha3_uncles = '0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347', 
                size = 1408113, 
                total_difficulty = '4794080996481072', 
                uncles = [
                    ''
                    ]
            )
        else :
            return GetLastMinedBlockRIBSE(
                extra_data = '0x7070796520e4b883e5bda9e7a59ee4bb99e9b1bc080c',
                gas_limit = '12499653',
                gas_used = '12488144',
                mined_in_seconds = 17,
                nonce = '2113101077',
                sha3_uncles = '0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347',
                size = 1408113,
                total_difficulty = '4794080996481072',
                uncles = [
                    ''
                    ],
        )
        """

    def testGetLastMinedBlockRIBSE(self):
        """Test GetLastMinedBlockRIBSE"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
