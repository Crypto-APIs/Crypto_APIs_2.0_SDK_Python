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
from cryptoapis.models.list_zilliqa_transactions_by_block_hash_e401 import ListZilliqaTransactionsByBlockHashE401  # noqa: E501
from cryptoapis.rest import ApiException

class TestListZilliqaTransactionsByBlockHashE401(unittest.TestCase):
    """ListZilliqaTransactionsByBlockHashE401 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ListZilliqaTransactionsByBlockHashE401
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListZilliqaTransactionsByBlockHashE401`
        """
        model = cryptoapis.models.list_zilliqa_transactions_by_block_hash_e401.ListZilliqaTransactionsByBlockHashE401()  # noqa: E501
        if include_optional :
            return ListZilliqaTransactionsByBlockHashE401(
                code = 'invalid_api_key', 
                message = 'The provided API key is invalid. Please, generate a new one from your Dashboard.', 
                details = [
                    cryptoapis.models.banned_ip_address_details_inner.BannedIpAddress_details_inner(
                        attribute = 'attribute which content caused the error', 
                        message = 'message describing the error', )
                    ]
            )
        else :
            return ListZilliqaTransactionsByBlockHashE401(
                code = 'invalid_api_key',
                message = 'The provided API key is invalid. Please, generate a new one from your Dashboard.',
        )
        """

    def testListZilliqaTransactionsByBlockHashE401(self):
        """Test ListZilliqaTransactionsByBlockHashE401"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
