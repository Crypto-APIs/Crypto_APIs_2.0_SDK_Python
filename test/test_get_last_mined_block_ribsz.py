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
from cryptoapis.models.get_last_mined_block_ribsz import GetLastMinedBlockRIBSZ  # noqa: E501
from cryptoapis.rest import ApiException

class TestGetLastMinedBlockRIBSZ(unittest.TestCase):
    """GetLastMinedBlockRIBSZ unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetLastMinedBlockRIBSZ
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetLastMinedBlockRIBSZ`
        """
        model = cryptoapis.models.get_last_mined_block_ribsz.GetLastMinedBlockRIBSZ()  # noqa: E501
        if include_optional :
            return GetLastMinedBlockRIBSZ(
                bits = '524517883', 
                chainwork = '000000000000000000000000000000000000000000000000000000262b072797', 
                difficulty = '', 
                merkle_root = '961113ae943a3abf76da307cf881c4c6b6c13efb27fb67f02c9cdb46029848e8', 
                nonce = '2113101077', 
                size = 1408113, 
                version = 4
            )
        else :
            return GetLastMinedBlockRIBSZ(
                bits = '524517883',
                chainwork = '000000000000000000000000000000000000000000000000000000262b072797',
                merkle_root = '961113ae943a3abf76da307cf881c4c6b6c13efb27fb67f02c9cdb46029848e8',
                nonce = '2113101077',
                size = 1408113,
                version = 4,
        )
        """

    def testGetLastMinedBlockRIBSZ(self):
        """Test GetLastMinedBlockRIBSZ"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
