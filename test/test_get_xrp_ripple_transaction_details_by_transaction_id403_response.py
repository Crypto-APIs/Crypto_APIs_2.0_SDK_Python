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
from cryptoapis.models.get_xrp_ripple_transaction_details_by_transaction_id403_response import GetXRPRippleTransactionDetailsByTransactionID403Response  # noqa: E501
from cryptoapis.rest import ApiException

class TestGetXRPRippleTransactionDetailsByTransactionID403Response(unittest.TestCase):
    """GetXRPRippleTransactionDetailsByTransactionID403Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetXRPRippleTransactionDetailsByTransactionID403Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetXRPRippleTransactionDetailsByTransactionID403Response`
        """
        model = cryptoapis.models.get_xrp_ripple_transaction_details_by_transaction_id403_response.GetXRPRippleTransactionDetailsByTransactionID403Response()  # noqa: E501
        if include_optional :
            return GetXRPRippleTransactionDetailsByTransactionID403Response(
                api_version = '2021-03-20', 
                request_id = '601c1710034ed6d407996b30', 
                context = 'yourExampleString', 
                error = cryptoapis.models.get_xrp_ripple_transaction_details_by_transaction_ide403.GetXRPRippleTransactionDetailsByTransactionIDE403()
            )
        else :
            return GetXRPRippleTransactionDetailsByTransactionID403Response(
                api_version = '2021-03-20',
                request_id = '601c1710034ed6d407996b30',
                error = cryptoapis.models.get_xrp_ripple_transaction_details_by_transaction_ide403.GetXRPRippleTransactionDetailsByTransactionIDE403(),
        )
        """

    def testGetXRPRippleTransactionDetailsByTransactionID403Response(self):
        """Test GetXRPRippleTransactionDetailsByTransactionID403Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
