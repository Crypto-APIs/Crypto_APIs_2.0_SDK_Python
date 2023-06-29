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
from cryptoapis.api.automatic_coins_forwarding_api import AutomaticCoinsForwardingApi  # noqa: E501
from cryptoapis.rest import ApiException


class TestAutomaticCoinsForwardingApi(unittest.TestCase):
    """AutomaticCoinsForwardingApi unit test stubs"""

    def setUp(self):
        self.api = cryptoapis.api.automatic_coins_forwarding_api.AutomaticCoinsForwardingApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_automatic_coins_forwarding(self):
        """Test case for create_automatic_coins_forwarding

        Create Automatic Coins Forwarding  # noqa: E501
        """
        pass

    def test_delete_automatic_coins_forwarding(self):
        """Test case for delete_automatic_coins_forwarding

        Delete Automatic Coins Forwarding  # noqa: E501
        """
        pass

    def test_list_coins_forwarding_automations(self):
        """Test case for list_coins_forwarding_automations

        List Coins Forwarding Automations  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
