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
from cryptoapis.models.get_wallet_transaction_details_by_transaction_idribsbc_vout_inner import GetWalletTransactionDetailsByTransactionIDRIBSBCVoutInner  # noqa: E501
from cryptoapis.rest import ApiException

class TestGetWalletTransactionDetailsByTransactionIDRIBSBCVoutInner(unittest.TestCase):
    """GetWalletTransactionDetailsByTransactionIDRIBSBCVoutInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetWalletTransactionDetailsByTransactionIDRIBSBCVoutInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetWalletTransactionDetailsByTransactionIDRIBSBCVoutInner`
        """
        model = cryptoapis.models.get_wallet_transaction_details_by_transaction_idribsbc_vout_inner.GetWalletTransactionDetailsByTransactionIDRIBSBCVoutInner()  # noqa: E501
        if include_optional :
            return GetWalletTransactionDetailsByTransactionIDRIBSBCVoutInner(
                is_spent = False, 
                script_pub_key = cryptoapis.models.get_wallet_transaction_details_by_transaction_idribsbc_vout_inner_script_pub_key.GetWalletTransactionDetailsByTransactionIDRIBSBC_vout_inner_scriptPubKey(
                    addresses = [
                        'qqux7gek8sg6r9qjkrdmrvz6t4xet3ax3gztt2drzk'
                        ], 
                    asm = 'OP_DUP OP_HASH160 386f23363c11a19412b0dbb1b05a5d4d95c7a68a OP_EQUALVERIFY OP_CHECKSIG', 
                    hex = 'a914507a5bd8cac1d9efdf4c0a4bfacb3e0abb4f8d1587', 
                    req_sigs = 1, 
                    type = 'pubkeyhash', ), 
                value = '0.000122'
            )
        else :
            return GetWalletTransactionDetailsByTransactionIDRIBSBCVoutInner(
                is_spent = False,
                script_pub_key = cryptoapis.models.get_wallet_transaction_details_by_transaction_idribsbc_vout_inner_script_pub_key.GetWalletTransactionDetailsByTransactionIDRIBSBC_vout_inner_scriptPubKey(
                    addresses = [
                        'qqux7gek8sg6r9qjkrdmrvz6t4xet3ax3gztt2drzk'
                        ], 
                    asm = 'OP_DUP OP_HASH160 386f23363c11a19412b0dbb1b05a5d4d95c7a68a OP_EQUALVERIFY OP_CHECKSIG', 
                    hex = 'a914507a5bd8cac1d9efdf4c0a4bfacb3e0abb4f8d1587', 
                    req_sigs = 1, 
                    type = 'pubkeyhash', ),
                value = '0.000122',
        )
        """

    def testGetWalletTransactionDetailsByTransactionIDRIBSBCVoutInner(self):
        """Test GetWalletTransactionDetailsByTransactionIDRIBSBCVoutInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
