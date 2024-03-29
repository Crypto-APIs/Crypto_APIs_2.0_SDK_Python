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
from cryptoapis.models.prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_ri import PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRI  # noqa: E501
from cryptoapis.rest import ApiException

class TestPrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRI(unittest.TestCase):
    """PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRI unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRI
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRI`
        """
        model = cryptoapis.models.prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_ri.PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRI()  # noqa: E501
        if include_optional :
            return PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRI(
                amount = '0.000003', 
                recipient = '0x041c594a0cc194e826bef5411b29c7f27001b7e3', 
                sender = '0x03654A9E78771442CAdf8DB37ae60D6a12bAEa9f', 
                sig_hash = '40738814e379fd2b1923729c87ac80dddc6810a3f8f02fef05452251972ec83a', 
                blockchain_specific = cryptoapis.models.prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_ribs.PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBS()
            )
        else :
            return PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRI(
                amount = '0.000003',
                recipient = '0x041c594a0cc194e826bef5411b29c7f27001b7e3',
                sender = '0x03654A9E78771442CAdf8DB37ae60D6a12bAEa9f',
                sig_hash = '40738814e379fd2b1923729c87ac80dddc6810a3f8f02fef05452251972ec83a',
                blockchain_specific = cryptoapis.models.prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_ribs.PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBS(),
        )
        """

    def testPrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRI(self):
        """Test PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRI"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
