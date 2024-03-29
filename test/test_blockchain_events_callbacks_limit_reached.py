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
from cryptoapis.models.blockchain_events_callbacks_limit_reached import BlockchainEventsCallbacksLimitReached  # noqa: E501
from cryptoapis.rest import ApiException

class TestBlockchainEventsCallbacksLimitReached(unittest.TestCase):
    """BlockchainEventsCallbacksLimitReached unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test BlockchainEventsCallbacksLimitReached
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BlockchainEventsCallbacksLimitReached`
        """
        model = cryptoapis.models.blockchain_events_callbacks_limit_reached.BlockchainEventsCallbacksLimitReached()  # noqa: E501
        if include_optional :
            return BlockchainEventsCallbacksLimitReached(
                code = 'blockchain_events_callbacks_limit_reached', 
                message = 'You have reached the maximum number of active Blockchain Events subscriptions which is {callbacks_limit} now. Please upgrade your plan to be get higher number of active subscriptions.', 
                details = [
                    cryptoapis.models.banned_ip_address_details_inner.BannedIpAddress_details_inner(
                        attribute = 'attribute which content caused the error', 
                        message = 'message describing the error', )
                    ]
            )
        else :
            return BlockchainEventsCallbacksLimitReached(
                code = 'blockchain_events_callbacks_limit_reached',
                message = 'You have reached the maximum number of active Blockchain Events subscriptions which is {callbacks_limit} now. Please upgrade your plan to be get higher number of active subscriptions.',
        )
        """

    def testBlockchainEventsCallbacksLimitReached(self):
        """Test BlockchainEventsCallbacksLimitReached"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
