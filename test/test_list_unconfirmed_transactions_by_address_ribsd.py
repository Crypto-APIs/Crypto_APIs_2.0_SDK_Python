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
from cryptoapis.models.list_unconfirmed_transactions_by_address_ribsd import ListUnconfirmedTransactionsByAddressRIBSD  # noqa: E501
from cryptoapis.rest import ApiException

class TestListUnconfirmedTransactionsByAddressRIBSD(unittest.TestCase):
    """ListUnconfirmedTransactionsByAddressRIBSD unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ListUnconfirmedTransactionsByAddressRIBSD
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListUnconfirmedTransactionsByAddressRIBSD`
        """
        model = cryptoapis.models.list_unconfirmed_transactions_by_address_ribsd.ListUnconfirmedTransactionsByAddressRIBSD()  # noqa: E501
        if include_optional :
            return ListUnconfirmedTransactionsByAddressRIBSD(
                locktime = 0, 
                size = 233, 
                version = 2, 
                vin = [
                    cryptoapis.models.list_unconfirmed_transactions_by_address_ribsd_vin_inner.ListUnconfirmedTransactionsByAddressRIBSD_vin_inner(
                        addresses = [
                            'DPzdWPsKaGvRn3AH7WjBpnNVHhAPELDY4o'
                            ], 
                        script_sig = cryptoapis.models.list_confirmed_transactions_by_address_ribsd_vin_inner_script_sig.ListConfirmedTransactionsByAddressRIBSD_vin_inner_scriptSig(
                            asm = '030483ff6271580681f4f7828c01df56d5aebfe982cbaa2922594be9eb6cf40206 OP_CHECKSIG', 
                            hex = '21030483ff6271580681f4f7828c01df56d5aebfe982cbaa2922594be9eb6cf40206ac', 
                            type = 'pubkey', ), 
                        sequence = 4294967295, 
                        txid = 'e1945b5d7e05f6d5ff77983d8a701b806722063559ed2528721b23fcb50baf06', 
                        txinwitness = [
                            'nY1qa6325pH5zfGjA3NW16xPYG8XYQjtbS'
                            ], 
                        value = '0.0225', 
                        vout = 1, )
                    ], 
                vout = [
                    cryptoapis.models.get_transaction_details_by_transaction_idribsd_vout_inner.GetTransactionDetailsByTransactionIDRIBSD_vout_inner(
                        is_spent = False, 
                        script_pub_key = cryptoapis.models.get_transaction_details_by_transaction_idribsd_vout_inner_script_pub_key.GetTransactionDetailsByTransactionIDRIBSD_vout_inner_scriptPubKey(
                            addresses = [
                                'yd5KMREs3GLMe6mTJYr3YrH1juwNwrFCfB'
                                ], 
                            asm = 'OP_DUP OP_HASH160 430158211605af1f0fa26d90405199621bdae5cd OP_EQUALVERIFY OP_CHECKSIG', 
                            hex = '76a914430158211605af1f0fa26d90405199621bdae5cd88ac', 
                            req_sigs = 1, 
                            type = 'scripthash', ), 
                        value = '11.25', )
                    ]
            )
        else :
            return ListUnconfirmedTransactionsByAddressRIBSD(
                locktime = 0,
                size = 233,
                version = 2,
                vin = [
                    cryptoapis.models.list_unconfirmed_transactions_by_address_ribsd_vin_inner.ListUnconfirmedTransactionsByAddressRIBSD_vin_inner(
                        addresses = [
                            'DPzdWPsKaGvRn3AH7WjBpnNVHhAPELDY4o'
                            ], 
                        script_sig = cryptoapis.models.list_confirmed_transactions_by_address_ribsd_vin_inner_script_sig.ListConfirmedTransactionsByAddressRIBSD_vin_inner_scriptSig(
                            asm = '030483ff6271580681f4f7828c01df56d5aebfe982cbaa2922594be9eb6cf40206 OP_CHECKSIG', 
                            hex = '21030483ff6271580681f4f7828c01df56d5aebfe982cbaa2922594be9eb6cf40206ac', 
                            type = 'pubkey', ), 
                        sequence = 4294967295, 
                        txid = 'e1945b5d7e05f6d5ff77983d8a701b806722063559ed2528721b23fcb50baf06', 
                        txinwitness = [
                            'nY1qa6325pH5zfGjA3NW16xPYG8XYQjtbS'
                            ], 
                        value = '0.0225', 
                        vout = 1, )
                    ],
                vout = [
                    cryptoapis.models.get_transaction_details_by_transaction_idribsd_vout_inner.GetTransactionDetailsByTransactionIDRIBSD_vout_inner(
                        is_spent = False, 
                        script_pub_key = cryptoapis.models.get_transaction_details_by_transaction_idribsd_vout_inner_script_pub_key.GetTransactionDetailsByTransactionIDRIBSD_vout_inner_scriptPubKey(
                            addresses = [
                                'yd5KMREs3GLMe6mTJYr3YrH1juwNwrFCfB'
                                ], 
                            asm = 'OP_DUP OP_HASH160 430158211605af1f0fa26d90405199621bdae5cd OP_EQUALVERIFY OP_CHECKSIG', 
                            hex = '76a914430158211605af1f0fa26d90405199621bdae5cd88ac', 
                            req_sigs = 1, 
                            type = 'scripthash', ), 
                        value = '11.25', )
                    ],
        )
        """

    def testListUnconfirmedTransactionsByAddressRIBSD(self):
        """Test ListUnconfirmedTransactionsByAddressRIBSD"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
