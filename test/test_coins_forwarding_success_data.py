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
from cryptoapis.models.coins_forwarding_success_data import CoinsForwardingSuccessData  # noqa: E501
from cryptoapis.rest import ApiException

class TestCoinsForwardingSuccessData(unittest.TestCase):
    """CoinsForwardingSuccessData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CoinsForwardingSuccessData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CoinsForwardingSuccessData`
        """
        model = cryptoapis.models.coins_forwarding_success_data.CoinsForwardingSuccessData()  # noqa: E501
        if include_optional :
            return CoinsForwardingSuccessData(
                product = 'BLOCKCHAIN_AUTOMATIONS', 
                event = 'COINS_FORWARDING_SUCCESS', 
                item = cryptoapis.models.coins_forwarding_success_data_item.CoinsForwardingSuccess_data_item(
                    blockchain = 'bitcoin', 
                    network = 'testnet', 
                    from_address = 'mmd963W1fECjLyaDCHcioSCZYHkRwjkGST', 
                    to_address = 'ms4KNsbNpoU8g424pzmEjbkFbfAHae1msB', 
                    forwarded_amount = '00059441', 
                    forwarded_unit = 'BTC', 
                    spent_fees_amount = '0.00022827', 
                    spent_fees_unit = 'BTC', 
                    trigger_transaction_id = '86a7546bde4ac28b34504909d138592a6d6fc1277ea1f8f2f9c75dc04bdf3b7b', 
                    forwarding_transaction_id = '2241b5264fac8acb92e9fc597035b99cdd22f6578d63c6f52b099729f7c4f979', )
            )
        else :
            return CoinsForwardingSuccessData(
                product = 'BLOCKCHAIN_AUTOMATIONS',
                event = 'COINS_FORWARDING_SUCCESS',
                item = cryptoapis.models.coins_forwarding_success_data_item.CoinsForwardingSuccess_data_item(
                    blockchain = 'bitcoin', 
                    network = 'testnet', 
                    from_address = 'mmd963W1fECjLyaDCHcioSCZYHkRwjkGST', 
                    to_address = 'ms4KNsbNpoU8g424pzmEjbkFbfAHae1msB', 
                    forwarded_amount = '00059441', 
                    forwarded_unit = 'BTC', 
                    spent_fees_amount = '0.00022827', 
                    spent_fees_unit = 'BTC', 
                    trigger_transaction_id = '86a7546bde4ac28b34504909d138592a6d6fc1277ea1f8f2f9c75dc04bdf3b7b', 
                    forwarding_transaction_id = '2241b5264fac8acb92e9fc597035b99cdd22f6578d63c6f52b099729f7c4f979', ),
        )
        """

    def testCoinsForwardingSuccessData(self):
        """Test CoinsForwardingSuccessData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
