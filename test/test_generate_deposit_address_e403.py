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
from cryptoapis.models.generate_deposit_address_e403 import GenerateDepositAddressE403  # noqa: E501
from cryptoapis.rest import ApiException

class TestGenerateDepositAddressE403(unittest.TestCase):
    """GenerateDepositAddressE403 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GenerateDepositAddressE403
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GenerateDepositAddressE403`
        """
        model = cryptoapis.models.generate_deposit_address_e403.GenerateDepositAddressE403()  # noqa: E501
        if include_optional :
            return GenerateDepositAddressE403(
                code = 'wallet_as_a_service_provided_network_is_not_suitable_for_this_wallet_type', 
                message = 'This wallet is not for the provided network.', 
                details = [
                    cryptoapis.models.banned_ip_address_details_inner.BannedIpAddress_details_inner(
                        attribute = 'attribute which content caused the error', 
                        message = 'message describing the error', )
                    ]
            )
        else :
            return GenerateDepositAddressE403(
                code = 'wallet_as_a_service_provided_network_is_not_suitable_for_this_wallet_type',
                message = 'This wallet is not for the provided network.',
        )
        """

    def testGenerateDepositAddressE403(self):
        """Test GenerateDepositAddressE403"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
