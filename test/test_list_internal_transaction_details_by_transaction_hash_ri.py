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
from cryptoapis.models.list_internal_transaction_details_by_transaction_hash_ri import ListInternalTransactionDetailsByTransactionHashRI  # noqa: E501
from cryptoapis.rest import ApiException

class TestListInternalTransactionDetailsByTransactionHashRI(unittest.TestCase):
    """ListInternalTransactionDetailsByTransactionHashRI unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ListInternalTransactionDetailsByTransactionHashRI
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListInternalTransactionDetailsByTransactionHashRI`
        """
        model = cryptoapis.models.list_internal_transaction_details_by_transaction_hash_ri.ListInternalTransactionDetailsByTransactionHashRI()  # noqa: E501
        if include_optional :
            return ListInternalTransactionDetailsByTransactionHashRI(
                amount = '0.089286906469667626', 
                block_hash = '0x47245a445acd6c7a328d033313ea621fbc0642aaf913790e9d558c1c208625f0', 
                block_height = 12561919, 
                operation_id = 'call_1', 
                operation_type = 'CALL', 
                parent_hash = '0x5d4ea0471b70de09fa3d6a4bc32f703ec44483bffa4d6169fa0a36c6a1dc108a', 
                recipient = '0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2', 
                sender = '0x7a250d5630b4cf539739df2c5dacb4c659f2488d', 
                timestamp = 1622728329
            )
        else :
            return ListInternalTransactionDetailsByTransactionHashRI(
                amount = '0.089286906469667626',
                block_hash = '0x47245a445acd6c7a328d033313ea621fbc0642aaf913790e9d558c1c208625f0',
                block_height = 12561919,
                operation_id = 'call_1',
                operation_type = 'CALL',
                parent_hash = '0x5d4ea0471b70de09fa3d6a4bc32f703ec44483bffa4d6169fa0a36c6a1dc108a',
                recipient = '0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2',
                sender = '0x7a250d5630b4cf539739df2c5dacb4c659f2488d',
                timestamp = 1622728329,
        )
        """

    def testListInternalTransactionDetailsByTransactionHashRI(self):
        """Test ListInternalTransactionDetailsByTransactionHashRI"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
