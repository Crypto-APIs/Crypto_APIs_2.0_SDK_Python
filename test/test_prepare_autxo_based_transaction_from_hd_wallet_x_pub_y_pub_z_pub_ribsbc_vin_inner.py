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
from cryptoapis.models.prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_ribsbc_vin_inner import PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSBCVinInner  # noqa: E501
from cryptoapis.rest import ApiException

class TestPrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSBCVinInner(unittest.TestCase):
    """PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSBCVinInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSBCVinInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSBCVinInner`
        """
        model = cryptoapis.models.prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_ribsbc_vin_inner.PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSBCVinInner()  # noqa: E501
        if include_optional :
            return PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSBCVinInner(
                address = 'bchtest:qqelmepfue2vs2ahmqwd26en6s5uern2duw0v0f8cr', 
                change = 0, 
                derivation_index = 0, 
                output_index = 0, 
                satoshis = 10000, 
                script = '76a91433fde429e654c82bb7d81cd56b33d429cc8e6a6f88ac', 
                sighash = '73c0e09da473d0fd28715cce2ec6eb0a1c5a72d84e46acd1a02942454d5f1dd1', 
                transaction_id = 'd4eb833c3e75f8c8f11bcac592c6c31143a0509115e4a5526cedeba76a239bcd'
            )
        else :
            return PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSBCVinInner(
                address = 'bchtest:qqelmepfue2vs2ahmqwd26en6s5uern2duw0v0f8cr',
                change = 0,
                derivation_index = 0,
                output_index = 0,
                satoshis = 10000,
                script = '76a91433fde429e654c82bb7d81cd56b33d429cc8e6a6f88ac',
                sighash = '73c0e09da473d0fd28715cce2ec6eb0a1c5a72d84e46acd1a02942454d5f1dd1',
                transaction_id = 'd4eb833c3e75f8c8f11bcac592c6c31143a0509115e4a5526cedeba76a239bcd',
        )
        """

    def testPrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSBCVinInner(self):
        """Test PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSBCVinInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()