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
from cryptoapis.models.get_xrp_ripple_address_details_ri import GetXRPRippleAddressDetailsRI  # noqa: E501
from cryptoapis.rest import ApiException

class TestGetXRPRippleAddressDetailsRI(unittest.TestCase):
    """GetXRPRippleAddressDetailsRI unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetXRPRippleAddressDetailsRI
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetXRPRippleAddressDetailsRI`
        """
        model = cryptoapis.models.get_xrp_ripple_address_details_ri.GetXRPRippleAddressDetailsRI()  # noqa: E501
        if include_optional :
            return GetXRPRippleAddressDetailsRI(
                balance = cryptoapis.models.get_xrp_ripple_address_details_ri_balance.GetXRPRippleAddressDetailsRI_balance(
                    amount = '22.0000', 
                    unit = 'XRP', ), 
                incoming_transactions_count = 1, 
                outgoing_transactions_count = 1, 
                sequence = 25648975, 
                transactions_count = 2
            )
        else :
            return GetXRPRippleAddressDetailsRI(
                balance = cryptoapis.models.get_xrp_ripple_address_details_ri_balance.GetXRPRippleAddressDetailsRI_balance(
                    amount = '22.0000', 
                    unit = 'XRP', ),
                incoming_transactions_count = 1,
                outgoing_transactions_count = 1,
                sequence = 25648975,
                transactions_count = 2,
        )
        """

    def testGetXRPRippleAddressDetailsRI(self):
        """Test GetXRPRippleAddressDetailsRI"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
