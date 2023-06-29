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

import cryptoapis
from cryptoapis.api.manage_subscriptions_api import ManageSubscriptionsApi  # noqa: E501
from cryptoapis.rest import ApiException


class TestManageSubscriptionsApi(unittest.TestCase):
    """ManageSubscriptionsApi unit test stubs"""

    def setUp(self):
        self.api = cryptoapis.api.manage_subscriptions_api.ManageSubscriptionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_activate_blockchain_event_subscription(self):
        """Test case for activate_blockchain_event_subscription

        Activate Blockchain Event Subscription  # noqa: E501
        """
        pass

    def test_delete_blockchain_event_subscription(self):
        """Test case for delete_blockchain_event_subscription

        Delete Blockchain Event Subscription  # noqa: E501
        """
        pass

    def test_get_blockchain_event_subscription_details_by_reference_id(self):
        """Test case for get_blockchain_event_subscription_details_by_reference_id

        Get Blockchain Event Subscription Details By Reference ID  # noqa: E501
        """
        pass

    def test_list_blockchain_events_subscriptions(self):
        """Test case for list_blockchain_events_subscriptions

        List Blockchain Events Subscriptions  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
