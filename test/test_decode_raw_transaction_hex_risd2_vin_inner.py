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
from cryptoapis.models.decode_raw_transaction_hex_risd2_vin_inner import DecodeRawTransactionHexRISD2VinInner  # noqa: E501
from cryptoapis.rest import ApiException

class TestDecodeRawTransactionHexRISD2VinInner(unittest.TestCase):
    """DecodeRawTransactionHexRISD2VinInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DecodeRawTransactionHexRISD2VinInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DecodeRawTransactionHexRISD2VinInner`
        """
        model = cryptoapis.models.decode_raw_transaction_hex_risd2_vin_inner.DecodeRawTransactionHexRISD2VinInner()  # noqa: E501
        if include_optional :
            return DecodeRawTransactionHexRISD2VinInner(
                address = 'DPzdWPsKaGvRn3AH7WjBpnNVHhAPELDY4o', 
                input_hash = '746b56225c5eee8c50c0bedd885d18d3fda37b846d59eb7434b5e365e73e4b60', 
                output_index = '2', 
                script_sig = cryptoapis.models.decode_raw_transaction_hex_risd2_vin_inner_script_sig.DecodeRawTransactionHexRISD2_vin_inner_scriptSig(
                    asm = '030483ff6271580681f4f7828c01df56d5aebfe982cbaa2922594be9eb6cf40206', 
                    hex = '21030483ff6271580681f4f7828c01df56d5aebfe982cbaa2922594be9eb6cf40206ac', 
                    type = 'scripthash', ), 
                sequence = '4294967295', 
                txinwitness = [
                    'qpq395ljesqakppupe3chd3n3jp60wd23ue00g66xx'
                    ]
            )
        else :
            return DecodeRawTransactionHexRISD2VinInner(
                script_sig = cryptoapis.models.decode_raw_transaction_hex_risd2_vin_inner_script_sig.DecodeRawTransactionHexRISD2_vin_inner_scriptSig(
                    asm = '030483ff6271580681f4f7828c01df56d5aebfe982cbaa2922594be9eb6cf40206', 
                    hex = '21030483ff6271580681f4f7828c01df56d5aebfe982cbaa2922594be9eb6cf40206ac', 
                    type = 'scripthash', ),
        )
        """

    def testDecodeRawTransactionHexRISD2VinInner(self):
        """Test DecodeRawTransactionHexRISD2VinInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()