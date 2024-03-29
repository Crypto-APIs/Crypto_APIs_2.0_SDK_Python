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
from cryptoapis.models.list_unconfirmed_transactions_by_address_ribsd2_vin_inner import ListUnconfirmedTransactionsByAddressRIBSD2VinInner  # noqa: E501
from cryptoapis.rest import ApiException

class TestListUnconfirmedTransactionsByAddressRIBSD2VinInner(unittest.TestCase):
    """ListUnconfirmedTransactionsByAddressRIBSD2VinInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ListUnconfirmedTransactionsByAddressRIBSD2VinInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListUnconfirmedTransactionsByAddressRIBSD2VinInner`
        """
        model = cryptoapis.models.list_unconfirmed_transactions_by_address_ribsd2_vin_inner.ListUnconfirmedTransactionsByAddressRIBSD2VinInner()  # noqa: E501
        if include_optional :
            return ListUnconfirmedTransactionsByAddressRIBSD2VinInner(
                addresses = [
                    'yP8A3cbdxRtLRduy5mXDsBnJtMzHWs6ZXr'
                    ], 
                script_sig = cryptoapis.models.list_confirmed_transactions_by_address_ribsd2_vin_inner_script_sig.ListConfirmedTransactionsByAddressRIBSD2_vin_inner_scriptSig(
                    asm = 'OP_DUP OP_HASH160 1ec5c66e9789c655ae068d35088b4073345fe0b0 OP_EQUALVERIFY OP_CHECKSIG', 
                    hex = '76a9141ec5c66e9789c655ae068d35088b4073345fe0b088ac', 
                    type = 'scripthash', ), 
                sequence = '4294967295', 
                txid = '54b8f0e54b4b66fab386c6f9dea76bfe06524ab71d1d42b321aea9a7fea50f48', 
                txinwitness = [
                    'yP8A3cbdxRtLRduy5mXDsBnJtMzHWs6ZXr'
                    ], 
                value = '7.76021116', 
                vout = 1
            )
        else :
            return ListUnconfirmedTransactionsByAddressRIBSD2VinInner(
                addresses = [
                    'yP8A3cbdxRtLRduy5mXDsBnJtMzHWs6ZXr'
                    ],
                script_sig = cryptoapis.models.list_confirmed_transactions_by_address_ribsd2_vin_inner_script_sig.ListConfirmedTransactionsByAddressRIBSD2_vin_inner_scriptSig(
                    asm = 'OP_DUP OP_HASH160 1ec5c66e9789c655ae068d35088b4073345fe0b0 OP_EQUALVERIFY OP_CHECKSIG', 
                    hex = '76a9141ec5c66e9789c655ae068d35088b4073345fe0b088ac', 
                    type = 'scripthash', ),
                sequence = '4294967295',
                txid = '54b8f0e54b4b66fab386c6f9dea76bfe06524ab71d1d42b321aea9a7fea50f48',
                txinwitness = [
                    'yP8A3cbdxRtLRduy5mXDsBnJtMzHWs6ZXr'
                    ],
                vout = 1,
        )
        """

    def testListUnconfirmedTransactionsByAddressRIBSD2VinInner(self):
        """Test ListUnconfirmedTransactionsByAddressRIBSD2VinInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
