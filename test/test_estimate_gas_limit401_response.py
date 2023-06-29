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
from cryptoapis.models.estimate_gas_limit401_response import EstimateGasLimit401Response  # noqa: E501
from cryptoapis.rest import ApiException

class TestEstimateGasLimit401Response(unittest.TestCase):
    """EstimateGasLimit401Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test EstimateGasLimit401Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EstimateGasLimit401Response`
        """
        model = cryptoapis.models.estimate_gas_limit401_response.EstimateGasLimit401Response()  # noqa: E501
        if include_optional :
            return EstimateGasLimit401Response(
                api_version = '2021-03-20', 
                request_id = '601c1710034ed6d407996b30', 
                context = 'yourExampleString', 
                error = cryptoapis.models.estimate_gas_limit_e401.EstimateGasLimitE401()
            )
        else :
            return EstimateGasLimit401Response(
                api_version = '2021-03-20',
                request_id = '601c1710034ed6d407996b30',
                error = cryptoapis.models.estimate_gas_limit_e401.EstimateGasLimitE401(),
        )
        """

    def testEstimateGasLimit401Response(self):
        """Test EstimateGasLimit401Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()