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
from cryptoapis.models.get_transaction_details_by_transaction_idribsb import GetTransactionDetailsByTransactionIDRIBSB  # noqa: E501
from cryptoapis.rest import ApiException

class TestGetTransactionDetailsByTransactionIDRIBSB(unittest.TestCase):
    """GetTransactionDetailsByTransactionIDRIBSB unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetTransactionDetailsByTransactionIDRIBSB
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetTransactionDetailsByTransactionIDRIBSB`
        """
        model = cryptoapis.models.get_transaction_details_by_transaction_idribsb.GetTransactionDetailsByTransactionIDRIBSB()  # noqa: E501
        if include_optional :
            return GetTransactionDetailsByTransactionIDRIBSB(
                locktime = 1781965, 
                size = 248, 
                v_size = 166, 
                version = 1, 
                vin = [
                    cryptoapis.models.get_transaction_details_by_transaction_idribsb_vin_inner.GetTransactionDetailsByTransactionIDRIBSB_vin_inner(
                        addresses = [
                            '2N5PcdirZUzKF9bWuGdugNuzcQrCbBudxv1'
                            ], 
                        coinbase = '0399991d20706f6f6c2e656e6a6f79626f646965732e636f6d20393963336532346234374747a53e994c4a000001', 
                        script_sig = cryptoapis.models.get_transaction_details_by_transaction_idribsb_vin_inner_script_sig.GetTransactionDetailsByTransactionIDRIBSB_vin_inner_scriptSig(
                            asm = '0014daaf6d5cb86befe42df851a4d1df052e663754c1', 
                            hex = '160014daaf6d5cb86befe42df851a4d1df052e663754c1', 
                            type = 'scripthash', ), 
                        sequence = 4294967295, 
                        txid = 'caee978cae255bbe303ac86152679e46113a8b12925aa3afaa312d89d11ccbf8', 
                        txinwitness = [
                            '3045022100c11ea5740bcd69f0f68a4914279838014d28923134d18e05c5a5486dfd06cc8c02200dadccec3f07bed0d1040f9e5a155efa5fdd40fc91f92342578d26848da4c6b901'
                            ], 
                        value = '0.00873472', 
                        vout = 1, )
                    ], 
                vout = [
                    cryptoapis.models.get_transaction_details_by_transaction_idribsb_vout_inner.GetTransactionDetailsByTransactionIDRIBSB_vout_inner(
                        is_spent = False, 
                        script_pub_key = cryptoapis.models.get_transaction_details_by_transaction_idribsb_vout_inner_script_pub_key.GetTransactionDetailsByTransactionIDRIBSB_vout_inner_scriptPubKey(
                            addresses = [
                                '2MzakdGTEp8SMWEHKwKM4HYv6uNCBXtHpkV'
                                ], 
                            asm = 'OP_HASH160 507a5bd8cac1d9efdf4c0a4bfacb3e0abb4f8d15 OP_EQUAL', 
                            hex = 'a914507a5bd8cac1d9efdf4c0a4bfacb3e0abb4f8d1587', 
                            req_sigs = 1, 
                            type = 'scripthash', ), 
                        value = '0.00014400', )
                    ]
            )
        else :
            return GetTransactionDetailsByTransactionIDRIBSB(
                locktime = 1781965,
                size = 248,
                v_size = 166,
                version = 1,
                vin = [
                    cryptoapis.models.get_transaction_details_by_transaction_idribsb_vin_inner.GetTransactionDetailsByTransactionIDRIBSB_vin_inner(
                        addresses = [
                            '2N5PcdirZUzKF9bWuGdugNuzcQrCbBudxv1'
                            ], 
                        coinbase = '0399991d20706f6f6c2e656e6a6f79626f646965732e636f6d20393963336532346234374747a53e994c4a000001', 
                        script_sig = cryptoapis.models.get_transaction_details_by_transaction_idribsb_vin_inner_script_sig.GetTransactionDetailsByTransactionIDRIBSB_vin_inner_scriptSig(
                            asm = '0014daaf6d5cb86befe42df851a4d1df052e663754c1', 
                            hex = '160014daaf6d5cb86befe42df851a4d1df052e663754c1', 
                            type = 'scripthash', ), 
                        sequence = 4294967295, 
                        txid = 'caee978cae255bbe303ac86152679e46113a8b12925aa3afaa312d89d11ccbf8', 
                        txinwitness = [
                            '3045022100c11ea5740bcd69f0f68a4914279838014d28923134d18e05c5a5486dfd06cc8c02200dadccec3f07bed0d1040f9e5a155efa5fdd40fc91f92342578d26848da4c6b901'
                            ], 
                        value = '0.00873472', 
                        vout = 1, )
                    ],
                vout = [
                    cryptoapis.models.get_transaction_details_by_transaction_idribsb_vout_inner.GetTransactionDetailsByTransactionIDRIBSB_vout_inner(
                        is_spent = False, 
                        script_pub_key = cryptoapis.models.get_transaction_details_by_transaction_idribsb_vout_inner_script_pub_key.GetTransactionDetailsByTransactionIDRIBSB_vout_inner_scriptPubKey(
                            addresses = [
                                '2MzakdGTEp8SMWEHKwKM4HYv6uNCBXtHpkV'
                                ], 
                            asm = 'OP_HASH160 507a5bd8cac1d9efdf4c0a4bfacb3e0abb4f8d15 OP_EQUAL', 
                            hex = 'a914507a5bd8cac1d9efdf4c0a4bfacb3e0abb4f8d1587', 
                            req_sigs = 1, 
                            type = 'scripthash', ), 
                        value = '0.00014400', )
                    ],
        )
        """

    def testGetTransactionDetailsByTransactionIDRIBSB(self):
        """Test GetTransactionDetailsByTransactionIDRIBSB"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
