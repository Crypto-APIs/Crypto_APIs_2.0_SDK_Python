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
from cryptoapis.models.create_automatic_tokens_forwarding_ri import CreateAutomaticTokensForwardingRI  # noqa: E501
from cryptoapis.rest import ApiException

class TestCreateAutomaticTokensForwardingRI(unittest.TestCase):
    """CreateAutomaticTokensForwardingRI unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreateAutomaticTokensForwardingRI
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateAutomaticTokensForwardingRI`
        """
        model = cryptoapis.models.create_automatic_tokens_forwarding_ri.CreateAutomaticTokensForwardingRI()  # noqa: E501
        if include_optional :
            return CreateAutomaticTokensForwardingRI(
                callback_url = 'https://example.com', 
                confirmations_count = 2, 
                created_timestamp = 1611238648, 
                fee_address = 'mojjR51gMXLJ4B3SBPhEXXRFDX7U5UWXNQ', 
                fee_priority = 'standard', 
                from_address = 'ms4KNsbNpoU8g424pzmEjbkFbfAHae1msB', 
                minimum_transfer_amount = '0.5', 
                reference_id = '6017dd02a309213863be9e55', 
                to_address = 'tb1q54j7qcu7kgsrx87yn0r9zjdvsxrnvxg4qua2z6', 
                token_data = cryptoapis.models.create_automatic_tokens_forwarding_rits.CreateAutomaticTokensForwardingRITS()
            )
        else :
            return CreateAutomaticTokensForwardingRI(
                callback_url = 'https://example.com',
                confirmations_count = 2,
                created_timestamp = 1611238648,
                fee_address = 'mojjR51gMXLJ4B3SBPhEXXRFDX7U5UWXNQ',
                fee_priority = 'standard',
                from_address = 'ms4KNsbNpoU8g424pzmEjbkFbfAHae1msB',
                minimum_transfer_amount = '0.5',
                reference_id = '6017dd02a309213863be9e55',
                to_address = 'tb1q54j7qcu7kgsrx87yn0r9zjdvsxrnvxg4qua2z6',
                token_data = cryptoapis.models.create_automatic_tokens_forwarding_rits.CreateAutomaticTokensForwardingRITS(),
        )
        """

    def testCreateAutomaticTokensForwardingRI(self):
        """Test CreateAutomaticTokensForwardingRI"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
