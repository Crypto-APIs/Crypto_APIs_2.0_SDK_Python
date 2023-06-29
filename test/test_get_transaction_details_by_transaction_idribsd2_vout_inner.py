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
from cryptoapis.models.get_transaction_details_by_transaction_idribsd2_vout_inner import GetTransactionDetailsByTransactionIDRIBSD2VoutInner  # noqa: E501
from cryptoapis.rest import ApiException

class TestGetTransactionDetailsByTransactionIDRIBSD2VoutInner(unittest.TestCase):
    """GetTransactionDetailsByTransactionIDRIBSD2VoutInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetTransactionDetailsByTransactionIDRIBSD2VoutInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetTransactionDetailsByTransactionIDRIBSD2VoutInner`
        """
        model = cryptoapis.models.get_transaction_details_by_transaction_idribsd2_vout_inner.GetTransactionDetailsByTransactionIDRIBSD2VoutInner()  # noqa: E501
        if include_optional :
            return GetTransactionDetailsByTransactionIDRIBSD2VoutInner(
                is_spent = False, 
                script_pub_key = cryptoapis.models.get_transaction_details_by_transaction_idribsd2_vout_inner_script_pub_key.GetTransactionDetailsByTransactionIDRIBSD2_vout_inner_scriptPubKey(
                    addresses = [
                        ''
                        ], 
                    asm = 'OP_DUP OP_HASH160 4112d3f2cc01db043c0e638bb6338c83a7b9aa8f OP_EQUALVERIFY OP_CHECKSIG', 
                    hex = '76a9144112d3f2cc01db043c0e638bb6338c83a7b9aa8f88ac', 
                    req_sigs = 1, 
                    type = 'scripthash', ), 
                value = '0.5896'
            )
        else :
            return GetTransactionDetailsByTransactionIDRIBSD2VoutInner(
                is_spent = False,
                script_pub_key = cryptoapis.models.get_transaction_details_by_transaction_idribsd2_vout_inner_script_pub_key.GetTransactionDetailsByTransactionIDRIBSD2_vout_inner_scriptPubKey(
                    addresses = [
                        ''
                        ], 
                    asm = 'OP_DUP OP_HASH160 4112d3f2cc01db043c0e638bb6338c83a7b9aa8f OP_EQUALVERIFY OP_CHECKSIG', 
                    hex = '76a9144112d3f2cc01db043c0e638bb6338c83a7b9aa8f88ac', 
                    req_sigs = 1, 
                    type = 'scripthash', ),
                value = '0.5896',
        )
        """

    def testGetTransactionDetailsByTransactionIDRIBSD2VoutInner(self):
        """Test GetTransactionDetailsByTransactionIDRIBSD2VoutInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()