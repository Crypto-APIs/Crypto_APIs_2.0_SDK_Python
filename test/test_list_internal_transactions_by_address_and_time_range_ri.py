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
from cryptoapis.models.list_internal_transactions_by_address_and_time_range_ri import ListInternalTransactionsByAddressAndTimeRangeRI  # noqa: E501
from cryptoapis.rest import ApiException

class TestListInternalTransactionsByAddressAndTimeRangeRI(unittest.TestCase):
    """ListInternalTransactionsByAddressAndTimeRangeRI unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ListInternalTransactionsByAddressAndTimeRangeRI
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListInternalTransactionsByAddressAndTimeRangeRI`
        """
        model = cryptoapis.models.list_internal_transactions_by_address_and_time_range_ri.ListInternalTransactionsByAddressAndTimeRangeRI()  # noqa: E501
        if include_optional :
            return ListInternalTransactionsByAddressAndTimeRangeRI(
                amount = '0.089286906469667626', 
                mined_in_block_hash = '0x85ce0aa9628726c60db14526be8a2b823084b1f4c3dcccdc10b0235f23a49e66', 
                mined_in_block_height = 11135508, 
                operation_id = 'call_1', 
                operation_type = 'CALL', 
                parent_hash = '0x5d4ea0471b70de09fa3d6a4bc32f703ec44483bffa4d6169fa0a36c6a1dc108a', 
                recipient = '0xc6d46aba0c6e2eb6358c4e24804158cc4d847922', 
                sender = '0x0902a667d6a3f287835e0a4593cae4167384abc6', 
                timestamp = 1582202940
            )
        else :
            return ListInternalTransactionsByAddressAndTimeRangeRI(
                amount = '0.089286906469667626',
                mined_in_block_hash = '0x85ce0aa9628726c60db14526be8a2b823084b1f4c3dcccdc10b0235f23a49e66',
                mined_in_block_height = 11135508,
                operation_id = 'call_1',
                operation_type = 'CALL',
                parent_hash = '0x5d4ea0471b70de09fa3d6a4bc32f703ec44483bffa4d6169fa0a36c6a1dc108a',
                recipient = '0xc6d46aba0c6e2eb6358c4e24804158cc4d847922',
                sender = '0x0902a667d6a3f287835e0a4593cae4167384abc6',
                timestamp = 1582202940,
        )
        """

    def testListInternalTransactionsByAddressAndTimeRangeRI(self):
        """Test ListInternalTransactionsByAddressAndTimeRangeRI"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
