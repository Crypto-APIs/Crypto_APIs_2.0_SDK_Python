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
from cryptoapis.models.new_reverted_block_e400 import NewRevertedBlockE400  # noqa: E501
from cryptoapis.rest import ApiException

class TestNewRevertedBlockE400(unittest.TestCase):
    """NewRevertedBlockE400 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test NewRevertedBlockE400
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NewRevertedBlockE400`
        """
        model = cryptoapis.models.new_reverted_block_e400.NewRevertedBlockE400()  # noqa: E501
        if include_optional :
            return NewRevertedBlockE400(
                code = 'invalid_pagination', 
                message = 'The pagination attributes that have been used are invalid. Please check the Documentation to see details on pagination.', 
                details = [
                    cryptoapis.models.banned_ip_address_details_inner.BannedIpAddress_details_inner(
                        attribute = 'attribute which content caused the error', 
                        message = 'message describing the error', )
                    ]
            )
        else :
            return NewRevertedBlockE400(
                code = 'invalid_pagination',
                message = 'The pagination attributes that have been used are invalid. Please check the Documentation to see details on pagination.',
        )
        """

    def testNewRevertedBlockE400(self):
        """Test NewRevertedBlockE400"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
