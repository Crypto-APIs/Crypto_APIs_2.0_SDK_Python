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
from cryptoapis.models.list_confirmed_tokens_transfers_by_address_and_time_range_ri import ListConfirmedTokensTransfersByAddressAndTimeRangeRI  # noqa: E501
from cryptoapis.rest import ApiException

class TestListConfirmedTokensTransfersByAddressAndTimeRangeRI(unittest.TestCase):
    """ListConfirmedTokensTransfersByAddressAndTimeRangeRI unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ListConfirmedTokensTransfersByAddressAndTimeRangeRI
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListConfirmedTokensTransfersByAddressAndTimeRangeRI`
        """
        model = cryptoapis.models.list_confirmed_tokens_transfers_by_address_and_time_range_ri.ListConfirmedTokensTransfersByAddressAndTimeRangeRI()  # noqa: E501
        if include_optional :
            return ListConfirmedTokensTransfersByAddressAndTimeRangeRI(
                contract_address = '0xdac17f958d2ee523a2206206994597c13d831ec7', 
                mined_in_block_height = 12046964, 
                recipient_address = '0xdac17f958d2ee523a2206206994597c13d831ec7', 
                sender_address = '0x65b895f400dae5541d70cbbec07527210158f6e2', 
                token_decimals = 6, 
                token_id = '16721', 
                token_name = 'Tether USD', 
                token_symbol = 'USDT', 
                token_type = 'ERC-20', 
                tokens_amount = '9.146383', 
                transaction_hash = '0x32de09d747bcbed41e8162681a72b2a6c760cf2116ce372fcd357c260909838a', 
                transaction_timestamp = 1615861410
            )
        else :
            return ListConfirmedTokensTransfersByAddressAndTimeRangeRI(
                contract_address = '0xdac17f958d2ee523a2206206994597c13d831ec7',
                mined_in_block_height = 12046964,
                recipient_address = '0xdac17f958d2ee523a2206206994597c13d831ec7',
                sender_address = '0x65b895f400dae5541d70cbbec07527210158f6e2',
                token_type = 'ERC-20',
                transaction_hash = '0x32de09d747bcbed41e8162681a72b2a6c760cf2116ce372fcd357c260909838a',
                transaction_timestamp = 1615861410,
        )
        """

    def testListConfirmedTokensTransfersByAddressAndTimeRangeRI(self):
        """Test ListConfirmedTokensTransfersByAddressAndTimeRangeRI"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
