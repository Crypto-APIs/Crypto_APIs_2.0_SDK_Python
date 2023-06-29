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
from cryptoapis.models.list_supported_assets403_response import ListSupportedAssets403Response  # noqa: E501
from cryptoapis.rest import ApiException

class TestListSupportedAssets403Response(unittest.TestCase):
    """ListSupportedAssets403Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ListSupportedAssets403Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListSupportedAssets403Response`
        """
        model = cryptoapis.models.list_supported_assets403_response.ListSupportedAssets403Response()  # noqa: E501
        if include_optional :
            return ListSupportedAssets403Response(
                api_version = '2021-03-20', 
                request_id = '601c1710034ed6d407996b30', 
                context = 'yourExampleString', 
                error = cryptoapis.models.list_supported_assets_e403.ListSupportedAssetsE403()
            )
        else :
            return ListSupportedAssets403Response(
                api_version = '2021-03-20',
                request_id = '601c1710034ed6d407996b30',
                error = cryptoapis.models.list_supported_assets_e403.ListSupportedAssetsE403(),
        )
        """

    def testListSupportedAssets403Response(self):
        """Test ListSupportedAssets403Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
