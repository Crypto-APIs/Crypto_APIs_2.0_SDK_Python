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
from cryptoapis.models.prepare_transaction_from_address_rb_data import PrepareTransactionFromAddressRBData  # noqa: E501
from cryptoapis.rest import ApiException

class TestPrepareTransactionFromAddressRBData(unittest.TestCase):
    """PrepareTransactionFromAddressRBData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PrepareTransactionFromAddressRBData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PrepareTransactionFromAddressRBData`
        """
        model = cryptoapis.models.prepare_transaction_from_address_rb_data.PrepareTransactionFromAddressRBData()  # noqa: E501
        if include_optional :
            return PrepareTransactionFromAddressRBData(
                item = cryptoapis.models.prepare_transaction_from_address_rb_data_item.PrepareTransactionFromAddressRB_data_item(
                    additional_data = 'yourAdditionalStriingHere', 
                    amount = '2000000009340', 
                    nonce = '0', 
                    recipient = '0x0902a667d6a3f287835e0a4593cae4167384abc6', 
                    sender = '0x1d107b75353229768dff96051262ce0088a3e26b', 
                    fee = cryptoapis.models.prepare_transaction_from_address_rb_data_item_fee.PrepareTransactionFromAddressRB_data_item_fee(
                        exact_amount = '0.00045', 
                        priority = 'standard', 
                        substract_from_amount = True, ), 
                    transaction_type = 'gas-fee-market-transaction', )
            )
        else :
            return PrepareTransactionFromAddressRBData(
                item = cryptoapis.models.prepare_transaction_from_address_rb_data_item.PrepareTransactionFromAddressRB_data_item(
                    additional_data = 'yourAdditionalStriingHere', 
                    amount = '2000000009340', 
                    nonce = '0', 
                    recipient = '0x0902a667d6a3f287835e0a4593cae4167384abc6', 
                    sender = '0x1d107b75353229768dff96051262ce0088a3e26b', 
                    fee = cryptoapis.models.prepare_transaction_from_address_rb_data_item_fee.PrepareTransactionFromAddressRB_data_item_fee(
                        exact_amount = '0.00045', 
                        priority = 'standard', 
                        substract_from_amount = True, ), 
                    transaction_type = 'gas-fee-market-transaction', ),
        )
        """

    def testPrepareTransactionFromAddressRBData(self):
        """Test PrepareTransactionFromAddressRBData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
