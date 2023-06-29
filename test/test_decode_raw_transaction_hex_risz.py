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
from cryptoapis.models.decode_raw_transaction_hex_risz import DecodeRawTransactionHexRISZ  # noqa: E501
from cryptoapis.rest import ApiException

class TestDecodeRawTransactionHexRISZ(unittest.TestCase):
    """DecodeRawTransactionHexRISZ unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DecodeRawTransactionHexRISZ
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DecodeRawTransactionHexRISZ`
        """
        model = cryptoapis.models.decode_raw_transaction_hex_risz.DecodeRawTransactionHexRISZ()  # noqa: E501
        if include_optional :
            return DecodeRawTransactionHexRISZ(
                expiry_height = 0, 
                locktime = 1781965, 
                overwintered = True, 
                saplinged = True, 
                transaction_hash = 'e8ae0fed2699de544f48a9209085a6fe85e4697f3cc5625a85fd5021299e8f82', 
                value_balance = '0', 
                version = 4, 
                version_group_id = '2301567109', 
                vin = [
                    cryptoapis.models.decode_raw_transaction_hex_risz_vin_inner.DecodeRawTransactionHexRISZ_vin_inner(
                        address = 't1ajyFP7GnauoDFaM8MqJx9ouQjKS3tbA7g', 
                        input_hash = '9dcaee77cd1806c4f9b0bac9ba17e4713fd04032f33be27b630ce499f7a35bd7', 
                        output_index = '1', 
                        script_sig = cryptoapis.models.decode_raw_transaction_hex_risz_vin_inner_script_sig.DecodeRawTransactionHexRISZ_vin_inner_scriptSig(
                            asm = 'OP_HASH160 ef775f1f997f122a062fff1a2d7443abd1f9c642 OP_EQUAL', 
                            hex = 'a914ef775f1f997f122a062fff1a2d7443abd1f9c64287', 
                            type = 'pubkeyhash', ), 
                        sequence = '4294967295', )
                    ], 
                vout = [
                    cryptoapis.models.decode_raw_transaction_hex_risz_vout_inner.DecodeRawTransactionHexRISZ_vout_inner(
                        script_pub_key = cryptoapis.models.decode_raw_transaction_hex_risz_vout_inner_script_pub_key.DecodeRawTransactionHexRISZ_vout_inner_scriptPubKey(
                            address = 't1ajyFP7GnauoDFaM8MqJx9ouQjKS3tbA7g', 
                            asm = 'OP_HASH160 ef775f1f997f122a062fff1a2d7443abd1f9c642 OP_EQUAL', 
                            hex = 'a914ef775f1f997f122a062fff1a2d7443abd1f9c64287', 
                            type = 'pubkeyhash', ), 
                        value = '2.50003291', )
                    ]
            )
        else :
            return DecodeRawTransactionHexRISZ(
                expiry_height = 0,
                locktime = 1781965,
                overwintered = True,
                saplinged = True,
                transaction_hash = 'e8ae0fed2699de544f48a9209085a6fe85e4697f3cc5625a85fd5021299e8f82',
                value_balance = '0',
                version = 4,
                version_group_id = '2301567109',
                vin = [
                    cryptoapis.models.decode_raw_transaction_hex_risz_vin_inner.DecodeRawTransactionHexRISZ_vin_inner(
                        address = 't1ajyFP7GnauoDFaM8MqJx9ouQjKS3tbA7g', 
                        input_hash = '9dcaee77cd1806c4f9b0bac9ba17e4713fd04032f33be27b630ce499f7a35bd7', 
                        output_index = '1', 
                        script_sig = cryptoapis.models.decode_raw_transaction_hex_risz_vin_inner_script_sig.DecodeRawTransactionHexRISZ_vin_inner_scriptSig(
                            asm = 'OP_HASH160 ef775f1f997f122a062fff1a2d7443abd1f9c642 OP_EQUAL', 
                            hex = 'a914ef775f1f997f122a062fff1a2d7443abd1f9c64287', 
                            type = 'pubkeyhash', ), 
                        sequence = '4294967295', )
                    ],
                vout = [
                    cryptoapis.models.decode_raw_transaction_hex_risz_vout_inner.DecodeRawTransactionHexRISZ_vout_inner(
                        script_pub_key = cryptoapis.models.decode_raw_transaction_hex_risz_vout_inner_script_pub_key.DecodeRawTransactionHexRISZ_vout_inner_scriptPubKey(
                            address = 't1ajyFP7GnauoDFaM8MqJx9ouQjKS3tbA7g', 
                            asm = 'OP_HASH160 ef775f1f997f122a062fff1a2d7443abd1f9c642 OP_EQUAL', 
                            hex = 'a914ef775f1f997f122a062fff1a2d7443abd1f9c64287', 
                            type = 'pubkeyhash', ), 
                        value = '2.50003291', )
                    ],
        )
        """

    def testDecodeRawTransactionHexRISZ(self):
        """Test DecodeRawTransactionHexRISZ"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
