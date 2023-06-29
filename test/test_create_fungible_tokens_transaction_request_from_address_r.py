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
from cryptoapis.models.create_fungible_tokens_transaction_request_from_address_r import CreateFungibleTokensTransactionRequestFromAddressR  # noqa: E501
from cryptoapis.rest import ApiException

class TestCreateFungibleTokensTransactionRequestFromAddressR(unittest.TestCase):
    """CreateFungibleTokensTransactionRequestFromAddressR unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreateFungibleTokensTransactionRequestFromAddressR
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateFungibleTokensTransactionRequestFromAddressR`
        """
        model = cryptoapis.models.create_fungible_tokens_transaction_request_from_address_r.CreateFungibleTokensTransactionRequestFromAddressR()  # noqa: E501
        if include_optional :
            return CreateFungibleTokensTransactionRequestFromAddressR(
                api_version = '2021-03-20', 
                request_id = '601c1710034ed6d407996b30', 
                context = 'yourExampleString', 
                data = cryptoapis.models.create_fungible_tokens_transaction_request_from_address_r_data.CreateFungibleTokensTransactionRequestFromAddressR_data(
                    item = cryptoapis.models.create_fungible_tokens_transaction_request_from_address_ri.CreateFungibleTokensTransactionRequestFromAddressRI(
                        callback_secret_key = 'yourSecretString', 
                        callback_url = 'https://example.com', 
                        fee_priority = 'fast', 
                        note = 'yourAdditionalInformationhere', 
                        recipients = 0x1316bea88fb7cd4ccc4a57e2f9f4f43d1a86ee59, 
                        senders = cryptoapis.models.create_coins_transaction_request_from_address_ri_senders.CreateCoinsTransactionRequestFromAddressRI_senders(
                            address = '0x0902a667d6a3f287835e0a4593cae4167384abc6', ), 
                        token_type_specific_data = cryptoapis.models.create_fungible_tokens_transaction_request_from_address_ris.CreateFungibleTokensTransactionRequestFromAddressRIS(), 
                        transaction_request_id = '6038d09050653d1f0e40584c', ), )
            )
        else :
            return CreateFungibleTokensTransactionRequestFromAddressR(
                api_version = '2021-03-20',
                request_id = '601c1710034ed6d407996b30',
                data = cryptoapis.models.create_fungible_tokens_transaction_request_from_address_r_data.CreateFungibleTokensTransactionRequestFromAddressR_data(
                    item = cryptoapis.models.create_fungible_tokens_transaction_request_from_address_ri.CreateFungibleTokensTransactionRequestFromAddressRI(
                        callback_secret_key = 'yourSecretString', 
                        callback_url = 'https://example.com', 
                        fee_priority = 'fast', 
                        note = 'yourAdditionalInformationhere', 
                        recipients = 0x1316bea88fb7cd4ccc4a57e2f9f4f43d1a86ee59, 
                        senders = cryptoapis.models.create_coins_transaction_request_from_address_ri_senders.CreateCoinsTransactionRequestFromAddressRI_senders(
                            address = '0x0902a667d6a3f287835e0a4593cae4167384abc6', ), 
                        token_type_specific_data = cryptoapis.models.create_fungible_tokens_transaction_request_from_address_ris.CreateFungibleTokensTransactionRequestFromAddressRIS(), 
                        transaction_request_id = '6038d09050653d1f0e40584c', ), ),
        )
        """

    def testCreateFungibleTokensTransactionRequestFromAddressR(self):
        """Test CreateFungibleTokensTransactionRequestFromAddressR"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
