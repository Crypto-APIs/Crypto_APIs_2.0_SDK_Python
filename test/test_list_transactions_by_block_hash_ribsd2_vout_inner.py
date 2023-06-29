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
from cryptoapis.models.list_transactions_by_block_hash_ribsd2_vout_inner import ListTransactionsByBlockHashRIBSD2VoutInner  # noqa: E501
from cryptoapis.rest import ApiException

class TestListTransactionsByBlockHashRIBSD2VoutInner(unittest.TestCase):
    """ListTransactionsByBlockHashRIBSD2VoutInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ListTransactionsByBlockHashRIBSD2VoutInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListTransactionsByBlockHashRIBSD2VoutInner`
        """
        model = cryptoapis.models.list_transactions_by_block_hash_ribsd2_vout_inner.ListTransactionsByBlockHashRIBSD2VoutInner()  # noqa: E501
        if include_optional :
            return ListTransactionsByBlockHashRIBSD2VoutInner(
                is_spent = False, 
                script_pub_key = cryptoapis.models.list_transactions_by_block_hash_ribsd2_vout_inner_script_pub_key.ListTransactionsByBlockHashRIBSD2_vout_inner_scriptPubKey(
                    addresses = [
                        'nW3Hxfx9a9ef1MCHm6veWBbw1Nh2ZEefER'
                        ], 
                    asm = 'OP_DUP OP_HASH160 1442eec4888ec035fd27a82f227e09f548bec812 OP_EQUALVERIFY OP_CHECKSIG', 
                    hex = '76a9141442eec4888ec035fd27a82f227e09f548bec81288ac', 
                    req_sigs = 2, 
                    type = 'scripthash', ), 
                value = '10000'
            )
        else :
            return ListTransactionsByBlockHashRIBSD2VoutInner(
                is_spent = False,
                script_pub_key = cryptoapis.models.list_transactions_by_block_hash_ribsd2_vout_inner_script_pub_key.ListTransactionsByBlockHashRIBSD2_vout_inner_scriptPubKey(
                    addresses = [
                        'nW3Hxfx9a9ef1MCHm6veWBbw1Nh2ZEefER'
                        ], 
                    asm = 'OP_DUP OP_HASH160 1442eec4888ec035fd27a82f227e09f548bec812 OP_EQUALVERIFY OP_CHECKSIG', 
                    hex = '76a9141442eec4888ec035fd27a82f227e09f548bec81288ac', 
                    req_sigs = 2, 
                    type = 'scripthash', ),
                value = '10000',
        )
        """

    def testListTransactionsByBlockHashRIBSD2VoutInner(self):
        """Test ListTransactionsByBlockHashRIBSD2VoutInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
