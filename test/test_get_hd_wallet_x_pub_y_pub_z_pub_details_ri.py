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
from cryptoapis.models.get_hd_wallet_x_pub_y_pub_z_pub_details_ri import GetHDWalletXPubYPubZPubDetailsRI  # noqa: E501
from cryptoapis.rest import ApiException

class TestGetHDWalletXPubYPubZPubDetailsRI(unittest.TestCase):
    """GetHDWalletXPubYPubZPubDetailsRI unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetHDWalletXPubYPubZPubDetailsRI
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetHDWalletXPubYPubZPubDetailsRI`
        """
        model = cryptoapis.models.get_hd_wallet_x_pub_y_pub_z_pub_details_ri.GetHDWalletXPubYPubZPubDetailsRI()  # noqa: E501
        if include_optional :
            return GetHDWalletXPubYPubZPubDetailsRI(
                confirmed_balance = '0.0021', 
                total_received = '0.0002', 
                total_spent = '0.0001'
            )
        else :
            return GetHDWalletXPubYPubZPubDetailsRI(
                confirmed_balance = '0.0021',
        )
        """

    def testGetHDWalletXPubYPubZPubDetailsRI(self):
        """Test GetHDWalletXPubYPubZPubDetailsRI"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
