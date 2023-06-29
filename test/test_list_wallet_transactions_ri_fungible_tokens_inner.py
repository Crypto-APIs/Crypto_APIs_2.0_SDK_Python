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
from cryptoapis.models.list_wallet_transactions_ri_fungible_tokens_inner import ListWalletTransactionsRIFungibleTokensInner  # noqa: E501
from cryptoapis.rest import ApiException

class TestListWalletTransactionsRIFungibleTokensInner(unittest.TestCase):
    """ListWalletTransactionsRIFungibleTokensInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ListWalletTransactionsRIFungibleTokensInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListWalletTransactionsRIFungibleTokensInner`
        """
        model = cryptoapis.models.list_wallet_transactions_ri_fungible_tokens_inner.ListWalletTransactionsRIFungibleTokensInner()  # noqa: E501
        if include_optional :
            return ListWalletTransactionsRIFungibleTokensInner(
                amount = '0.254', 
                converted_amount = '0.0034', 
                exchange_rate_unit = 'USD', 
                name = 'Tether USD', 
                recipient = '0x229f7172eab232d09d2de05a3e3b7b79c9abfe3b', 
                sender = '0x1b7aa44088a0ea95bdc65fef6e5071e946bf7d8f', 
                symbol = 'ETH', 
                token_decimals = 6, 
                type = 'ERC-20'
            )
        else :
            return ListWalletTransactionsRIFungibleTokensInner(
                amount = '0.254',
                converted_amount = '0.0034',
                exchange_rate_unit = 'USD',
                name = 'Tether USD',
                recipient = '0x229f7172eab232d09d2de05a3e3b7b79c9abfe3b',
                sender = '0x1b7aa44088a0ea95bdc65fef6e5071e946bf7d8f',
                symbol = 'ETH',
                token_decimals = 6,
                type = 'ERC-20',
        )
        """

    def testListWalletTransactionsRIFungibleTokensInner(self):
        """Test ListWalletTransactionsRIFungibleTokensInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()