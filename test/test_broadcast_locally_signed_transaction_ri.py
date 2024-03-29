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
from cryptoapis.models.broadcast_locally_signed_transaction_ri import BroadcastLocallySignedTransactionRI  # noqa: E501
from cryptoapis.rest import ApiException

class TestBroadcastLocallySignedTransactionRI(unittest.TestCase):
    """BroadcastLocallySignedTransactionRI unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test BroadcastLocallySignedTransactionRI
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BroadcastLocallySignedTransactionRI`
        """
        model = cryptoapis.models.broadcast_locally_signed_transaction_ri.BroadcastLocallySignedTransactionRI()  # noqa: E501
        if include_optional :
            return BroadcastLocallySignedTransactionRI(
                transaction_id = '347d96855d41b77f1e23048fff11c18e9fe699ee69b0b402338f34189734e0a2'
            )
        else :
            return BroadcastLocallySignedTransactionRI(
                transaction_id = '347d96855d41b77f1e23048fff11c18e9fe699ee69b0b402338f34189734e0a2',
        )
        """

    def testBroadcastLocallySignedTransactionRI(self):
        """Test BroadcastLocallySignedTransactionRI"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
