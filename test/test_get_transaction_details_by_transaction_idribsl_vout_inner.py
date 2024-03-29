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
from cryptoapis.models.get_transaction_details_by_transaction_idribsl_vout_inner import GetTransactionDetailsByTransactionIDRIBSLVoutInner  # noqa: E501
from cryptoapis.rest import ApiException

class TestGetTransactionDetailsByTransactionIDRIBSLVoutInner(unittest.TestCase):
    """GetTransactionDetailsByTransactionIDRIBSLVoutInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetTransactionDetailsByTransactionIDRIBSLVoutInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetTransactionDetailsByTransactionIDRIBSLVoutInner`
        """
        model = cryptoapis.models.get_transaction_details_by_transaction_idribsl_vout_inner.GetTransactionDetailsByTransactionIDRIBSLVoutInner()  # noqa: E501
        if include_optional :
            return GetTransactionDetailsByTransactionIDRIBSLVoutInner(
                is_spent = False, 
                script_pub_key = cryptoapis.models.get_transaction_details_by_transaction_idribsl_vout_inner_script_pub_key.GetTransactionDetailsByTransactionIDRIBSL_vout_inner_scriptPubKey(
                    addresses = [
                        '3LAAY4fp88RsNHkVW5DZJgqUdbMD5rVoqZ'
                        ], 
                    asm = 'OP_HASH160 ca94af32587de4e5006685ffffc65a818ccd3fbc OP_EQUAL', 
                    hex = 'a914ca94af32587de4e5006685ffffc65a818ccd3fbc87', 
                    req_sigs = 1, 
                    type = 'scripthash', ), 
                value = '0.03505975'
            )
        else :
            return GetTransactionDetailsByTransactionIDRIBSLVoutInner(
                is_spent = False,
                script_pub_key = cryptoapis.models.get_transaction_details_by_transaction_idribsl_vout_inner_script_pub_key.GetTransactionDetailsByTransactionIDRIBSL_vout_inner_scriptPubKey(
                    addresses = [
                        '3LAAY4fp88RsNHkVW5DZJgqUdbMD5rVoqZ'
                        ], 
                    asm = 'OP_HASH160 ca94af32587de4e5006685ffffc65a818ccd3fbc OP_EQUAL', 
                    hex = 'a914ca94af32587de4e5006685ffffc65a818ccd3fbc87', 
                    req_sigs = 1, 
                    type = 'scripthash', ),
                value = '0.03505975',
        )
        """

    def testGetTransactionDetailsByTransactionIDRIBSLVoutInner(self):
        """Test GetTransactionDetailsByTransactionIDRIBSLVoutInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
