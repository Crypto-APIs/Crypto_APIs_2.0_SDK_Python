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
from cryptoapis.models.decode_raw_transaction_hex_risb_vout_inner import DecodeRawTransactionHexRISBVoutInner  # noqa: E501
from cryptoapis.rest import ApiException

class TestDecodeRawTransactionHexRISBVoutInner(unittest.TestCase):
    """DecodeRawTransactionHexRISBVoutInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DecodeRawTransactionHexRISBVoutInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DecodeRawTransactionHexRISBVoutInner`
        """
        model = cryptoapis.models.decode_raw_transaction_hex_risb_vout_inner.DecodeRawTransactionHexRISBVoutInner()  # noqa: E501
        if include_optional :
            return DecodeRawTransactionHexRISBVoutInner(
                script_pub_key = cryptoapis.models.decode_raw_transaction_hex_risb_vout_inner_script_pub_key.DecodeRawTransactionHexRISB_vout_inner_scriptPubKey(
                    address = '2MzakdGTEp8SMWEHKwKM4HYv6uNCBXtHpkV', 
                    asm = 'OP_HASH160 507a5bd8cac1d9efdf4c0a4bfacb3e0abb4f8d15 OP_EQUAL', 
                    hex = 'a914507a5bd8cac1d9efdf4c0a4bfacb3e0abb4f8d1587', 
                    type = 'scripthash', ), 
                value = '0.00014400'
            )
        else :
            return DecodeRawTransactionHexRISBVoutInner(
                script_pub_key = cryptoapis.models.decode_raw_transaction_hex_risb_vout_inner_script_pub_key.DecodeRawTransactionHexRISB_vout_inner_scriptPubKey(
                    address = '2MzakdGTEp8SMWEHKwKM4HYv6uNCBXtHpkV', 
                    asm = 'OP_HASH160 507a5bd8cac1d9efdf4c0a4bfacb3e0abb4f8d15 OP_EQUAL', 
                    hex = 'a914507a5bd8cac1d9efdf4c0a4bfacb3e0abb4f8d1587', 
                    type = 'scripthash', ),
        )
        """

    def testDecodeRawTransactionHexRISBVoutInner(self):
        """Test DecodeRawTransactionHexRISBVoutInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()