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
from cryptoapis.models.list_confirmed_transactions_by_address_ribst2 import ListConfirmedTransactionsByAddressRIBST2  # noqa: E501
from cryptoapis.rest import ApiException

class TestListConfirmedTransactionsByAddressRIBST2(unittest.TestCase):
    """ListConfirmedTransactionsByAddressRIBST2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ListConfirmedTransactionsByAddressRIBST2
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListConfirmedTransactionsByAddressRIBST2`
        """
        model = cryptoapis.models.list_confirmed_transactions_by_address_ribst2.ListConfirmedTransactionsByAddressRIBST2()  # noqa: E501
        if include_optional :
            return ListConfirmedTransactionsByAddressRIBST2(
                addresses = [
                    'tz1arY7HNDq17nrZJ7f3sikxuHZgeopsU9xq'
                    ], 
                counter = 392812, 
                gas_limit = '1081', 
                gas_used = '1001', 
                has_internal_transactions = False, 
                is_confirmed = True, 
                nonce = 1, 
                token_transfers_count = 0, 
                transaction_status = 'applied'
            )
        else :
            return ListConfirmedTransactionsByAddressRIBST2(
                addresses = [
                    'tz1arY7HNDq17nrZJ7f3sikxuHZgeopsU9xq'
                    ],
                counter = 392812,
                gas_limit = '1081',
                gas_used = '1001',
                has_internal_transactions = False,
                is_confirmed = True,
                token_transfers_count = 0,
                transaction_status = 'applied',
        )
        """

    def testListConfirmedTransactionsByAddressRIBST2(self):
        """Test ListConfirmedTransactionsByAddressRIBST2"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()