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
from cryptoapis.models.transaction_mined import TransactionMined  # noqa: E501
from cryptoapis.rest import ApiException

class TestTransactionMined(unittest.TestCase):
    """TransactionMined unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TransactionMined
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TransactionMined`
        """
        model = cryptoapis.models.transaction_mined.TransactionMined()  # noqa: E501
        if include_optional :
            return TransactionMined(
                api_version = '2021-03-20', 
                reference_id = '6038d09050653d1f0e40584c', 
                idempotency_key = 'e55bf7a4a7188855f1c27541a6c387d04cc3b22ee34d1304b0e6ecad61c9906c', 
                data = cryptoapis.models.transaction_mined_data.TransactionMined_data(
                    product = 'BLOCKCHAIN_EVENTS', 
                    event = 'TRANSACTION_MINED', 
                    item = cryptoapis.models.transaction_mined_data_item.TransactionMined_data_item(
                        blockchain = 'bitcoin', 
                        network = 'testnet', 
                        transaction_id = 'e6439461e5bf8920e75740896d4b47730b844837295e8c3f2dbf441542aebcb6', 
                        mined_in_block = cryptoapis.models.transaction_mined_data_item_mined_in_block.TransactionMined_data_item_minedInBlock(
                            height = 667900, 
                            hash = 'e9da0c8ce1861050c20f40fb660df4d13399f50b882e85bcd98126eb1173cc50', 
                            timestamp = 1610355613, ), ), )
            )
        else :
            return TransactionMined(
                api_version = '2021-03-20',
                reference_id = '6038d09050653d1f0e40584c',
                idempotency_key = 'e55bf7a4a7188855f1c27541a6c387d04cc3b22ee34d1304b0e6ecad61c9906c',
                data = cryptoapis.models.transaction_mined_data.TransactionMined_data(
                    product = 'BLOCKCHAIN_EVENTS', 
                    event = 'TRANSACTION_MINED', 
                    item = cryptoapis.models.transaction_mined_data_item.TransactionMined_data_item(
                        blockchain = 'bitcoin', 
                        network = 'testnet', 
                        transaction_id = 'e6439461e5bf8920e75740896d4b47730b844837295e8c3f2dbf441542aebcb6', 
                        mined_in_block = cryptoapis.models.transaction_mined_data_item_mined_in_block.TransactionMined_data_item_minedInBlock(
                            height = 667900, 
                            hash = 'e9da0c8ce1861050c20f40fb660df4d13399f50b882e85bcd98126eb1173cc50', 
                            timestamp = 1610355613, ), ), ),
        )
        """

    def testTransactionMined(self):
        """Test TransactionMined"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
