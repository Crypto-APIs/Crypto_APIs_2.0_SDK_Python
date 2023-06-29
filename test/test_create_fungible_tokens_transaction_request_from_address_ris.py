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
from cryptoapis.models.create_fungible_tokens_transaction_request_from_address_ris import CreateFungibleTokensTransactionRequestFromAddressRIS  # noqa: E501
from cryptoapis.rest import ApiException

class TestCreateFungibleTokensTransactionRequestFromAddressRIS(unittest.TestCase):
    """CreateFungibleTokensTransactionRequestFromAddressRIS unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreateFungibleTokensTransactionRequestFromAddressRIS
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateFungibleTokensTransactionRequestFromAddressRIS`
        """
        model = cryptoapis.models.create_fungible_tokens_transaction_request_from_address_ris.CreateFungibleTokensTransactionRequestFromAddressRIS()  # noqa: E501
        if include_optional :
            return CreateFungibleTokensTransactionRequestFromAddressRIS(
                contract_address = '0x534bD102153EF199abAe8296a2FaE4599fC44Cdc'
            )
        else :
            return CreateFungibleTokensTransactionRequestFromAddressRIS(
                contract_address = '0x534bD102153EF199abAe8296a2FaE4599fC44Cdc',
        )
        """

    def testCreateFungibleTokensTransactionRequestFromAddressRIS(self):
        """Test CreateFungibleTokensTransactionRequestFromAddressRIS"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
