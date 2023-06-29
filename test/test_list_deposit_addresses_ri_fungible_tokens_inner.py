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
from cryptoapis.models.list_deposit_addresses_ri_fungible_tokens_inner import ListDepositAddressesRIFungibleTokensInner  # noqa: E501
from cryptoapis.rest import ApiException

class TestListDepositAddressesRIFungibleTokensInner(unittest.TestCase):
    """ListDepositAddressesRIFungibleTokensInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ListDepositAddressesRIFungibleTokensInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListDepositAddressesRIFungibleTokensInner`
        """
        model = cryptoapis.models.list_deposit_addresses_ri_fungible_tokens_inner.ListDepositAddressesRIFungibleTokensInner()  # noqa: E501
        if include_optional :
            return ListDepositAddressesRIFungibleTokensInner(
                amount = '0.254', 
                identifier = '0xdac17f958d2ee523a2206206994597c13d831ec7', 
                name = 'Tether USD', 
                symbol = 'USDT', 
                token_decimals = 6, 
                type = 'ERC-20'
            )
        else :
            return ListDepositAddressesRIFungibleTokensInner(
                amount = '0.254',
                identifier = '0xdac17f958d2ee523a2206206994597c13d831ec7',
                name = 'Tether USD',
                symbol = 'USDT',
                token_decimals = 6,
                type = 'ERC-20',
        )
        """

    def testListDepositAddressesRIFungibleTokensInner(self):
        """Test ListDepositAddressesRIFungibleTokensInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
