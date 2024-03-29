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
from cryptoapis.models.new_confirmed_internal_transactions_and_each_confirmation_r_data import NewConfirmedInternalTransactionsAndEachConfirmationRData  # noqa: E501
from cryptoapis.rest import ApiException

class TestNewConfirmedInternalTransactionsAndEachConfirmationRData(unittest.TestCase):
    """NewConfirmedInternalTransactionsAndEachConfirmationRData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test NewConfirmedInternalTransactionsAndEachConfirmationRData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NewConfirmedInternalTransactionsAndEachConfirmationRData`
        """
        model = cryptoapis.models.new_confirmed_internal_transactions_and_each_confirmation_r_data.NewConfirmedInternalTransactionsAndEachConfirmationRData()  # noqa: E501
        if include_optional :
            return NewConfirmedInternalTransactionsAndEachConfirmationRData(
                item = cryptoapis.models.new_confirmed_internal_transactions_and_each_confirmation_ri.NewConfirmedInternalTransactionsAndEachConfirmationRI(
                    address = '0xe2b5f5e885a268e4b6faae53f99a663f3bb3e036', 
                    callback_secret_key = 'yourSecretKey', 
                    callback_url = 'https://example.com', 
                    confirmations_count = 3, 
                    created_timestamp = 1611238648, 
                    event_type = 'ADDRESS_INTERNAL_TRANSACTION_CONFIRMED_EACH_CONFIRMATION', 
                    is_active = True, 
                    reference_id = 'bc243c86-0902-4386-b30d-e6b30fa1f2aa', )
            )
        else :
            return NewConfirmedInternalTransactionsAndEachConfirmationRData(
                item = cryptoapis.models.new_confirmed_internal_transactions_and_each_confirmation_ri.NewConfirmedInternalTransactionsAndEachConfirmationRI(
                    address = '0xe2b5f5e885a268e4b6faae53f99a663f3bb3e036', 
                    callback_secret_key = 'yourSecretKey', 
                    callback_url = 'https://example.com', 
                    confirmations_count = 3, 
                    created_timestamp = 1611238648, 
                    event_type = 'ADDRESS_INTERNAL_TRANSACTION_CONFIRMED_EACH_CONFIRMATION', 
                    is_active = True, 
                    reference_id = 'bc243c86-0902-4386-b30d-e6b30fa1f2aa', ),
        )
        """

    def testNewConfirmedInternalTransactionsAndEachConfirmationRData(self):
        """Test NewConfirmedInternalTransactionsAndEachConfirmationRData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
