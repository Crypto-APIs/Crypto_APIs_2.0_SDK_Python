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
from cryptoapis.models.derive_and_sync_new_change_addresses_rb_data_item import DeriveAndSyncNewChangeAddressesRBDataItem  # noqa: E501
from cryptoapis.rest import ApiException

class TestDeriveAndSyncNewChangeAddressesRBDataItem(unittest.TestCase):
    """DeriveAndSyncNewChangeAddressesRBDataItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DeriveAndSyncNewChangeAddressesRBDataItem
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeriveAndSyncNewChangeAddressesRBDataItem`
        """
        model = cryptoapis.models.derive_and_sync_new_change_addresses_rb_data_item.DeriveAndSyncNewChangeAddressesRBDataItem()  # noqa: E501
        if include_optional :
            return DeriveAndSyncNewChangeAddressesRBDataItem(
                extended_public_key = 'xpub6BuJ8T4xTEePRTWxEcyyZRHPRZw91GFRjuu4H1eNqNGDswpraD5Hthf7JBbK7iQayuLf2MbxT6MVrKGbY7HvBcQo937Qiwmxz7Fzy9S5y9q'
            )
        else :
            return DeriveAndSyncNewChangeAddressesRBDataItem(
                extended_public_key = 'xpub6BuJ8T4xTEePRTWxEcyyZRHPRZw91GFRjuu4H1eNqNGDswpraD5Hthf7JBbK7iQayuLf2MbxT6MVrKGbY7HvBcQo937Qiwmxz7Fzy9S5y9q',
        )
        """

    def testDeriveAndSyncNewChangeAddressesRBDataItem(self):
        """Test DeriveAndSyncNewChangeAddressesRBDataItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
