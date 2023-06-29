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
from cryptoapis.models.list_blockchain_events_subscriptions_r import ListBlockchainEventsSubscriptionsR  # noqa: E501
from cryptoapis.rest import ApiException

class TestListBlockchainEventsSubscriptionsR(unittest.TestCase):
    """ListBlockchainEventsSubscriptionsR unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ListBlockchainEventsSubscriptionsR
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListBlockchainEventsSubscriptionsR`
        """
        model = cryptoapis.models.list_blockchain_events_subscriptions_r.ListBlockchainEventsSubscriptionsR()  # noqa: E501
        if include_optional :
            return ListBlockchainEventsSubscriptionsR(
                api_version = '2021-03-20', 
                request_id = '601c1710034ed6d407996b30', 
                context = 'yourExampleString', 
                data = cryptoapis.models.list_blockchain_events_subscriptions_r_data.ListBlockchainEventsSubscriptionsR_data(
                    limit = 50, 
                    offset = 0, 
                    total = 100, 
                    items = [], )
            )
        else :
            return ListBlockchainEventsSubscriptionsR(
                api_version = '2021-03-20',
                request_id = '601c1710034ed6d407996b30',
                data = cryptoapis.models.list_blockchain_events_subscriptions_r_data.ListBlockchainEventsSubscriptionsR_data(
                    limit = 50, 
                    offset = 0, 
                    total = 100, 
                    items = [], ),
        )
        """

    def testListBlockchainEventsSubscriptionsR(self):
        """Test ListBlockchainEventsSubscriptionsR"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
