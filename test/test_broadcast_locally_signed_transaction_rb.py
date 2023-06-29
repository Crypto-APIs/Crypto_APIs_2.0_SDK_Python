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
from cryptoapis.models.broadcast_locally_signed_transaction_rb import BroadcastLocallySignedTransactionRB  # noqa: E501
from cryptoapis.rest import ApiException

class TestBroadcastLocallySignedTransactionRB(unittest.TestCase):
    """BroadcastLocallySignedTransactionRB unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test BroadcastLocallySignedTransactionRB
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BroadcastLocallySignedTransactionRB`
        """
        model = cryptoapis.models.broadcast_locally_signed_transaction_rb.BroadcastLocallySignedTransactionRB()  # noqa: E501
        if include_optional :
            return BroadcastLocallySignedTransactionRB(
                context = 'yourExampleString', 
                data = cryptoapis.models.broadcast_locally_signed_transaction_rb_data.BroadcastLocallySignedTransactionRB_data(
                    item = cryptoapis.models.broadcast_locally_signed_transaction_rb_data_item.BroadcastLocallySignedTransactionRB_data_item(
                        callback_secret_key = 'yourSecretString', 
                        callback_url = 'https://example.com', 
                        signed_transaction_hex = '0xf86a22827d00831e8480941b85a43e2e7f52e766ddfdfa2b901c42cb1201be8801b27f33b807c0008029a084ccbf02b27e0842fb1eda7a187a5589c3759be0e969e0ca989dc469a5e5e394a02e111e1156b197f1de4c1d9ba4af26e50665ea6d617d05b3e4047da12b915e69', ), )
            )
        else :
            return BroadcastLocallySignedTransactionRB(
                data = cryptoapis.models.broadcast_locally_signed_transaction_rb_data.BroadcastLocallySignedTransactionRB_data(
                    item = cryptoapis.models.broadcast_locally_signed_transaction_rb_data_item.BroadcastLocallySignedTransactionRB_data_item(
                        callback_secret_key = 'yourSecretString', 
                        callback_url = 'https://example.com', 
                        signed_transaction_hex = '0xf86a22827d00831e8480941b85a43e2e7f52e766ddfdfa2b901c42cb1201be8801b27f33b807c0008029a084ccbf02b27e0842fb1eda7a187a5589c3759be0e969e0ca989dc469a5e5e394a02e111e1156b197f1de4c1d9ba4af26e50665ea6d617d05b3e4047da12b915e69', ), ),
        )
        """

    def testBroadcastLocallySignedTransactionRB(self):
        """Test BroadcastLocallySignedTransactionRB"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
