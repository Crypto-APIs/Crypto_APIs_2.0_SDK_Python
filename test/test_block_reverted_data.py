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
from cryptoapis.models.block_reverted_data import BlockRevertedData  # noqa: E501
from cryptoapis.rest import ApiException

class TestBlockRevertedData(unittest.TestCase):
    """BlockRevertedData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test BlockRevertedData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BlockRevertedData`
        """
        model = cryptoapis.models.block_reverted_data.BlockRevertedData()  # noqa: E501
        if include_optional :
            return BlockRevertedData(
                product = 'BLOCKCHAIN_EVENTS', 
                event = 'BLOCK_REVERTED', 
                item = cryptoapis.models.block_reverted_data_item.BlockReverted_data_item(
                    blockchain = 'bitcoin', 
                    network = 'testnet', 
                    height = 570008, 
                    hash = '00000000000000000006ddb5e854505f8b792122b0ac9469c07eb26db414f6fb', 
                    timestamp = 1610365615, )
            )
        else :
            return BlockRevertedData(
                product = 'BLOCKCHAIN_EVENTS',
                event = 'BLOCK_REVERTED',
                item = cryptoapis.models.block_reverted_data_item.BlockReverted_data_item(
                    blockchain = 'bitcoin', 
                    network = 'testnet', 
                    height = 570008, 
                    hash = '00000000000000000006ddb5e854505f8b792122b0ac9469c07eb26db414f6fb', 
                    timestamp = 1610365615, ),
        )
        """

    def testBlockRevertedData(self):
        """Test BlockRevertedData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
