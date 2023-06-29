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
from cryptoapis.models.prepare_a_fungible_token_transfer_from_address_rb_data import PrepareAFungibleTokenTransferFromAddressRBData  # noqa: E501
from cryptoapis.rest import ApiException

class TestPrepareAFungibleTokenTransferFromAddressRBData(unittest.TestCase):
    """PrepareAFungibleTokenTransferFromAddressRBData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PrepareAFungibleTokenTransferFromAddressRBData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PrepareAFungibleTokenTransferFromAddressRBData`
        """
        model = cryptoapis.models.prepare_a_fungible_token_transfer_from_address_rb_data.PrepareAFungibleTokenTransferFromAddressRBData()  # noqa: E501
        if include_optional :
            return PrepareAFungibleTokenTransferFromAddressRBData(
                item = cryptoapis.models.prepare_a_fungible_token_transfer_from_address_rb_data_item.PrepareAFungibleTokenTransferFromAddressRB_data_item(
                    amount = '1.09340', 
                    contract = '0xdAC17F958D2ee523a2206206994597C13D831ec7', 
                    nonce = '0', 
                    recipient = '0x534bd102153ef199abae8296a2fae4599fc44cdc', 
                    sender = '0x1d107b75353229768dff96051262ce0088a3e26b', 
                    fee = cryptoapis.models.prepare_a_fungible_token_transfer_from_address_rb_data_item_fee.PrepareAFungibleTokenTransferFromAddressRB_data_item_fee(
                        exact_amount = '0.00045', 
                        priority = 'standard', ), 
                    transaction_type = 'legacy-transaction', )
            )
        else :
            return PrepareAFungibleTokenTransferFromAddressRBData(
                item = cryptoapis.models.prepare_a_fungible_token_transfer_from_address_rb_data_item.PrepareAFungibleTokenTransferFromAddressRB_data_item(
                    amount = '1.09340', 
                    contract = '0xdAC17F958D2ee523a2206206994597C13D831ec7', 
                    nonce = '0', 
                    recipient = '0x534bd102153ef199abae8296a2fae4599fc44cdc', 
                    sender = '0x1d107b75353229768dff96051262ce0088a3e26b', 
                    fee = cryptoapis.models.prepare_a_fungible_token_transfer_from_address_rb_data_item_fee.PrepareAFungibleTokenTransferFromAddressRB_data_item_fee(
                        exact_amount = '0.00045', 
                        priority = 'standard', ), 
                    transaction_type = 'legacy-transaction', ),
        )
        """

    def testPrepareAFungibleTokenTransferFromAddressRBData(self):
        """Test PrepareAFungibleTokenTransferFromAddressRBData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
