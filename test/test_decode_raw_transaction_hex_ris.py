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
from cryptoapis.models.decode_raw_transaction_hex_ris import DecodeRawTransactionHexRIS  # noqa: E501
from cryptoapis.rest import ApiException

class TestDecodeRawTransactionHexRIS(unittest.TestCase):
    """DecodeRawTransactionHexRIS unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DecodeRawTransactionHexRIS
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DecodeRawTransactionHexRIS`
        """
        model = cryptoapis.models.decode_raw_transaction_hex_ris.DecodeRawTransactionHexRIS()  # noqa: E501
        if include_optional :
            return DecodeRawTransactionHexRIS(
                locktime = 1781965, 
                transaction_hash = 'e8ae0fed2699de544f48a9209085a6fe85e4697f3cc5625a85fd5021299e8f82', 
                v_size = 141, 
                version = 4, 
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
                weight = 245, 
                approximate_fee = '0.00016932', 
                approximate_minimum_required_fee = '0.000021', 
                gas_limit = '552020', 
                gas_paid_for_data = '0', 
                gas_price = '2994782927', 
                input_data = '0x34', 
                max_fee_per_gas = '0.000000149248157973', 
                max_fee_priority_per_gas = '0.000000002', 
                nonce = 16, 
                r = '0xc297031972fe2d4926e01e66768d669882ace256f8a8397f757af341f5e7c49', 
                recipient = '0x59d9d70DC4717cc9F3c1f7Bf3Fb9B62430872725', 
                s = '0x7b717faa31c5edf9332e1cd5fa3f736838a9262834ece621bb3c30671b66ab05', 
                sender = '0x4dF189c73C714dd636a99AA4f3317CcD72a05d62', 
                type = 0, 
                v = '0x26', 
                value = '11.25', 
                expiry_height = 0, 
                overwintered = True, 
                saplinged = True, 
                value_balance = '0', 
                version_group_id = '2301567109'
            )
        else :
            return DecodeRawTransactionHexRIS(
                locktime = 1781965,
                transaction_hash = 'e8ae0fed2699de544f48a9209085a6fe85e4697f3cc5625a85fd5021299e8f82',
                v_size = 141,
                version = 4,
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
                gas_limit = '552020',
                nonce = 16,
                recipient = '0x59d9d70DC4717cc9F3c1f7Bf3Fb9B62430872725',
                sender = '0x4dF189c73C714dd636a99AA4f3317CcD72a05d62',
                type = 0,
                expiry_height = 0,
                overwintered = True,
                saplinged = True,
                value_balance = '0',
                version_group_id = '2301567109',
        )
        """

    def testDecodeRawTransactionHexRIS(self):
        """Test DecodeRawTransactionHexRIS"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
