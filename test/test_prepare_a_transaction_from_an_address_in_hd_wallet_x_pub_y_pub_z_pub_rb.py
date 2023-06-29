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
from cryptoapis.models.prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_rb import PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRB  # noqa: E501
from cryptoapis.rest import ApiException

class TestPrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRB(unittest.TestCase):
    """PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRB unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRB
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRB`
        """
        model = cryptoapis.models.prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_rb.PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRB()  # noqa: E501
        if include_optional :
            return PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRB(
                context = 'yourExampleString', 
                data = cryptoapis.models.prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_rb_data.PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRB_data(
                    item = cryptoapis.models.prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_rb_data_item.PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRB_data_item(
                        additional_data = 'yourAdditionalDataHere', 
                        amount = '0.000003', 
                        recipient = '0x041c594a0cc194e826bef5411b29c7f27001b7e3', 
                        sender = '0x03654A9E78771442CAdf8DB37ae60D6a12bAEa9f', 
                        xpub = 'xpub6CsGdqTDEVRnLmpWN218HBwJqfhqSx46iA8ByzEA5Bz9jfwU3TSg9U7ambKgJyykvCraHQ6sAFAddMGFdPzhXrRanKbHnnkbDTyRPyn5gRJ', 
                        fee = cryptoapis.models.prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_rb_data_item_fee.PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRB_data_item_fee(
                            exact_amount = '0.00045', 
                            priority = 'standard', ), 
                        nonce = '0', 
                        transaction_type = 'gas-fee-market-transaction', 
                        sequence = '31715632', ), )
            )
        else :
            return PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRB(
                data = cryptoapis.models.prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_rb_data.PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRB_data(
                    item = cryptoapis.models.prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_rb_data_item.PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRB_data_item(
                        additional_data = 'yourAdditionalDataHere', 
                        amount = '0.000003', 
                        recipient = '0x041c594a0cc194e826bef5411b29c7f27001b7e3', 
                        sender = '0x03654A9E78771442CAdf8DB37ae60D6a12bAEa9f', 
                        xpub = 'xpub6CsGdqTDEVRnLmpWN218HBwJqfhqSx46iA8ByzEA5Bz9jfwU3TSg9U7ambKgJyykvCraHQ6sAFAddMGFdPzhXrRanKbHnnkbDTyRPyn5gRJ', 
                        fee = cryptoapis.models.prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_rb_data_item_fee.PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRB_data_item_fee(
                            exact_amount = '0.00045', 
                            priority = 'standard', ), 
                        nonce = '0', 
                        transaction_type = 'gas-fee-market-transaction', 
                        sequence = '31715632', ), ),
        )
        """

    def testPrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRB(self):
        """Test PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRB"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()