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
from cryptoapis.models.get_transaction_details_by_transaction_idribszv_shielded_spend_inner import GetTransactionDetailsByTransactionIDRIBSZVShieldedSpendInner  # noqa: E501
from cryptoapis.rest import ApiException

class TestGetTransactionDetailsByTransactionIDRIBSZVShieldedSpendInner(unittest.TestCase):
    """GetTransactionDetailsByTransactionIDRIBSZVShieldedSpendInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetTransactionDetailsByTransactionIDRIBSZVShieldedSpendInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetTransactionDetailsByTransactionIDRIBSZVShieldedSpendInner`
        """
        model = cryptoapis.models.get_transaction_details_by_transaction_idribszv_shielded_spend_inner.GetTransactionDetailsByTransactionIDRIBSZVShieldedSpendInner()  # noqa: E501
        if include_optional :
            return GetTransactionDetailsByTransactionIDRIBSZVShieldedSpendInner(
                anchor = 'd32ddbaf0d9dc8c10783c01fd9ba5bd0bc2e5efe3d1665d7d6771eb4393736b4', 
                cv = '547a9cef4937304f97acacfcd9827b5aa1b2e5b1ae32e360fae828b955564a0e', 
                nullifier = '30e41a9a6605933a75ec42439ab65eb347025002f6486e5549abb82438447dbe', 
                proof = '030ff7fdb006db7f9acb0d2d6fae180e4395f0b6a979f6ddf48a349bc03ad2e7bb0324a5c3c7e6be131c34126ad22c74138f45f6f77bba706dfc87335a9adffcfef20a03e47751f403a37f9c5e1874aa50818c3eef09304c57c77b111057c09ed2112a7ed310ad285e0b778a4f44b654032b642b8b2df3be16bea011da7a2221bc0f0a0309f51f87caef2ea0f665f1a77d0dd50766d835d181e534818d8c3413b4d555990222574d9c92f81f17ff0af7a0583e76b3d3d4df2927561f37e57e15bc07b3f5d70306a9624c496d0bcb40085894bf32ef05db6469ec145c0ce5529e2697b6a0252c0216930cf7b3a7381762a6a91868e9d2bf823bfc7fb885de1fbd6a6cacae02db590318ffeb357ffd6832893ab0ccd3b15cef1df0fef45c091cf33fccee43a2834d44', 
                rk = '39bdf742e16c4d1533a56df956bebe4d0214d4a361820db58a293847b6344d30', 
                spend_auth_sig = '0f3b38a91fffbbf58f99d2d070002c0868be6804204b7bf4be0df47f62ee5e0d43222776a71fd7e1421ec54502194192d73681701b743ad427573ca18a95a405'
            )
        else :
            return GetTransactionDetailsByTransactionIDRIBSZVShieldedSpendInner(
                anchor = 'd32ddbaf0d9dc8c10783c01fd9ba5bd0bc2e5efe3d1665d7d6771eb4393736b4',
                cv = '547a9cef4937304f97acacfcd9827b5aa1b2e5b1ae32e360fae828b955564a0e',
                nullifier = '30e41a9a6605933a75ec42439ab65eb347025002f6486e5549abb82438447dbe',
                proof = '030ff7fdb006db7f9acb0d2d6fae180e4395f0b6a979f6ddf48a349bc03ad2e7bb0324a5c3c7e6be131c34126ad22c74138f45f6f77bba706dfc87335a9adffcfef20a03e47751f403a37f9c5e1874aa50818c3eef09304c57c77b111057c09ed2112a7ed310ad285e0b778a4f44b654032b642b8b2df3be16bea011da7a2221bc0f0a0309f51f87caef2ea0f665f1a77d0dd50766d835d181e534818d8c3413b4d555990222574d9c92f81f17ff0af7a0583e76b3d3d4df2927561f37e57e15bc07b3f5d70306a9624c496d0bcb40085894bf32ef05db6469ec145c0ce5529e2697b6a0252c0216930cf7b3a7381762a6a91868e9d2bf823bfc7fb885de1fbd6a6cacae02db590318ffeb357ffd6832893ab0ccd3b15cef1df0fef45c091cf33fccee43a2834d44',
                rk = '39bdf742e16c4d1533a56df956bebe4d0214d4a361820db58a293847b6344d30',
                spend_auth_sig = '0f3b38a91fffbbf58f99d2d070002c0868be6804204b7bf4be0df47f62ee5e0d43222776a71fd7e1421ec54502194192d73681701b743ad427573ca18a95a405',
        )
        """

    def testGetTransactionDetailsByTransactionIDRIBSZVShieldedSpendInner(self):
        """Test GetTransactionDetailsByTransactionIDRIBSZVShieldedSpendInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
