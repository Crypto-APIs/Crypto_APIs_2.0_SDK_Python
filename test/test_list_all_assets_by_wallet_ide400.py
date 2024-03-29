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
from cryptoapis.models.list_all_assets_by_wallet_ide400 import ListAllAssetsByWalletIDE400  # noqa: E501
from cryptoapis.rest import ApiException

class TestListAllAssetsByWalletIDE400(unittest.TestCase):
    """ListAllAssetsByWalletIDE400 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ListAllAssetsByWalletIDE400
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListAllAssetsByWalletIDE400`
        """
        model = cryptoapis.models.list_all_assets_by_wallet_ide400.ListAllAssetsByWalletIDE400()  # noqa: E501
        if include_optional :
            return ListAllAssetsByWalletIDE400(
                code = 'invalid_pagination', 
                message = 'The pagination attributes that have been used are invalid. Please check the Documentation to see details on pagination.', 
                details = [
                    cryptoapis.models.banned_ip_address_details_inner.BannedIpAddress_details_inner(
                        attribute = 'attribute which content caused the error', 
                        message = 'message describing the error', )
                    ]
            )
        else :
            return ListAllAssetsByWalletIDE400(
                code = 'invalid_pagination',
                message = 'The pagination attributes that have been used are invalid. Please check the Documentation to see details on pagination.',
        )
        """

    def testListAllAssetsByWalletIDE400(self):
        """Test ListAllAssetsByWalletIDE400"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
