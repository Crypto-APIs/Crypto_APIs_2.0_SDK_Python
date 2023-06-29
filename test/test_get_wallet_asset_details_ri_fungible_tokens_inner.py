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
from cryptoapis.models.get_wallet_asset_details_ri_fungible_tokens_inner import GetWalletAssetDetailsRIFungibleTokensInner  # noqa: E501
from cryptoapis.rest import ApiException

class TestGetWalletAssetDetailsRIFungibleTokensInner(unittest.TestCase):
    """GetWalletAssetDetailsRIFungibleTokensInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetWalletAssetDetailsRIFungibleTokensInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetWalletAssetDetailsRIFungibleTokensInner`
        """
        model = cryptoapis.models.get_wallet_asset_details_ri_fungible_tokens_inner.GetWalletAssetDetailsRIFungibleTokensInner()  # noqa: E501
        if include_optional :
            return GetWalletAssetDetailsRIFungibleTokensInner(
                confirmed_amount = '0.254', 
                identifier = '0xdac17f958d2ee523a2206206994597c13d831ec7', 
                symbol = 'USDT', 
                type = 'ERC-20'
            )
        else :
            return GetWalletAssetDetailsRIFungibleTokensInner(
                confirmed_amount = '0.254',
                identifier = '0xdac17f958d2ee523a2206206994597c13d831ec7',
                symbol = 'USDT',
                type = 'ERC-20',
        )
        """

    def testGetWalletAssetDetailsRIFungibleTokensInner(self):
        """Test GetWalletAssetDetailsRIFungibleTokensInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()