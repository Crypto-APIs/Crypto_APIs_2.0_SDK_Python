"""
    CryptoAPIs

    Crypto APIs is a complex and innovative infrastructure layer that radically simplifies the development of any Blockchain and Crypto related applications. Organized around REST, Crypto APIs can assist both novice Bitcoin/Ethereum enthusiasts and crypto experts with the development of their blockchain applications. Crypto APIs provides unified endpoints and data, raw data, automatic tokens and coins forwardings, callback functionalities, and much more.  # noqa: E501

    The version of the OpenAPI document: 2021-03-20
    Contact: developers@cryptoapis.io
    Generated by: https://openapi-generator.tech
"""


import unittest

import cryptoapis
from cryptoapis.api.internal_api import InternalApi  # noqa: E501


class TestInternalApi(unittest.TestCase):
    """InternalApi unit test stubs"""

    def setUp(self):
        self.api = InternalApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_internal_transaction_by_transaction_hash_and_operation_id(self):
        """Test case for get_internal_transaction_by_transaction_hash_and_operation_id

        Get Internal Transaction by Transaction Hash and Operation Id  # noqa: E501
        """
        pass

    def test_list_internal_transaction_details_by_transaction_hash(self):
        """Test case for list_internal_transaction_details_by_transaction_hash

        List Internal Transaction Details by Transaction Hash  # noqa: E501
        """
        pass

    def test_list_internal_transactions_by_address(self):
        """Test case for list_internal_transactions_by_address

        List Internal Transactions By Address  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
