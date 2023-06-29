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
from cryptoapis.models.sync_new_hd_wallet_x_pub_y_pub_z_pub_rb import SyncNewHDWalletXPubYPubZPubRB  # noqa: E501
from cryptoapis.rest import ApiException

class TestSyncNewHDWalletXPubYPubZPubRB(unittest.TestCase):
    """SyncNewHDWalletXPubYPubZPubRB unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SyncNewHDWalletXPubYPubZPubRB
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SyncNewHDWalletXPubYPubZPubRB`
        """
        model = cryptoapis.models.sync_new_hd_wallet_x_pub_y_pub_z_pub_rb.SyncNewHDWalletXPubYPubZPubRB()  # noqa: E501
        if include_optional :
            return SyncNewHDWalletXPubYPubZPubRB(
                context = 'yourExampleString', 
                data = cryptoapis.models.sync_hd_wallet_x_pub_y_pub_z_pub_rb_data.SyncHDWalletXPubYPubZPubRB_data(
                    item = cryptoapis.models.sync_hd_wallet_x_pub_y_pub_z_pub_rb_data_item.SyncHDWalletXPubYPubZPubRB_data_item(
                        extended_public_key = 'upub5Ei6bRNneqozk6smK7dvtXHC5PjUyEL4ynCfMKvjznLcXi9DQaikETzQjHvJC43XexMvQs64jxB1njMjCHpRZ4xQWAmv3ge9cVtjfsHmbvQ', ), )
            )
        else :
            return SyncNewHDWalletXPubYPubZPubRB(
                data = cryptoapis.models.sync_hd_wallet_x_pub_y_pub_z_pub_rb_data.SyncHDWalletXPubYPubZPubRB_data(
                    item = cryptoapis.models.sync_hd_wallet_x_pub_y_pub_z_pub_rb_data_item.SyncHDWalletXPubYPubZPubRB_data_item(
                        extended_public_key = 'upub5Ei6bRNneqozk6smK7dvtXHC5PjUyEL4ynCfMKvjznLcXi9DQaikETzQjHvJC43XexMvQs64jxB1njMjCHpRZ4xQWAmv3ge9cVtjfsHmbvQ', ), ),
        )
        """

    def testSyncNewHDWalletXPubYPubZPubRB(self):
        """Test SyncNewHDWalletXPubYPubZPubRB"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
