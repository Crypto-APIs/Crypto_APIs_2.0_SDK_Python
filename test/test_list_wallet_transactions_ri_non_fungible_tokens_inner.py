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
from cryptoapis.models.list_wallet_transactions_ri_non_fungible_tokens_inner import ListWalletTransactionsRINonFungibleTokensInner  # noqa: E501
from cryptoapis.rest import ApiException

class TestListWalletTransactionsRINonFungibleTokensInner(unittest.TestCase):
    """ListWalletTransactionsRINonFungibleTokensInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ListWalletTransactionsRINonFungibleTokensInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListWalletTransactionsRINonFungibleTokensInner`
        """
        model = cryptoapis.models.list_wallet_transactions_ri_non_fungible_tokens_inner.ListWalletTransactionsRINonFungibleTokensInner()  # noqa: E501
        if include_optional :
            return ListWalletTransactionsRINonFungibleTokensInner(
                converted_amount = '0.034', 
                exchange_rate_unit = 'USD', 
                name = 'Axie Infinity', 
                recipient = '0xdac17f958d2ee523a2206206994597c13d831ec7', 
                sender = '0x65b895f400dae5541d70cbbec07527210158f6e2', 
                symbol = 'AXS', 
                token_id = '13383', 
                type = 'ERC-721'
            )
        else :
            return ListWalletTransactionsRINonFungibleTokensInner(
                converted_amount = '0.034',
                exchange_rate_unit = 'USD',
                name = 'Axie Infinity',
                recipient = '0xdac17f958d2ee523a2206206994597c13d831ec7',
                sender = '0x65b895f400dae5541d70cbbec07527210158f6e2',
                symbol = 'AXS',
                token_id = '13383',
                type = 'ERC-721',
        )
        """

    def testListWalletTransactionsRINonFungibleTokensInner(self):
        """Test ListWalletTransactionsRINonFungibleTokensInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
