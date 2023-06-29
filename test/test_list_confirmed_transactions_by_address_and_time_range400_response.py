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
from cryptoapis.models.list_confirmed_transactions_by_address_and_time_range400_response import ListConfirmedTransactionsByAddressAndTimeRange400Response  # noqa: E501
from cryptoapis.rest import ApiException

class TestListConfirmedTransactionsByAddressAndTimeRange400Response(unittest.TestCase):
    """ListConfirmedTransactionsByAddressAndTimeRange400Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ListConfirmedTransactionsByAddressAndTimeRange400Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListConfirmedTransactionsByAddressAndTimeRange400Response`
        """
        model = cryptoapis.models.list_confirmed_transactions_by_address_and_time_range400_response.ListConfirmedTransactionsByAddressAndTimeRange400Response()  # noqa: E501
        if include_optional :
            return ListConfirmedTransactionsByAddressAndTimeRange400Response(
                api_version = '2021-03-20', 
                request_id = '601c1710034ed6d407996b30', 
                context = 'yourExampleString', 
                error = cryptoapis.models.list_confirmed_transactions_by_address_and_time_range_e400.ListConfirmedTransactionsByAddressAndTimeRangeE400()
            )
        else :
            return ListConfirmedTransactionsByAddressAndTimeRange400Response(
                api_version = '2021-03-20',
                request_id = '601c1710034ed6d407996b30',
                error = cryptoapis.models.list_confirmed_transactions_by_address_and_time_range_e400.ListConfirmedTransactionsByAddressAndTimeRangeE400(),
        )
        """

    def testListConfirmedTransactionsByAddressAndTimeRange400Response(self):
        """Test ListConfirmedTransactionsByAddressAndTimeRange400Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
