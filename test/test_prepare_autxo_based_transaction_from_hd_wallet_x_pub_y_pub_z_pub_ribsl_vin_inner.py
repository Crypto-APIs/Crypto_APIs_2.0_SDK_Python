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
from cryptoapis.models.prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_ribsl_vin_inner import PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSLVinInner  # noqa: E501
from cryptoapis.rest import ApiException

class TestPrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSLVinInner(unittest.TestCase):
    """PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSLVinInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSLVinInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSLVinInner`
        """
        model = cryptoapis.models.prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_ribsl_vin_inner.PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSLVinInner()  # noqa: E501
        if include_optional :
            return PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSLVinInner(
                address = 'tltc1qky8qd86dtha5l4daspec2cauf2ew58z8gfw6y2', 
                change = 0, 
                derivation_index = 0, 
                output_index = 1, 
                satoshis = 10000, 
                script = '0014b10e069f4d5dfb4fd5bd80738563bc4ab2ea1c47', 
                sighash = 'deddbe2c247b054d00f8ab03987ea576171953445e28041b09e732fc0bedcd4e', 
                transaction_id = '9b9cf1d240dcf38c2946dc6c4671993cc7e38bf1d08b084b31332e11b1806683'
            )
        else :
            return PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSLVinInner(
                address = 'tltc1qky8qd86dtha5l4daspec2cauf2ew58z8gfw6y2',
                change = 0,
                derivation_index = 0,
                output_index = 1,
                satoshis = 10000,
                script = '0014b10e069f4d5dfb4fd5bd80738563bc4ab2ea1c47',
                sighash = 'deddbe2c247b054d00f8ab03987ea576171953445e28041b09e732fc0bedcd4e',
                transaction_id = '9b9cf1d240dcf38c2946dc6c4671993cc7e38bf1d08b084b31332e11b1806683',
        )
        """

    def testPrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSLVinInner(self):
        """Test PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSLVinInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
