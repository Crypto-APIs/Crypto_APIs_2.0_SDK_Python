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
from cryptoapis.models.get_internal_transaction_by_transaction_hash_and_operation_id_e403 import GetInternalTransactionByTransactionHashAndOperationIdE403  # noqa: E501
from cryptoapis.rest import ApiException

class TestGetInternalTransactionByTransactionHashAndOperationIdE403(unittest.TestCase):
    """GetInternalTransactionByTransactionHashAndOperationIdE403 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetInternalTransactionByTransactionHashAndOperationIdE403
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetInternalTransactionByTransactionHashAndOperationIdE403`
        """
        model = cryptoapis.models.get_internal_transaction_by_transaction_hash_and_operation_id_e403.GetInternalTransactionByTransactionHashAndOperationIdE403()  # noqa: E501
        if include_optional :
            return GetInternalTransactionByTransactionHashAndOperationIdE403(
                code = 'feature_mainnets_not_allowed_for_plan', 
                message = 'Mainnets access is not available for your current subscription plan, please upgrade your plan to be able to use it.', 
                details = [
                    cryptoapis.models.banned_ip_address_details_inner.BannedIpAddress_details_inner(
                        attribute = 'attribute which content caused the error', 
                        message = 'message describing the error', )
                    ]
            )
        else :
            return GetInternalTransactionByTransactionHashAndOperationIdE403(
                code = 'feature_mainnets_not_allowed_for_plan',
                message = 'Mainnets access is not available for your current subscription plan, please upgrade your plan to be able to use it.',
        )
        """

    def testGetInternalTransactionByTransactionHashAndOperationIdE403(self):
        """Test GetInternalTransactionByTransactionHashAndOperationIdE403"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
