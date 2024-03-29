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
from cryptoapis.models.list_confirmed_transactions_by_address_ribsd_vin_inner import ListConfirmedTransactionsByAddressRIBSDVinInner  # noqa: E501
from cryptoapis.rest import ApiException

class TestListConfirmedTransactionsByAddressRIBSDVinInner(unittest.TestCase):
    """ListConfirmedTransactionsByAddressRIBSDVinInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ListConfirmedTransactionsByAddressRIBSDVinInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListConfirmedTransactionsByAddressRIBSDVinInner`
        """
        model = cryptoapis.models.list_confirmed_transactions_by_address_ribsd_vin_inner.ListConfirmedTransactionsByAddressRIBSDVinInner()  # noqa: E501
        if include_optional :
            return ListConfirmedTransactionsByAddressRIBSDVinInner(
                addresses = [
                    'DPzdWPsKaGvRn3AH7WjBpnNVHhAPELDY4o'
                    ], 
                coinbase = '0301352f0101', 
                script_sig = cryptoapis.models.list_confirmed_transactions_by_address_ribsd_vin_inner_script_sig.ListConfirmedTransactionsByAddressRIBSD_vin_inner_scriptSig(
                    asm = '030483ff6271580681f4f7828c01df56d5aebfe982cbaa2922594be9eb6cf40206 OP_CHECKSIG', 
                    hex = '21030483ff6271580681f4f7828c01df56d5aebfe982cbaa2922594be9eb6cf40206ac', 
                    type = 'pubkey', ), 
                sequence = '4294967295', 
                txid = 'e1945b5d7e05f6d5ff77983d8a701b806722063559ed2528721b23fcb50baf06', 
                txinwitness = [
                    'nY1qa6325pH5zfGjA3NW16xPYG8XYQjtbS'
                    ], 
                value = '0.0225', 
                vout = 1
            )
        else :
            return ListConfirmedTransactionsByAddressRIBSDVinInner(
                addresses = [
                    'DPzdWPsKaGvRn3AH7WjBpnNVHhAPELDY4o'
                    ],
                coinbase = '0301352f0101',
                script_sig = cryptoapis.models.list_confirmed_transactions_by_address_ribsd_vin_inner_script_sig.ListConfirmedTransactionsByAddressRIBSD_vin_inner_scriptSig(
                    asm = '030483ff6271580681f4f7828c01df56d5aebfe982cbaa2922594be9eb6cf40206 OP_CHECKSIG', 
                    hex = '21030483ff6271580681f4f7828c01df56d5aebfe982cbaa2922594be9eb6cf40206ac', 
                    type = 'pubkey', ),
                sequence = '4294967295',
                txinwitness = [
                    'nY1qa6325pH5zfGjA3NW16xPYG8XYQjtbS'
                    ],
                value = '0.0225',
        )
        """

    def testListConfirmedTransactionsByAddressRIBSDVinInner(self):
        """Test ListConfirmedTransactionsByAddressRIBSDVinInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
