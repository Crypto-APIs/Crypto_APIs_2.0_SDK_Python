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
from cryptoapis.models.list_tokens_transfers_by_transaction_hash_ri import ListTokensTransfersByTransactionHashRI  # noqa: E501
from cryptoapis.rest import ApiException

class TestListTokensTransfersByTransactionHashRI(unittest.TestCase):
    """ListTokensTransfersByTransactionHashRI unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ListTokensTransfersByTransactionHashRI
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListTokensTransfersByTransactionHashRI`
        """
        model = cryptoapis.models.list_tokens_transfers_by_transaction_hash_ri.ListTokensTransfersByTransactionHashRI()  # noqa: E501
        if include_optional :
            return ListTokensTransfersByTransactionHashRI(
                contract_address = '0x7495fede000c8a3b77eeae09cf70fa94cd2d53f5', 
                mined_in_block_height = 9841271, 
                recipient_address = '0x9e91eb3a35b96f0f0fe71f3c17fe8d29eb406b16', 
                sender_address = '0x9df8a6441e8a3dda75019595d431f9aa0dec475c', 
                token_decimals = 6, 
                token_name = 'Tether USD', 
                token_symbol = 'BAND', 
                token_type = 'ERC-20', 
                tokens_amount = '0.0012', 
                transaction_hash = '0x60ba3dded833e61f63b6b6d62afe5c7526c5ca09c6744749f13eef11afde2cb4', 
                transaction_timestamp = 1615818368, 
                transaction_fee = cryptoapis.models.list_tokens_transfers_by_transaction_hash_ri_transaction_fee.ListTokensTransfersByTransactionHashRI_transactionFee(
                    amount = '0.0000051873', 
                    unit = 'ETH', )
            )
        else :
            return ListTokensTransfersByTransactionHashRI(
                contract_address = '0x7495fede000c8a3b77eeae09cf70fa94cd2d53f5',
                mined_in_block_height = 9841271,
                recipient_address = '0x9e91eb3a35b96f0f0fe71f3c17fe8d29eb406b16',
                sender_address = '0x9df8a6441e8a3dda75019595d431f9aa0dec475c',
                token_type = 'ERC-20',
                tokens_amount = '0.0012',
                transaction_hash = '0x60ba3dded833e61f63b6b6d62afe5c7526c5ca09c6744749f13eef11afde2cb4',
                transaction_timestamp = 1615818368,
                transaction_fee = cryptoapis.models.list_tokens_transfers_by_transaction_hash_ri_transaction_fee.ListTokensTransfersByTransactionHashRI_transactionFee(
                    amount = '0.0000051873', 
                    unit = 'ETH', ),
        )
        """

    def testListTokensTransfersByTransactionHashRI(self):
        """Test ListTokensTransfersByTransactionHashRI"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
