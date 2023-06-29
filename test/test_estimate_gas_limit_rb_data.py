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
from cryptoapis.models.estimate_gas_limit_rb_data import EstimateGasLimitRBData  # noqa: E501
from cryptoapis.rest import ApiException

class TestEstimateGasLimitRBData(unittest.TestCase):
    """EstimateGasLimitRBData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test EstimateGasLimitRBData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EstimateGasLimitRBData`
        """
        model = cryptoapis.models.estimate_gas_limit_rb_data.EstimateGasLimitRBData()  # noqa: E501
        if include_optional :
            return EstimateGasLimitRBData(
                item = cryptoapis.models.estimate_gas_limit_rb_data_item.EstimateGasLimitRB_data_item(
                    additional_data = 'yourAdditionalString', 
                    amount = '0.002', 
                    recipient = '0xc065b539490f81b6c297c37b1925c3be2f190738', 
                    sender = '0x6f61e3c2fbb8c8be698bd0907ba6c04b62800fe5', )
            )
        else :
            return EstimateGasLimitRBData(
                item = cryptoapis.models.estimate_gas_limit_rb_data_item.EstimateGasLimitRB_data_item(
                    additional_data = 'yourAdditionalString', 
                    amount = '0.002', 
                    recipient = '0xc065b539490f81b6c297c37b1925c3be2f190738', 
                    sender = '0x6f61e3c2fbb8c8be698bd0907ba6c04b62800fe5', ),
        )
        """

    def testEstimateGasLimitRBData(self):
        """Test EstimateGasLimitRBData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
