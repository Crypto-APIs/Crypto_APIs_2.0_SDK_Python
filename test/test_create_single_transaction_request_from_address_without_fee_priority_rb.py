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
from cryptoapis.models.create_single_transaction_request_from_address_without_fee_priority_rb import CreateSingleTransactionRequestFromAddressWithoutFeePriorityRB  # noqa: E501
from cryptoapis.rest import ApiException

class TestCreateSingleTransactionRequestFromAddressWithoutFeePriorityRB(unittest.TestCase):
    """CreateSingleTransactionRequestFromAddressWithoutFeePriorityRB unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreateSingleTransactionRequestFromAddressWithoutFeePriorityRB
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateSingleTransactionRequestFromAddressWithoutFeePriorityRB`
        """
        model = cryptoapis.models.create_single_transaction_request_from_address_without_fee_priority_rb.CreateSingleTransactionRequestFromAddressWithoutFeePriorityRB()  # noqa: E501
        if include_optional :
            return CreateSingleTransactionRequestFromAddressWithoutFeePriorityRB(
                context = 'yourExampleString', 
                data = cryptoapis.models.create_single_transaction_request_from_address_without_fee_priority_rb_data.CreateSingleTransactionRequestFromAddressWithoutFeePriorityRB_data(
                    item = cryptoapis.models.create_single_transaction_request_from_address_without_fee_priority_rb_data_item.CreateSingleTransactionRequestFromAddressWithoutFeePriorityRB_data_item(
                        amount = '0.0006', 
                        callback_secret_key = 'yourSecretKey', 
                        callback_url = 'https://example.com', 
                        note = 'yourAdditionalInformationhere', 
                        recipient_address = 'TMVeigwYyuXJVHER4oA2yQzsFFSN2JfXkt', ), )
            )
        else :
            return CreateSingleTransactionRequestFromAddressWithoutFeePriorityRB(
                data = cryptoapis.models.create_single_transaction_request_from_address_without_fee_priority_rb_data.CreateSingleTransactionRequestFromAddressWithoutFeePriorityRB_data(
                    item = cryptoapis.models.create_single_transaction_request_from_address_without_fee_priority_rb_data_item.CreateSingleTransactionRequestFromAddressWithoutFeePriorityRB_data_item(
                        amount = '0.0006', 
                        callback_secret_key = 'yourSecretKey', 
                        callback_url = 'https://example.com', 
                        note = 'yourAdditionalInformationhere', 
                        recipient_address = 'TMVeigwYyuXJVHER4oA2yQzsFFSN2JfXkt', ), ),
        )
        """

    def testCreateSingleTransactionRequestFromAddressWithoutFeePriorityRB(self):
        """Test CreateSingleTransactionRequestFromAddressWithoutFeePriorityRB"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()