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
from cryptoapis.models.prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_rb_data_item import PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRBDataItem  # noqa: E501
from cryptoapis.rest import ApiException

class TestPrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRBDataItem(unittest.TestCase):
    """PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRBDataItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRBDataItem
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRBDataItem`
        """
        model = cryptoapis.models.prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_rb_data_item.PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRBDataItem()  # noqa: E501
        if include_optional :
            return PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRBDataItem(
                additional_data = 'yourAdditionalDataHere', 
                locktime = 1659001055, 
                xpub = 'tpubDCNoSqt3HF32yq8VU6mgapTuW1FzENZa3C5dKUF6WCQzubWz2nA1yxUhMQWkhhkD58Uc8YiuD8cmB3y5tihqAv4zT2GNyqKTNLchHJmsvt9', 
                fee = cryptoapis.models.prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_rb_data_item_fee.PrepareAUTXO_BasedTransactionFromHDWalletXPubYPubZPubRB_data_item_fee(
                    address = 'tmG2WnrxrpfXxPf5Phk6yPZffqQhezhcUsz', 
                    exact_amount = '0.00458', 
                    priority = 'standard', ), 
                prepare_strategy = 'minimize-dust', 
                recipients = [
                    cryptoapis.models.prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_rb_data_item_recipients_inner.PrepareAUTXO_BasedTransactionFromHDWalletXPubYPubZPubRB_data_item_recipients_inner(
                        address = 'tmHb1bHWAvK6hHDZEq57cbEz2wgxYEMqdbd', 
                        amount = '0.00458', )
                    ], 
                replaceable = True
            )
        else :
            return PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRBDataItem(
                xpub = 'tpubDCNoSqt3HF32yq8VU6mgapTuW1FzENZa3C5dKUF6WCQzubWz2nA1yxUhMQWkhhkD58Uc8YiuD8cmB3y5tihqAv4zT2GNyqKTNLchHJmsvt9',
                fee = cryptoapis.models.prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_rb_data_item_fee.PrepareAUTXO_BasedTransactionFromHDWalletXPubYPubZPubRB_data_item_fee(
                    address = 'tmG2WnrxrpfXxPf5Phk6yPZffqQhezhcUsz', 
                    exact_amount = '0.00458', 
                    priority = 'standard', ),
                recipients = [
                    cryptoapis.models.prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_rb_data_item_recipients_inner.PrepareAUTXO_BasedTransactionFromHDWalletXPubYPubZPubRB_data_item_recipients_inner(
                        address = 'tmHb1bHWAvK6hHDZEq57cbEz2wgxYEMqdbd', 
                        amount = '0.00458', )
                    ],
        )
        """

    def testPrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRBDataItem(self):
        """Test PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRBDataItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
