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
from cryptoapis.models.get_last_mined_block_ribsbc import GetLastMinedBlockRIBSBC  # noqa: E501
from cryptoapis.rest import ApiException

class TestGetLastMinedBlockRIBSBC(unittest.TestCase):
    """GetLastMinedBlockRIBSBC unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetLastMinedBlockRIBSBC
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetLastMinedBlockRIBSBC`
        """
        model = cryptoapis.models.get_last_mined_block_ribsbc.GetLastMinedBlockRIBSBC()  # noqa: E501
        if include_optional :
            return GetLastMinedBlockRIBSBC(
                bits = '1805839a', 
                chainwork = '0000000000000000000000000000000000000000015dc8754d8bfaedfffbb3bd', 
                difficulty = '', 
                merkle_root = '543872ba53c13183f951d76dd5933f98900a1bf9b3eef716857dfcc3c0534dfb', 
                nonce = '2113101077', 
                size = 1408113, 
                version = 545259520, 
                version_hex = '20000000'
            )
        else :
            return GetLastMinedBlockRIBSBC(
                bits = '1805839a',
                chainwork = '0000000000000000000000000000000000000000015dc8754d8bfaedfffbb3bd',
                merkle_root = '543872ba53c13183f951d76dd5933f98900a1bf9b3eef716857dfcc3c0534dfb',
                nonce = '2113101077',
                size = 1408113,
                version = 545259520,
                version_hex = '20000000',
        )
        """

    def testGetLastMinedBlockRIBSBC(self):
        """Test GetLastMinedBlockRIBSBC"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
