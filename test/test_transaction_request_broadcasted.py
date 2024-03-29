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
from cryptoapis.models.transaction_request_broadcasted import TransactionRequestBroadcasted  # noqa: E501
from cryptoapis.rest import ApiException

class TestTransactionRequestBroadcasted(unittest.TestCase):
    """TransactionRequestBroadcasted unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TransactionRequestBroadcasted
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TransactionRequestBroadcasted`
        """
        model = cryptoapis.models.transaction_request_broadcasted.TransactionRequestBroadcasted()  # noqa: E501
        if include_optional :
            return TransactionRequestBroadcasted(
                api_version = '2021-03-20', 
                reference_id = '6038d09050653d1f0e40584c', 
                idempotency_key = 'e55bf7a4a7188855f1c27541a6c387d04cc3b22ee34d1304b0e6ecad61c9906c', 
                data = cryptoapis.models.transaction_request_broadcasted_data.TransactionRequestBroadcasted_data(
                    product = 'WALLET_AS_A_SERVICE', 
                    event = 'TRANSACTION_REQUEST_BROADCASTED', 
                    item = cryptoapis.models.transaction_request_broadcasted_data_item.TransactionRequestBroadcasted_data_item(
                        blockchain = 'Bitcoin/Ethereum (whichever applicable)', 
                        network = 'Testnet/Mainnet (whichever applicable)', 
                        required_approvals = 5, 
                        required_rejections = 2, 
                        current_approvals = 2, 
                        current_rejections = 1, 
                        transaction_id = '4e78f606bc42534744e223f54b85d5bbd54a3949f54eb8fac31d73028c286e31', ), )
            )
        else :
            return TransactionRequestBroadcasted(
                api_version = '2021-03-20',
                reference_id = '6038d09050653d1f0e40584c',
                idempotency_key = 'e55bf7a4a7188855f1c27541a6c387d04cc3b22ee34d1304b0e6ecad61c9906c',
                data = cryptoapis.models.transaction_request_broadcasted_data.TransactionRequestBroadcasted_data(
                    product = 'WALLET_AS_A_SERVICE', 
                    event = 'TRANSACTION_REQUEST_BROADCASTED', 
                    item = cryptoapis.models.transaction_request_broadcasted_data_item.TransactionRequestBroadcasted_data_item(
                        blockchain = 'Bitcoin/Ethereum (whichever applicable)', 
                        network = 'Testnet/Mainnet (whichever applicable)', 
                        required_approvals = 5, 
                        required_rejections = 2, 
                        current_approvals = 2, 
                        current_rejections = 1, 
                        transaction_id = '4e78f606bc42534744e223f54b85d5bbd54a3949f54eb8fac31d73028c286e31', ), ),
        )
        """

    def testTransactionRequestBroadcasted(self):
        """Test TransactionRequestBroadcasted"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
