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
from cryptoapis.models.get_zilliqa_block_details_by_block_height_ri import GetZilliqaBlockDetailsByBlockHeightRI  # noqa: E501
from cryptoapis.rest import ApiException

class TestGetZilliqaBlockDetailsByBlockHeightRI(unittest.TestCase):
    """GetZilliqaBlockDetailsByBlockHeightRI unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetZilliqaBlockDetailsByBlockHeightRI
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetZilliqaBlockDetailsByBlockHeightRI`
        """
        model = cryptoapis.models.get_zilliqa_block_details_by_block_height_ri.GetZilliqaBlockDetailsByBlockHeightRI()  # noqa: E501
        if include_optional :
            return GetZilliqaBlockDetailsByBlockHeightRI(
                block_hash = '0xf679d0b5387f0b0b3c3c1f368305512b23860888ba4415063d464a09b8bb6205 Block 1244297 Block 1244299', 
                difficulty = '41.375', 
                ds_block = 12443, 
                ds_difficulty = '48.625', 
                ds_leader = 'zil1k9hne0uu86wuj2n7qdqwhrm9uma0xn7ut42tsj', 
                gas_limit = 550000, 
                gas_used = 0, 
                micro_blocks = [
                    '[0] 5b7c58118c4873f1f83bf0d1f93c58d608f1fb2692efbbe93483d8d03d7d6119 [1] 7504a82d1fcf28b03103b4e23bdf3b5045ac63d8c1b8af4bf533907f3b20ee9c [2] 6ea4f053dc37e0938dc3e729aa2f197dff3c13dcaa9558857a0d90260210950e [3] 31de23ba0a8a57e80a1d3a4a24ab378bd4a814ea0f0354f73ff9a6a46a785297'
                    ], 
                next_block_hash = '0x07939adbc3f5a6ba75968012acfe0fee9a351dca72c814e499fee554281b56b6 Block 1244298 Block 1244300', 
                previous_block_hash = '0xe347b6c09e54a582478f6ccc9f85a386616ad1367e9965e5409fab790e538d16 Block 1244296 Block 1244298', 
                timestamp = 1616069434, 
                transactions_count = 1
            )
        else :
            return GetZilliqaBlockDetailsByBlockHeightRI(
                block_hash = '0xf679d0b5387f0b0b3c3c1f368305512b23860888ba4415063d464a09b8bb6205 Block 1244297 Block 1244299',
                difficulty = '41.375',
                ds_block = 12443,
                ds_difficulty = '48.625',
                ds_leader = 'zil1k9hne0uu86wuj2n7qdqwhrm9uma0xn7ut42tsj',
                gas_limit = 550000,
                gas_used = 0,
                micro_blocks = [
                    '[0] 5b7c58118c4873f1f83bf0d1f93c58d608f1fb2692efbbe93483d8d03d7d6119 [1] 7504a82d1fcf28b03103b4e23bdf3b5045ac63d8c1b8af4bf533907f3b20ee9c [2] 6ea4f053dc37e0938dc3e729aa2f197dff3c13dcaa9558857a0d90260210950e [3] 31de23ba0a8a57e80a1d3a4a24ab378bd4a814ea0f0354f73ff9a6a46a785297'
                    ],
                next_block_hash = '0x07939adbc3f5a6ba75968012acfe0fee9a351dca72c814e499fee554281b56b6 Block 1244298 Block 1244300',
                previous_block_hash = '0xe347b6c09e54a582478f6ccc9f85a386616ad1367e9965e5409fab790e538d16 Block 1244296 Block 1244298',
                timestamp = 1616069434,
                transactions_count = 1,
        )
        """

    def testGetZilliqaBlockDetailsByBlockHeightRI(self):
        """Test GetZilliqaBlockDetailsByBlockHeightRI"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
