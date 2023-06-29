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
from cryptoapis.models.create_coins_transaction_from_address_for_whole_amount_rb_data_item import CreateCoinsTransactionFromAddressForWholeAmountRBDataItem  # noqa: E501
from cryptoapis.rest import ApiException

class TestCreateCoinsTransactionFromAddressForWholeAmountRBDataItem(unittest.TestCase):
    """CreateCoinsTransactionFromAddressForWholeAmountRBDataItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreateCoinsTransactionFromAddressForWholeAmountRBDataItem
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateCoinsTransactionFromAddressForWholeAmountRBDataItem`
        """
        model = cryptoapis.models.create_coins_transaction_from_address_for_whole_amount_rb_data_item.CreateCoinsTransactionFromAddressForWholeAmountRBDataItem()  # noqa: E501
        if include_optional :
            return CreateCoinsTransactionFromAddressForWholeAmountRBDataItem(
                callback_secret_key = 'yourSecretString', 
                callback_url = 'https://example.com', 
                fee_priority = 'standard', 
                note = 'yourAdditionalInformationhere', 
                recipient_address = '0xc6d46aba0c6e2eb6358c4e24804158cc4d847922'
            )
        else :
            return CreateCoinsTransactionFromAddressForWholeAmountRBDataItem(
                fee_priority = 'standard',
                recipient_address = '0xc6d46aba0c6e2eb6358c4e24804158cc4d847922',
        )
        """

    def testCreateCoinsTransactionFromAddressForWholeAmountRBDataItem(self):
        """Test CreateCoinsTransactionFromAddressForWholeAmountRBDataItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
