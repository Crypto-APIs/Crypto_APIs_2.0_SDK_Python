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
from cryptoapis.models.address_tokens_transaction_unconfirmed_data_item import AddressTokensTransactionUnconfirmedDataItem  # noqa: E501
from cryptoapis.rest import ApiException

class TestAddressTokensTransactionUnconfirmedDataItem(unittest.TestCase):
    """AddressTokensTransactionUnconfirmedDataItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AddressTokensTransactionUnconfirmedDataItem
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AddressTokensTransactionUnconfirmedDataItem`
        """
        model = cryptoapis.models.address_tokens_transaction_unconfirmed_data_item.AddressTokensTransactionUnconfirmedDataItem()  # noqa: E501
        if include_optional :
            return AddressTokensTransactionUnconfirmedDataItem(
                blockchain = 'ethereum', 
                network = 'ropsten', 
                address = '0x65b895f400dae5541d70cbbec07527210158f6e2', 
                transaction_id = '0x76670f3bb45c09e69173fe74834face446edf251c5f02ec30384a0957fce482b', 
                token_type = 'ERC-20', 
                token = cryptoapis.models.address_tokens_transaction_unconfirmed_token.AddressTokensTransactionUnconfirmedToken(), 
                direction = 'incoming', 
                first_seen_in_mempool_timestamp = 1210363220
            )
        else :
            return AddressTokensTransactionUnconfirmedDataItem(
                blockchain = 'ethereum',
                network = 'ropsten',
                address = '0x65b895f400dae5541d70cbbec07527210158f6e2',
                transaction_id = '0x76670f3bb45c09e69173fe74834face446edf251c5f02ec30384a0957fce482b',
                token_type = 'ERC-20',
                token = cryptoapis.models.address_tokens_transaction_unconfirmed_token.AddressTokensTransactionUnconfirmedToken(),
                direction = 'incoming',
                first_seen_in_mempool_timestamp = 1210363220,
        )
        """

    def testAddressTokensTransactionUnconfirmedDataItem(self):
        """Test AddressTokensTransactionUnconfirmedDataItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
