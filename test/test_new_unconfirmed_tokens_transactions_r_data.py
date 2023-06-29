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
from cryptoapis.models.new_unconfirmed_tokens_transactions_r_data import NewUnconfirmedTokensTransactionsRData  # noqa: E501
from cryptoapis.rest import ApiException

class TestNewUnconfirmedTokensTransactionsRData(unittest.TestCase):
    """NewUnconfirmedTokensTransactionsRData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test NewUnconfirmedTokensTransactionsRData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NewUnconfirmedTokensTransactionsRData`
        """
        model = cryptoapis.models.new_unconfirmed_tokens_transactions_r_data.NewUnconfirmedTokensTransactionsRData()  # noqa: E501
        if include_optional :
            return NewUnconfirmedTokensTransactionsRData(
                item = cryptoapis.models.new_unconfirmed_tokens_transactions_ri.NewUnconfirmedTokensTransactionsRI(
                    address = '0x65b895f400dae5541d70cbbec07527210158f6e2', 
                    callback_secret_key = 'yourSecretKey', 
                    callback_url = 'https://example.com', 
                    created_timestamp = 1611238648, 
                    event_type = 'ADDRESS_TOKENS_TRANSACTION_UNCONFIRMED', 
                    is_active = True, 
                    reference_id = 'c748624f-1843-4738-a7de-8258ada0f524', )
            )
        else :
            return NewUnconfirmedTokensTransactionsRData(
                item = cryptoapis.models.new_unconfirmed_tokens_transactions_ri.NewUnconfirmedTokensTransactionsRI(
                    address = '0x65b895f400dae5541d70cbbec07527210158f6e2', 
                    callback_secret_key = 'yourSecretKey', 
                    callback_url = 'https://example.com', 
                    created_timestamp = 1611238648, 
                    event_type = 'ADDRESS_TOKENS_TRANSACTION_UNCONFIRMED', 
                    is_active = True, 
                    reference_id = 'c748624f-1843-4738-a7de-8258ada0f524', ),
        )
        """

    def testNewUnconfirmedTokensTransactionsRData(self):
        """Test NewUnconfirmedTokensTransactionsRData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
