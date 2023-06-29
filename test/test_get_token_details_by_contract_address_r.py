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
from cryptoapis.models.get_token_details_by_contract_address_r import GetTokenDetailsByContractAddressR  # noqa: E501
from cryptoapis.rest import ApiException

class TestGetTokenDetailsByContractAddressR(unittest.TestCase):
    """GetTokenDetailsByContractAddressR unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetTokenDetailsByContractAddressR
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetTokenDetailsByContractAddressR`
        """
        model = cryptoapis.models.get_token_details_by_contract_address_r.GetTokenDetailsByContractAddressR()  # noqa: E501
        if include_optional :
            return GetTokenDetailsByContractAddressR(
                api_version = '2021-03-20', 
                request_id = '601c1710034ed6d407996b30', 
                context = 'yourExampleString', 
                data = cryptoapis.models.get_token_details_by_contract_address_r_data.GetTokenDetailsByContractAddressR_data(
                    item = cryptoapis.models.get_token_details_by_contract_address_ri.GetTokenDetailsByContractAddressRI(
                        token_decimals = '18', 
                        token_name = 'Band Protocol', 
                        token_symbol = 'BAND', 
                        token_type = 'ERC-20', 
                        total_supply = '1000000', ), )
            )
        else :
            return GetTokenDetailsByContractAddressR(
                api_version = '2021-03-20',
                request_id = '601c1710034ed6d407996b30',
                data = cryptoapis.models.get_token_details_by_contract_address_r_data.GetTokenDetailsByContractAddressR_data(
                    item = cryptoapis.models.get_token_details_by_contract_address_ri.GetTokenDetailsByContractAddressRI(
                        token_decimals = '18', 
                        token_name = 'Band Protocol', 
                        token_symbol = 'BAND', 
                        token_type = 'ERC-20', 
                        total_supply = '1000000', ), ),
        )
        """

    def testGetTokenDetailsByContractAddressR(self):
        """Test GetTokenDetailsByContractAddressR"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
