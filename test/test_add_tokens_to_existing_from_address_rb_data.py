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
from cryptoapis.models.add_tokens_to_existing_from_address_rb_data import AddTokensToExistingFromAddressRBData  # noqa: E501
from cryptoapis.rest import ApiException

class TestAddTokensToExistingFromAddressRBData(unittest.TestCase):
    """AddTokensToExistingFromAddressRBData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AddTokensToExistingFromAddressRBData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AddTokensToExistingFromAddressRBData`
        """
        model = cryptoapis.models.add_tokens_to_existing_from_address_rb_data.AddTokensToExistingFromAddressRBData()  # noqa: E501
        if include_optional :
            return AddTokensToExistingFromAddressRBData(
                item = cryptoapis.models.add_tokens_to_existing_from_address_rb_data_item.AddTokensToExistingFromAddressRB_data_item(
                    callback_secret_key = 'yourSecretString', 
                    callback_url = 'https://example.com', 
                    confirmations_count = 3, 
                    fee_priority = 'standard', 
                    from_address = 'mizRduUBKEbJ6uzYJUegPh78gEGgM3WjAr', 
                    minimum_transfer_amount = '0.00001', 
                    to_address = 'mnumE76iEKN47bUsdni85oped5D1fRwKWi', 
                    token_data = cryptoapis.models.add_tokens_to_existing_from_address_rb_token_data.AddTokensToExistingFromAddressRBTokenData(), )
            )
        else :
            return AddTokensToExistingFromAddressRBData(
                item = cryptoapis.models.add_tokens_to_existing_from_address_rb_data_item.AddTokensToExistingFromAddressRB_data_item(
                    callback_secret_key = 'yourSecretString', 
                    callback_url = 'https://example.com', 
                    confirmations_count = 3, 
                    fee_priority = 'standard', 
                    from_address = 'mizRduUBKEbJ6uzYJUegPh78gEGgM3WjAr', 
                    minimum_transfer_amount = '0.00001', 
                    to_address = 'mnumE76iEKN47bUsdni85oped5D1fRwKWi', 
                    token_data = cryptoapis.models.add_tokens_to_existing_from_address_rb_token_data.AddTokensToExistingFromAddressRBTokenData(), ),
        )
        """

    def testAddTokensToExistingFromAddressRBData(self):
        """Test AddTokensToExistingFromAddressRBData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
