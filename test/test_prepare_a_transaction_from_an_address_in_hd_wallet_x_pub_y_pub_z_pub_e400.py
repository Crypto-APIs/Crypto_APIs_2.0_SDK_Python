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
from cryptoapis.models.prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_e400 import PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubE400  # noqa: E501
from cryptoapis.rest import ApiException

class TestPrepareATransactionFromAnAddressInHDWalletXPubYPubZPubE400(unittest.TestCase):
    """PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubE400 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubE400
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubE400`
        """
        model = cryptoapis.models.prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_e400.PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubE400()  # noqa: E501
        if include_optional :
            return PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubE400(
                code = 'invalid_pagination', 
                message = 'The pagination attributes that have been used are invalid. Please check the Documentation to see details on pagination.', 
                details = [
                    cryptoapis.models.banned_ip_address_details_inner.BannedIpAddress_details_inner(
                        attribute = 'attribute which content caused the error', 
                        message = 'message describing the error', )
                    ]
            )
        else :
            return PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubE400(
                code = 'invalid_pagination',
                message = 'The pagination attributes that have been used are invalid. Please check the Documentation to see details on pagination.',
        )
        """

    def testPrepareATransactionFromAnAddressInHDWalletXPubYPubZPubE400(self):
        """Test PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubE400"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()