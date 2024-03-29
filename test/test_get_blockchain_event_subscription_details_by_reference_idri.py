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
from cryptoapis.models.get_blockchain_event_subscription_details_by_reference_idri import GetBlockchainEventSubscriptionDetailsByReferenceIDRI  # noqa: E501
from cryptoapis.rest import ApiException

class TestGetBlockchainEventSubscriptionDetailsByReferenceIDRI(unittest.TestCase):
    """GetBlockchainEventSubscriptionDetailsByReferenceIDRI unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetBlockchainEventSubscriptionDetailsByReferenceIDRI
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetBlockchainEventSubscriptionDetailsByReferenceIDRI`
        """
        model = cryptoapis.models.get_blockchain_event_subscription_details_by_reference_idri.GetBlockchainEventSubscriptionDetailsByReferenceIDRI()  # noqa: E501
        if include_optional :
            return GetBlockchainEventSubscriptionDetailsByReferenceIDRI(
                address = 'tb1qtm44m6xmuasy4sc7nl7thvuxcerau2dfvkkgsc', 
                blockchain = 'bitcoin', 
                callback_secret_key = 'yourSecretKey', 
                callback_url = 'http://example.com', 
                confirmations_count = 5, 
                created_timestamp = 1966238648, 
                deactivation_reasons = [
                    cryptoapis.models.list_blockchain_events_subscriptions_ri_deactivation_reasons_inner.ListBlockchainEventsSubscriptionsRI_deactivationReasons_inner(
                        reason = 'maximum_retry_attempts_reached', 
                        timestamp = 1642102581, )
                    ], 
                event_type = 'ADDRESS_COINS_TRANSACTION_CONFIRMED', 
                is_active = False, 
                network = 'testnet', 
                reference_id = 'bc243c86-0902-4386-b30d-e6b30fa1f2aa', 
                transaction_id = '742b4a8d54a663d372fa16abf74093595ae6fc950f2fa2bb7388c7f4d061d7b8'
            )
        else :
            return GetBlockchainEventSubscriptionDetailsByReferenceIDRI(
                blockchain = 'bitcoin',
                callback_url = 'http://example.com',
                created_timestamp = 1966238648,
                event_type = 'ADDRESS_COINS_TRANSACTION_CONFIRMED',
                is_active = False,
                network = 'testnet',
                reference_id = 'bc243c86-0902-4386-b30d-e6b30fa1f2aa',
        )
        """

    def testGetBlockchainEventSubscriptionDetailsByReferenceIDRI(self):
        """Test GetBlockchainEventSubscriptionDetailsByReferenceIDRI"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
