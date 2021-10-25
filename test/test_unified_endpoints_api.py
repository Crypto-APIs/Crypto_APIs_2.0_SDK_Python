"""
    CryptoAPIs

    Crypto APIs 2.0 is a complex and innovative infrastructure layer that radically simplifies the development of any Blockchain and Crypto related applications. Organized around REST, Crypto APIs 2.0 can assist both novice Bitcoin/Ethereum enthusiasts and crypto experts with the development of their blockchain applications. Crypto APIs 2.0 provides unified endpoints and data, raw data, automatic tokens and coins forwardings, callback functionalities, and much more.  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: developers@cryptoapis.io
    Generated by: https://openapi-generator.tech
"""


import unittest

import cryptoapis
from cryptoapis.api.unified_endpoints_api import UnifiedEndpointsApi  # noqa: E501


class TestUnifiedEndpointsApi(unittest.TestCase):
    """UnifiedEndpointsApi unit test stubs"""

    def setUp(self):
        self.api = UnifiedEndpointsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_address_details(self):
        """Test case for get_address_details

        Get Address Details  # noqa: E501
        """
        pass

    def test_get_block_details_by_block_hash(self):
        """Test case for get_block_details_by_block_hash

        Get Block Details By Block Hash  # noqa: E501
        """
        pass

    def test_get_block_details_by_block_height(self):
        """Test case for get_block_details_by_block_height

        Get Block Details By Block Height  # noqa: E501
        """
        pass

    def test_get_fee_recommendations(self):
        """Test case for get_fee_recommendations

        Get Fee Recommendations  # noqa: E501
        """
        pass

    def test_get_last_mined_block(self):
        """Test case for get_last_mined_block

        Get Last Mined Block  # noqa: E501
        """
        pass

    def test_get_transaction_details_by_transaction_id(self):
        """Test case for get_transaction_details_by_transaction_id

        Get Transaction Details By Transaction ID  # noqa: E501
        """
        pass

    def test_list_all_unconfirmed_transactions(self):
        """Test case for list_all_unconfirmed_transactions

        List All Unconfirmed Transactions  # noqa: E501
        """
        pass

    def test_list_confirmed_transactions_by_address(self):
        """Test case for list_confirmed_transactions_by_address

        List Confirmed Transactions By Address  # noqa: E501
        """
        pass

    def test_list_latest_mined_blocks(self):
        """Test case for list_latest_mined_blocks

        List Latest Mined Blocks  # noqa: E501
        """
        pass

    def test_list_transactions_by_block_hash(self):
        """Test case for list_transactions_by_block_hash

        List Transactions by Block Hash  # noqa: E501
        """
        pass

    def test_list_transactions_by_block_height(self):
        """Test case for list_transactions_by_block_height

        List Transactions by Block Height  # noqa: E501
        """
        pass

    def test_list_unconfirmed_transactions_by_address(self):
        """Test case for list_unconfirmed_transactions_by_address

        List Unconfirmed Transactions by Address  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
