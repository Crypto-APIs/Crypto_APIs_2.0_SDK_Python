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
from cryptoapis.models.get_transaction_request_details_ri_recipients_inner import GetTransactionRequestDetailsRIRecipientsInner  # noqa: E501
from cryptoapis.rest import ApiException

class TestGetTransactionRequestDetailsRIRecipientsInner(unittest.TestCase):
    """GetTransactionRequestDetailsRIRecipientsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetTransactionRequestDetailsRIRecipientsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetTransactionRequestDetailsRIRecipientsInner`
        """
        model = cryptoapis.models.get_transaction_request_details_ri_recipients_inner.GetTransactionRequestDetailsRIRecipientsInner()  # noqa: E501
        if include_optional :
            return GetTransactionRequestDetailsRIRecipientsInner(
                address = 'mr3zKBc7skyDHcVHWww4JzzziPnrdYTscR', 
                address_tag = 3999472835, 
                amount = '0.001', 
                classic_address = 'rA9bXGJcXvZKaWofrRphdJsBWzhyCfH3z', 
                unit = 'BTC'
            )
        else :
            return GetTransactionRequestDetailsRIRecipientsInner(
                address = 'mr3zKBc7skyDHcVHWww4JzzziPnrdYTscR',
                amount = '0.001',
                unit = 'BTC',
        )
        """

    def testGetTransactionRequestDetailsRIRecipientsInner(self):
        """Test GetTransactionRequestDetailsRIRecipientsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
