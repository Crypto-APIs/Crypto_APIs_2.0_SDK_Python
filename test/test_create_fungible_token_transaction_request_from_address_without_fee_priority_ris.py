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
from cryptoapis.models.create_fungible_token_transaction_request_from_address_without_fee_priority_ris import CreateFungibleTokenTransactionRequestFromAddressWithoutFeePriorityRIS  # noqa: E501
from cryptoapis.rest import ApiException

class TestCreateFungibleTokenTransactionRequestFromAddressWithoutFeePriorityRIS(unittest.TestCase):
    """CreateFungibleTokenTransactionRequestFromAddressWithoutFeePriorityRIS unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreateFungibleTokenTransactionRequestFromAddressWithoutFeePriorityRIS
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateFungibleTokenTransactionRequestFromAddressWithoutFeePriorityRIS`
        """
        model = cryptoapis.models.create_fungible_token_transaction_request_from_address_without_fee_priority_ris.CreateFungibleTokenTransactionRequestFromAddressWithoutFeePriorityRIS()  # noqa: E501
        if include_optional :
            return CreateFungibleTokenTransactionRequestFromAddressWithoutFeePriorityRIS(
                contract_address = 'TF17BgPaZYbz8oxbjhriubPDsA7ArKoLX3', 
                fee_limit = '1000000000', 
                symbol = 'JST'
            )
        else :
            return CreateFungibleTokenTransactionRequestFromAddressWithoutFeePriorityRIS(
                contract_address = 'TF17BgPaZYbz8oxbjhriubPDsA7ArKoLX3',
                fee_limit = '1000000000',
                symbol = 'JST',
        )
        """

    def testCreateFungibleTokenTransactionRequestFromAddressWithoutFeePriorityRIS(self):
        """Test CreateFungibleTokenTransactionRequestFromAddressWithoutFeePriorityRIS"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
