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
from cryptoapis.models.list_hd_wallet_x_pub_y_pub_z_pub_utxos400_response import ListHDWalletXPubYPubZPubUTXOs400Response  # noqa: E501
from cryptoapis.rest import ApiException

class TestListHDWalletXPubYPubZPubUTXOs400Response(unittest.TestCase):
    """ListHDWalletXPubYPubZPubUTXOs400Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ListHDWalletXPubYPubZPubUTXOs400Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListHDWalletXPubYPubZPubUTXOs400Response`
        """
        model = cryptoapis.models.list_hd_wallet_x_pub_y_pub_z_pub_utxos400_response.ListHDWalletXPubYPubZPubUTXOs400Response()  # noqa: E501
        if include_optional :
            return ListHDWalletXPubYPubZPubUTXOs400Response(
                api_version = '2021-03-20', 
                request_id = '601c1710034ed6d407996b30', 
                context = 'yourExampleString', 
                error = cryptoapis.models.list_hd_wallet_x_pub_y_pub_z_pub_utxos_e400.ListHDWalletXPubYPubZPubUTXOsE400()
            )
        else :
            return ListHDWalletXPubYPubZPubUTXOs400Response(
                api_version = '2021-03-20',
                request_id = '601c1710034ed6d407996b30',
                error = cryptoapis.models.list_hd_wallet_x_pub_y_pub_z_pub_utxos_e400.ListHDWalletXPubYPubZPubUTXOsE400(),
        )
        """

    def testListHDWalletXPubYPubZPubUTXOs400Response(self):
        """Test ListHDWalletXPubYPubZPubUTXOs400Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
