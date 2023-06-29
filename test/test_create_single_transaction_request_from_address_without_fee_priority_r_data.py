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
from cryptoapis.models.create_single_transaction_request_from_address_without_fee_priority_r_data import CreateSingleTransactionRequestFromAddressWithoutFeePriorityRData  # noqa: E501
from cryptoapis.rest import ApiException

class TestCreateSingleTransactionRequestFromAddressWithoutFeePriorityRData(unittest.TestCase):
    """CreateSingleTransactionRequestFromAddressWithoutFeePriorityRData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreateSingleTransactionRequestFromAddressWithoutFeePriorityRData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateSingleTransactionRequestFromAddressWithoutFeePriorityRData`
        """
        model = cryptoapis.models.create_single_transaction_request_from_address_without_fee_priority_r_data.CreateSingleTransactionRequestFromAddressWithoutFeePriorityRData()  # noqa: E501
        if include_optional :
            return CreateSingleTransactionRequestFromAddressWithoutFeePriorityRData(
                item = cryptoapis.models.create_single_transaction_request_from_address_without_fee_priority_ri.CreateSingleTransactionRequestFromAddressWithoutFeePriorityRI(
                    callback_secret_key = 'yourSecretString', 
                    callback_url = 'https://example.com', 
                    classic_address = 'TX8VXpdEoNNrKeEuNTfbEXfa9eZivcyUwD', 
                    note = 'yourAdditionalInformationhere', 
                    recipient = [
                        cryptoapis.models.create_single_transaction_request_from_address_without_fee_priority_ri_recipient_inner.CreateSingleTransactionRequestFromAddressWithoutFeePriorityRI_recipient_inner(
                            address = 'TX8VXpdEoNNrKeEuNTfbEXfa9eZivcyUwD', 
                            amount = '0.0006', 
                            classic_address = 'TMVeigwYyuXJVHER4oA2yQzsFFSN2JfXkt', 
                            unit = 'TRX', )
                        ], 
                    sender = cryptoapis.models.create_single_transaction_request_from_address_without_fee_priority_ri_sender.CreateSingleTransactionRequestFromAddressWithoutFeePriorityRI_sender(
                        address = 'TX8VXpdEoNNrKeEuNTfbEXfa9eZivcyUwD', ), 
                    transaction_request_id = '62da9f003d20a65c737af83f', 
                    transaction_request_status = 'created', 
                    total_amount = cryptoapis.models.create_single_transaction_request_from_address_without_fee_priority_ri_total_amount.CreateSingleTransactionRequestFromAddressWithoutFeePriorityRI_totalAmount(
                        unit = 'TRX', 
                        value = '0.0006', ), )
            )
        else :
            return CreateSingleTransactionRequestFromAddressWithoutFeePriorityRData(
                item = cryptoapis.models.create_single_transaction_request_from_address_without_fee_priority_ri.CreateSingleTransactionRequestFromAddressWithoutFeePriorityRI(
                    callback_secret_key = 'yourSecretString', 
                    callback_url = 'https://example.com', 
                    classic_address = 'TX8VXpdEoNNrKeEuNTfbEXfa9eZivcyUwD', 
                    note = 'yourAdditionalInformationhere', 
                    recipient = [
                        cryptoapis.models.create_single_transaction_request_from_address_without_fee_priority_ri_recipient_inner.CreateSingleTransactionRequestFromAddressWithoutFeePriorityRI_recipient_inner(
                            address = 'TX8VXpdEoNNrKeEuNTfbEXfa9eZivcyUwD', 
                            amount = '0.0006', 
                            classic_address = 'TMVeigwYyuXJVHER4oA2yQzsFFSN2JfXkt', 
                            unit = 'TRX', )
                        ], 
                    sender = cryptoapis.models.create_single_transaction_request_from_address_without_fee_priority_ri_sender.CreateSingleTransactionRequestFromAddressWithoutFeePriorityRI_sender(
                        address = 'TX8VXpdEoNNrKeEuNTfbEXfa9eZivcyUwD', ), 
                    transaction_request_id = '62da9f003d20a65c737af83f', 
                    transaction_request_status = 'created', 
                    total_amount = cryptoapis.models.create_single_transaction_request_from_address_without_fee_priority_ri_total_amount.CreateSingleTransactionRequestFromAddressWithoutFeePriorityRI_totalAmount(
                        unit = 'TRX', 
                        value = '0.0006', ), ),
        )
        """

    def testCreateSingleTransactionRequestFromAddressWithoutFeePriorityRData(self):
        """Test CreateSingleTransactionRequestFromAddressWithoutFeePriorityRData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
