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
from cryptoapis.models.address_tokens_transaction_confirmed_erc721 import AddressTokensTransactionConfirmedErc721  # noqa: E501
from cryptoapis.rest import ApiException

class TestAddressTokensTransactionConfirmedErc721(unittest.TestCase):
    """AddressTokensTransactionConfirmedErc721 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AddressTokensTransactionConfirmedErc721
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AddressTokensTransactionConfirmedErc721`
        """
        model = cryptoapis.models.address_tokens_transaction_confirmed_erc721.AddressTokensTransactionConfirmedErc721()  # noqa: E501
        if include_optional :
            return AddressTokensTransactionConfirmedErc721(
                name = 'Wonky Stonks', 
                symbol = 'WSTK', 
                token_id = '000000000000000000000000dac17f958d2ee523a2206206994597c13d831ec7', 
                contract_address = '0x518ba36f1ca6dfe3bb1b098b8dd0444030e79d9f'
            )
        else :
            return AddressTokensTransactionConfirmedErc721(
                name = 'Wonky Stonks',
                symbol = 'WSTK',
                token_id = '000000000000000000000000dac17f958d2ee523a2206206994597c13d831ec7',
                contract_address = '0x518ba36f1ca6dfe3bb1b098b8dd0444030e79d9f',
        )
        """

    def testAddressTokensTransactionConfirmedErc721(self):
        """Test AddressTokensTransactionConfirmedErc721"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
