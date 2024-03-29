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
from cryptoapis.models.prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_ribsd2_vin_inner import PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSD2VinInner  # noqa: E501
from cryptoapis.rest import ApiException

class TestPrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSD2VinInner(unittest.TestCase):
    """PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSD2VinInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSD2VinInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSD2VinInner`
        """
        model = cryptoapis.models.prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_ribsd2_vin_inner.PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSD2VinInner()  # noqa: E501
        if include_optional :
            return PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSD2VinInner(
                address = 'yLML6bW4d4gF5n3MzYwBNZag5CFaphqVmG', 
                change = 0, 
                derivation_index = 1, 
                output_index = 1, 
                satoshis = 912300000, 
                script = '76a914005b321d7019768e887f604630a4d6b0bdcff5ef88ac', 
                sighash = 'ce34bad636f22a18d8712d7d74cfd10fca1888fda1d6d4dcc8f1baf81e266d67', 
                transaction_id = '69612cd50be51af0ad5d3ae2ee30de7d59db45dc9453018f91de7e4ee023ef5d'
            )
        else :
            return PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSD2VinInner(
                address = 'yLML6bW4d4gF5n3MzYwBNZag5CFaphqVmG',
                change = 0,
                derivation_index = 1,
                output_index = 1,
                satoshis = 912300000,
                script = '76a914005b321d7019768e887f604630a4d6b0bdcff5ef88ac',
                sighash = 'ce34bad636f22a18d8712d7d74cfd10fca1888fda1d6d4dcc8f1baf81e266d67',
                transaction_id = '69612cd50be51af0ad5d3ae2ee30de7d59db45dc9453018f91de7e4ee023ef5d',
        )
        """

    def testPrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSD2VinInner(self):
        """Test PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSD2VinInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
