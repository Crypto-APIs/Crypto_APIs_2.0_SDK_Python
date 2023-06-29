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
from cryptoapis.models.list_unconfirmed_transactions_by_address_ribsbc import ListUnconfirmedTransactionsByAddressRIBSBC  # noqa: E501
from cryptoapis.rest import ApiException

class TestListUnconfirmedTransactionsByAddressRIBSBC(unittest.TestCase):
    """ListUnconfirmedTransactionsByAddressRIBSBC unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ListUnconfirmedTransactionsByAddressRIBSBC
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListUnconfirmedTransactionsByAddressRIBSBC`
        """
        model = cryptoapis.models.list_unconfirmed_transactions_by_address_ribsbc.ListUnconfirmedTransactionsByAddressRIBSBC()  # noqa: E501
        if include_optional :
            return ListUnconfirmedTransactionsByAddressRIBSBC(
                locktime = 1781965, 
                size = 123, 
                version = 1, 
                vin = [
                    cryptoapis.models.list_unconfirmed_transactions_by_address_ribsbc_vin_inner.ListUnconfirmedTransactionsByAddressRIBSBC_vin_inner(
                        addresses = [
                            'bitcoincash:qq0adqyntn2zl9tsyjfagnyda9j2gfjkk574lxyrxd'
                            ], 
                        script_sig = cryptoapis.models.get_transaction_details_by_transaction_idribsb_vin_inner_script_sig.GetTransactionDetailsByTransactionIDRIBSB_vin_inner_scriptSig(
                            asm = '0014daaf6d5cb86befe42df851a4d1df052e663754c1', 
                            hex = '160014daaf6d5cb86befe42df851a4d1df052e663754c1', 
                            type = 'scripthash', ), 
                        sequence = '4294967295', 
                        txid = 'caee978cae255bbe303ac86152679e46113a8b12925aa3afaa312d89d11ccbf8', 
                        txinwitness = [
                            '3045022100c11ea5740bcd69f0f68a4914279838014d28923134d18e05c5a5486dfd06cc8c02200dadccec3f07bed0d1040f9e5a155efa5fdd40fc91f92342578d26848da4c6b901'
                            ], 
                        value = '0.00873472', 
                        vout = 1, )
                    ], 
                vout = [
                    cryptoapis.models.list_unconfirmed_transactions_by_address_ribsbc_vout_inner.ListUnconfirmedTransactionsByAddressRIBSBC_vout_inner(
                        is_spent = True, 
                        script_pub_key = cryptoapis.models.list_unconfirmed_transactions_by_address_ribsbc_vout_inner_script_pub_key.ListUnconfirmedTransactionsByAddressRIBSBC_vout_inner_scriptPubKey(
                            addresses = [
                                'bchtest:qqux7gek8sg6r9qjkrdmrvz6t4xet3ax3gztt2drzk'
                                ], 
                            asm = 'OP_DUP OP_HASH160 386f23363c11a19412b0dbb1b05a5d4d95c7a68a OP_EQUALVERIFY OP_CHECKSIG', 
                            hex = 'a914507a5bd8cac1d9efdf4c0a4bfacb3e0abb4f8d1587', 
                            req_sigs = 1, 
                            type = 'pubkeyhash', ), 
                        value = '0.000122', )
                    ]
            )
        else :
            return ListUnconfirmedTransactionsByAddressRIBSBC(
                locktime = 1781965,
                size = 123,
                version = 1,
                vin = [
                    cryptoapis.models.list_unconfirmed_transactions_by_address_ribsbc_vin_inner.ListUnconfirmedTransactionsByAddressRIBSBC_vin_inner(
                        addresses = [
                            'bitcoincash:qq0adqyntn2zl9tsyjfagnyda9j2gfjkk574lxyrxd'
                            ], 
                        script_sig = cryptoapis.models.get_transaction_details_by_transaction_idribsb_vin_inner_script_sig.GetTransactionDetailsByTransactionIDRIBSB_vin_inner_scriptSig(
                            asm = '0014daaf6d5cb86befe42df851a4d1df052e663754c1', 
                            hex = '160014daaf6d5cb86befe42df851a4d1df052e663754c1', 
                            type = 'scripthash', ), 
                        sequence = '4294967295', 
                        txid = 'caee978cae255bbe303ac86152679e46113a8b12925aa3afaa312d89d11ccbf8', 
                        txinwitness = [
                            '3045022100c11ea5740bcd69f0f68a4914279838014d28923134d18e05c5a5486dfd06cc8c02200dadccec3f07bed0d1040f9e5a155efa5fdd40fc91f92342578d26848da4c6b901'
                            ], 
                        value = '0.00873472', 
                        vout = 1, )
                    ],
                vout = [
                    cryptoapis.models.list_unconfirmed_transactions_by_address_ribsbc_vout_inner.ListUnconfirmedTransactionsByAddressRIBSBC_vout_inner(
                        is_spent = True, 
                        script_pub_key = cryptoapis.models.list_unconfirmed_transactions_by_address_ribsbc_vout_inner_script_pub_key.ListUnconfirmedTransactionsByAddressRIBSBC_vout_inner_scriptPubKey(
                            addresses = [
                                'bchtest:qqux7gek8sg6r9qjkrdmrvz6t4xet3ax3gztt2drzk'
                                ], 
                            asm = 'OP_DUP OP_HASH160 386f23363c11a19412b0dbb1b05a5d4d95c7a68a OP_EQUALVERIFY OP_CHECKSIG', 
                            hex = 'a914507a5bd8cac1d9efdf4c0a4bfacb3e0abb4f8d1587', 
                            req_sigs = 1, 
                            type = 'pubkeyhash', ), 
                        value = '0.000122', )
                    ],
        )
        """

    def testListUnconfirmedTransactionsByAddressRIBSBC(self):
        """Test ListUnconfirmedTransactionsByAddressRIBSBC"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
