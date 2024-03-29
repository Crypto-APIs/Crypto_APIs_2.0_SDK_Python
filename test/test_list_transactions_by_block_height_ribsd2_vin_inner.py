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
from cryptoapis.models.list_transactions_by_block_height_ribsd2_vin_inner import ListTransactionsByBlockHeightRIBSD2VinInner  # noqa: E501
from cryptoapis.rest import ApiException

class TestListTransactionsByBlockHeightRIBSD2VinInner(unittest.TestCase):
    """ListTransactionsByBlockHeightRIBSD2VinInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ListTransactionsByBlockHeightRIBSD2VinInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListTransactionsByBlockHeightRIBSD2VinInner`
        """
        model = cryptoapis.models.list_transactions_by_block_height_ribsd2_vin_inner.ListTransactionsByBlockHeightRIBSD2VinInner()  # noqa: E501
        if include_optional :
            return ListTransactionsByBlockHeightRIBSD2VinInner(
                addresses = [
                    'DPzdWPsKaGvRn3AH7WjBpnNVHhAPELDY4o'
                    ], 
                coinbase = '03dcf4150c0b2f454233322f414431322f04da88506004565cc01f0c3130fc5f4e050000000000000a626368706f6f6c172f20626974636f696e636173682e6e6574776f726b202f', 
                script_sig = cryptoapis.models.get_transaction_details_by_transaction_idribsd_vin_inner_script_sig.GetTransactionDetailsByTransactionIDRIBSD_vin_inner_scriptSig(
                    asm = '030483ff6271580681f4f7828c01df56d5aebfe982cbaa2922594be9eb6cf40206 OP_CHECKSIG', 
                    hex = '21030483ff6271580681f4f7828c01df56d5aebfe982cbaa2922594be9eb6cf40206ac', 
                    type = 'scripthash', ), 
                sequence = '4294967295', 
                txid = 'e7d3052b4b87af78b6ca03db84357388c82475145cdc43cc3aa11e2b3dda60c5', 
                txinwitness = [
                    'nY1qa6325pH5zfGjA3NW16xPYG8XYQjtbS'
                    ], 
                value = '0.0225', 
                vout = 2
            )
        else :
            return ListTransactionsByBlockHeightRIBSD2VinInner(
                addresses = [
                    'DPzdWPsKaGvRn3AH7WjBpnNVHhAPELDY4o'
                    ],
                script_sig = cryptoapis.models.get_transaction_details_by_transaction_idribsd_vin_inner_script_sig.GetTransactionDetailsByTransactionIDRIBSD_vin_inner_scriptSig(
                    asm = '030483ff6271580681f4f7828c01df56d5aebfe982cbaa2922594be9eb6cf40206 OP_CHECKSIG', 
                    hex = '21030483ff6271580681f4f7828c01df56d5aebfe982cbaa2922594be9eb6cf40206ac', 
                    type = 'scripthash', ),
                sequence = '4294967295',
                txinwitness = [
                    'nY1qa6325pH5zfGjA3NW16xPYG8XYQjtbS'
                    ],
                value = '0.0225',
                vout = 2,
        )
        """

    def testListTransactionsByBlockHeightRIBSD2VinInner(self):
        """Test ListTransactionsByBlockHeightRIBSD2VinInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
