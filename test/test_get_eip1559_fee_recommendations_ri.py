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
from cryptoapis.models.get_eip1559_fee_recommendations_ri import GetEIP1559FeeRecommendationsRI  # noqa: E501
from cryptoapis.rest import ApiException

class TestGetEIP1559FeeRecommendationsRI(unittest.TestCase):
    """GetEIP1559FeeRecommendationsRI unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetEIP1559FeeRecommendationsRI
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetEIP1559FeeRecommendationsRI`
        """
        model = cryptoapis.models.get_eip1559_fee_recommendations_ri.GetEIP1559FeeRecommendationsRI()  # noqa: E501
        if include_optional :
            return GetEIP1559FeeRecommendationsRI(
                base_fee_per_gas = cryptoapis.models.get_eip1559_fee_recommendations_ri_base_fee_per_gas.GetEIP1559FeeRecommendationsRI_baseFeePerGas(
                    unit = 'WEI', 
                    value = '45265143502', ), 
                max_fee_per_gas = cryptoapis.models.get_eip1559_fee_recommendations_ri_max_fee_per_gas.GetEIP1559FeeRecommendationsRI_maxFeePerGas(
                    fast = '75235090892', 
                    slow = '67416761254', 
                    standard = '69996407508', 
                    unit = 'WEI', ), 
                max_priority_fee_per_gas = cryptoapis.models.get_eip1559_fee_recommendations_ri_max_priority_fee_per_gas.GetEIP1559FeeRecommendationsRI_maxPriorityFeePerGas(
                    fast = '47085140300', 
                    slow = '37331114417', 
                    standard = '41987372497', 
                    unit = 'WEI', )
            )
        else :
            return GetEIP1559FeeRecommendationsRI(
                base_fee_per_gas = cryptoapis.models.get_eip1559_fee_recommendations_ri_base_fee_per_gas.GetEIP1559FeeRecommendationsRI_baseFeePerGas(
                    unit = 'WEI', 
                    value = '45265143502', ),
                max_fee_per_gas = cryptoapis.models.get_eip1559_fee_recommendations_ri_max_fee_per_gas.GetEIP1559FeeRecommendationsRI_maxFeePerGas(
                    fast = '75235090892', 
                    slow = '67416761254', 
                    standard = '69996407508', 
                    unit = 'WEI', ),
                max_priority_fee_per_gas = cryptoapis.models.get_eip1559_fee_recommendations_ri_max_priority_fee_per_gas.GetEIP1559FeeRecommendationsRI_maxPriorityFeePerGas(
                    fast = '47085140300', 
                    slow = '37331114417', 
                    standard = '41987372497', 
                    unit = 'WEI', ),
        )
        """

    def testGetEIP1559FeeRecommendationsRI(self):
        """Test GetEIP1559FeeRecommendationsRI"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
