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
from cryptoapis.models.prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_ribsbc_vout_inner import PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSBCVoutInner  # noqa: E501
from cryptoapis.rest import ApiException

class TestPrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSBCVoutInner(unittest.TestCase):
    """PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSBCVoutInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSBCVoutInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSBCVoutInner`
        """
        model = cryptoapis.models.prepare_autxo_based_transaction_from_hd_wallet_x_pub_y_pub_z_pub_ribsbc_vout_inner.PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSBCVoutInner()  # noqa: E501
        if include_optional :
            return PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSBCVoutInner(
                address = 'bchtest:qzhksklst5p5qeer64gf70ssk69st0q3vcpvplqhny', 
                satoshis = 5904, 
                script = '76a914af685bf05d03406723d5509f3e10b68b05bc116688ac'
            )
        else :
            return PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSBCVoutInner(
                address = 'bchtest:qzhksklst5p5qeer64gf70ssk69st0q3vcpvplqhny',
                satoshis = 5904,
                script = '76a914af685bf05d03406723d5509f3e10b68b05bc116688ac',
        )
        """

    def testPrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSBCVoutInner(self):
        """Test PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIBSBCVoutInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
