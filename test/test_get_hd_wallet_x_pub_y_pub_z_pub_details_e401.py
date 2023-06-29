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
from cryptoapis.models.get_hd_wallet_x_pub_y_pub_z_pub_details_e401 import GetHDWalletXPubYPubZPubDetailsE401  # noqa: E501
from cryptoapis.rest import ApiException

class TestGetHDWalletXPubYPubZPubDetailsE401(unittest.TestCase):
    """GetHDWalletXPubYPubZPubDetailsE401 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetHDWalletXPubYPubZPubDetailsE401
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetHDWalletXPubYPubZPubDetailsE401`
        """
        model = cryptoapis.models.get_hd_wallet_x_pub_y_pub_z_pub_details_e401.GetHDWalletXPubYPubZPubDetailsE401()  # noqa: E501
        if include_optional :
            return GetHDWalletXPubYPubZPubDetailsE401(
                code = 'invalid_api_key', 
                message = 'The provided API key is invalid. Please, generate a new one from your Dashboard.', 
                details = [
                    cryptoapis.models.banned_ip_address_details_inner.BannedIpAddress_details_inner(
                        attribute = 'attribute which content caused the error', 
                        message = 'message describing the error', )
                    ]
            )
        else :
            return GetHDWalletXPubYPubZPubDetailsE401(
                code = 'invalid_api_key',
                message = 'The provided API key is invalid. Please, generate a new one from your Dashboard.',
        )
        """

    def testGetHDWalletXPubYPubZPubDetailsE401(self):
        """Test GetHDWalletXPubYPubZPubDetailsE401"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
