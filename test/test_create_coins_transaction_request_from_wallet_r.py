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
from cryptoapis.models.create_coins_transaction_request_from_wallet_r import CreateCoinsTransactionRequestFromWalletR  # noqa: E501
from cryptoapis.rest import ApiException

class TestCreateCoinsTransactionRequestFromWalletR(unittest.TestCase):
    """CreateCoinsTransactionRequestFromWalletR unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreateCoinsTransactionRequestFromWalletR
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateCoinsTransactionRequestFromWalletR`
        """
        model = cryptoapis.models.create_coins_transaction_request_from_wallet_r.CreateCoinsTransactionRequestFromWalletR()  # noqa: E501
        if include_optional :
            return CreateCoinsTransactionRequestFromWalletR(
                api_version = '2021-03-20', 
                request_id = '601c1710034ed6d407996b30', 
                context = 'yourExampleString', 
                data = cryptoapis.models.create_coins_transaction_request_from_wallet_r_data.CreateCoinsTransactionRequestFromWalletR_data(
                    item = cryptoapis.models.create_coins_transaction_request_from_wallet_ri.CreateCoinsTransactionRequestFromWalletRI(
                        callback_secret_key = 'yourSecretKey', 
                        callback_url = 'https://example.com', 
                        fee_priority = 'standard', 
                        note = 'yourAdditionalInformationhere', 
                        recipients = [
                            cryptoapis.models.create_coins_transaction_request_from_wallet_ri_recipients_inner.CreateCoinsTransactionRequestFromWalletRI_recipients_inner(
                                address = 'mmd963W1fECjLyaDCHcioSCZYHkRwjkhtr', 
                                amount = '0.00123', )
                            ], 
                        total_transaction_amount = '0.001', 
                        transaction_request_id = '6017dd02a309213863be9e55', 
                        transaction_request_status = 'created', ), )
            )
        else :
            return CreateCoinsTransactionRequestFromWalletR(
                api_version = '2021-03-20',
                request_id = '601c1710034ed6d407996b30',
                data = cryptoapis.models.create_coins_transaction_request_from_wallet_r_data.CreateCoinsTransactionRequestFromWalletR_data(
                    item = cryptoapis.models.create_coins_transaction_request_from_wallet_ri.CreateCoinsTransactionRequestFromWalletRI(
                        callback_secret_key = 'yourSecretKey', 
                        callback_url = 'https://example.com', 
                        fee_priority = 'standard', 
                        note = 'yourAdditionalInformationhere', 
                        recipients = [
                            cryptoapis.models.create_coins_transaction_request_from_wallet_ri_recipients_inner.CreateCoinsTransactionRequestFromWalletRI_recipients_inner(
                                address = 'mmd963W1fECjLyaDCHcioSCZYHkRwjkhtr', 
                                amount = '0.00123', )
                            ], 
                        total_transaction_amount = '0.001', 
                        transaction_request_id = '6017dd02a309213863be9e55', 
                        transaction_request_status = 'created', ), ),
        )
        """

    def testCreateCoinsTransactionRequestFromWalletR(self):
        """Test CreateCoinsTransactionRequestFromWalletR"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
