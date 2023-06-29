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
from cryptoapis.models.get_wallet_asset_details_ri_non_fungible_tokens_inner import GetWalletAssetDetailsRINonFungibleTokensInner  # noqa: E501
from cryptoapis.rest import ApiException

class TestGetWalletAssetDetailsRINonFungibleTokensInner(unittest.TestCase):
    """GetWalletAssetDetailsRINonFungibleTokensInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetWalletAssetDetailsRINonFungibleTokensInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetWalletAssetDetailsRINonFungibleTokensInner`
        """
        model = cryptoapis.models.get_wallet_asset_details_ri_non_fungible_tokens_inner.GetWalletAssetDetailsRINonFungibleTokensInner()  # noqa: E501
        if include_optional :
            return GetWalletAssetDetailsRINonFungibleTokensInner(
                identifier = '0x90ca8a3eb2574f937f514749ce619fdcca187d45', 
                symbol = 'ENS', 
                token_id = '0x000000000000000000000000000000000000000000000000000000000000195b', 
                type = 'ERC-721'
            )
        else :
            return GetWalletAssetDetailsRINonFungibleTokensInner(
                identifier = '0x90ca8a3eb2574f937f514749ce619fdcca187d45',
                symbol = 'ENS',
                token_id = '0x000000000000000000000000000000000000000000000000000000000000195b',
                type = 'ERC-721',
        )
        """

    def testGetWalletAssetDetailsRINonFungibleTokensInner(self):
        """Test GetWalletAssetDetailsRINonFungibleTokensInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
