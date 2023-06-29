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
from cryptoapis.models.get_raw_transaction_data_r import GetRawTransactionDataR  # noqa: E501
from cryptoapis.rest import ApiException

class TestGetRawTransactionDataR(unittest.TestCase):
    """GetRawTransactionDataR unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetRawTransactionDataR
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetRawTransactionDataR`
        """
        model = cryptoapis.models.get_raw_transaction_data_r.GetRawTransactionDataR()  # noqa: E501
        if include_optional :
            return GetRawTransactionDataR(
                api_version = '2021-03-20', 
                request_id = '601c1710034ed6d407996b30', 
                context = 'yourExampleString', 
                data = cryptoapis.models.get_raw_transaction_data_r_data.GetRawTransactionDataR_data(
                    item = cryptoapis.models.get_raw_transaction_data_ri.GetRawTransactionDataRI(
                        transaction_hex = '01000000000101f8cb1cd1892d31aaafa35a92128b3a11469e675261c83a30be5b25ae8c97eeca0100000017160014daaf6d5cb86befe42df851a4d1df052e663754c1ffffffff02403800000000000017a914507a5bd8cac1d9efdf4c0a4bfacb3e0abb4f8d15879cd90c000000000017a91475eb14fa1dc2c72637df3c58bc22d925ca0753af8702483045022100c11ea5740bcd69f0f68a4914279838014d28923134d18e05c5a5486dfd06cc8c02200dadccec3f07bed0d1040f9e5a155efa5fdd40fc91f92342578d26848da4c6b901210287e995526aa6ccb96141bb598fc7f73323279e026c55039d15f0cfbda5dea84100000000', ), )
            )
        else :
            return GetRawTransactionDataR(
                api_version = '2021-03-20',
                request_id = '601c1710034ed6d407996b30',
                data = cryptoapis.models.get_raw_transaction_data_r_data.GetRawTransactionDataR_data(
                    item = cryptoapis.models.get_raw_transaction_data_ri.GetRawTransactionDataRI(
                        transaction_hex = '01000000000101f8cb1cd1892d31aaafa35a92128b3a11469e675261c83a30be5b25ae8c97eeca0100000017160014daaf6d5cb86befe42df851a4d1df052e663754c1ffffffff02403800000000000017a914507a5bd8cac1d9efdf4c0a4bfacb3e0abb4f8d15879cd90c000000000017a91475eb14fa1dc2c72637df3c58bc22d925ca0753af8702483045022100c11ea5740bcd69f0f68a4914279838014d28923134d18e05c5a5486dfd06cc8c02200dadccec3f07bed0d1040f9e5a155efa5fdd40fc91f92342578d26848da4c6b901210287e995526aa6ccb96141bb598fc7f73323279e026c55039d15f0cfbda5dea84100000000', ), ),
        )
        """

    def testGetRawTransactionDataR(self):
        """Test GetRawTransactionDataR"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
