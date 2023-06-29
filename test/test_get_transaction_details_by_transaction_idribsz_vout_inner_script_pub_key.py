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
from cryptoapis.models.get_transaction_details_by_transaction_idribsz_vout_inner_script_pub_key import GetTransactionDetailsByTransactionIDRIBSZVoutInnerScriptPubKey  # noqa: E501
from cryptoapis.rest import ApiException

class TestGetTransactionDetailsByTransactionIDRIBSZVoutInnerScriptPubKey(unittest.TestCase):
    """GetTransactionDetailsByTransactionIDRIBSZVoutInnerScriptPubKey unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetTransactionDetailsByTransactionIDRIBSZVoutInnerScriptPubKey
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetTransactionDetailsByTransactionIDRIBSZVoutInnerScriptPubKey`
        """
        model = cryptoapis.models.get_transaction_details_by_transaction_idribsz_vout_inner_script_pub_key.GetTransactionDetailsByTransactionIDRIBSZVoutInnerScriptPubKey()  # noqa: E501
        if include_optional :
            return GetTransactionDetailsByTransactionIDRIBSZVoutInnerScriptPubKey(
                addresses = [
                    't2UNzUUx8mWBCRYPRezvA363EYXyEpHokyi'
                    ], 
                asm = 'OP_HASH160 ef775f1f997f122a062fff1a2d7443abd1f9c642 OP_EQUAL', 
                hex = 'a914ef775f1f997f122a062fff1a2d7443abd1f9c64287', 
                req_sigs = 1, 
                type = 'pubkeyhash'
            )
        else :
            return GetTransactionDetailsByTransactionIDRIBSZVoutInnerScriptPubKey(
                addresses = [
                    't2UNzUUx8mWBCRYPRezvA363EYXyEpHokyi'
                    ],
                asm = 'OP_HASH160 ef775f1f997f122a062fff1a2d7443abd1f9c642 OP_EQUAL',
                hex = 'a914ef775f1f997f122a062fff1a2d7443abd1f9c64287',
                type = 'pubkeyhash',
        )
        """

    def testGetTransactionDetailsByTransactionIDRIBSZVoutInnerScriptPubKey(self):
        """Test GetTransactionDetailsByTransactionIDRIBSZVoutInnerScriptPubKey"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()