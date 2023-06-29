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
from cryptoapis.models.get_latest_mined_xrp_ripple_block_r_data import GetLatestMinedXRPRippleBlockRData  # noqa: E501
from cryptoapis.rest import ApiException

class TestGetLatestMinedXRPRippleBlockRData(unittest.TestCase):
    """GetLatestMinedXRPRippleBlockRData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetLatestMinedXRPRippleBlockRData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetLatestMinedXRPRippleBlockRData`
        """
        model = cryptoapis.models.get_latest_mined_xrp_ripple_block_r_data.GetLatestMinedXRPRippleBlockRData()  # noqa: E501
        if include_optional :
            return GetLatestMinedXRPRippleBlockRData(
                item = cryptoapis.models.get_latest_mined_xrp_ripple_block_ri.GetLatestMinedXRPRippleBlockRI(
                    block_hash = 'f9b304b7933ef298142fdd58ad2dec414a5267dcbbd8a4fe9fc2c0a5f9dde050', 
                    block_height = 15975748, 
                    previous_block_hash = 'de9f9e5b68a1322a16f0d1217cf31765e9101764e6e2f3c7aa058b8c641da37a', 
                    timestamp = 1616430182, 
                    transactions_count = 1, 
                    total_coins = cryptoapis.models.get_latest_mined_xrp_ripple_block_ri_total_coins.GetLatestMinedXRPRippleBlockRI_totalCoins(
                        amount = '22.0012', 
                        unit = 'Drops', ), 
                    total_fees = cryptoapis.models.get_latest_mined_xrp_ripple_block_ri_total_fees.GetLatestMinedXRPRippleBlockRI_totalFees(
                        amount = '0.00001', 
                        unit = 'XRP', ), )
            )
        else :
            return GetLatestMinedXRPRippleBlockRData(
                item = cryptoapis.models.get_latest_mined_xrp_ripple_block_ri.GetLatestMinedXRPRippleBlockRI(
                    block_hash = 'f9b304b7933ef298142fdd58ad2dec414a5267dcbbd8a4fe9fc2c0a5f9dde050', 
                    block_height = 15975748, 
                    previous_block_hash = 'de9f9e5b68a1322a16f0d1217cf31765e9101764e6e2f3c7aa058b8c641da37a', 
                    timestamp = 1616430182, 
                    transactions_count = 1, 
                    total_coins = cryptoapis.models.get_latest_mined_xrp_ripple_block_ri_total_coins.GetLatestMinedXRPRippleBlockRI_totalCoins(
                        amount = '22.0012', 
                        unit = 'Drops', ), 
                    total_fees = cryptoapis.models.get_latest_mined_xrp_ripple_block_ri_total_fees.GetLatestMinedXRPRippleBlockRI_totalFees(
                        amount = '0.00001', 
                        unit = 'XRP', ), ),
        )
        """

    def testGetLatestMinedXRPRippleBlockRData(self):
        """Test GetLatestMinedXRPRippleBlockRData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
