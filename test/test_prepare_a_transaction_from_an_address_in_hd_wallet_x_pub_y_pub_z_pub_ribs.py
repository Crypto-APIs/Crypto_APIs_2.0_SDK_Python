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
from cryptoapis.models.prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_ribs import PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBS  # noqa: E501
from cryptoapis.rest import ApiException

class TestPrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBS(unittest.TestCase):
    """PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBS unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBS
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBS`
        """
        model = cryptoapis.models.prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_ribs.PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBS()  # noqa: E501
        if include_optional :
            return PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBS(
                data_hex = '0x0079006f00750072004100640064006900740069006f006e0061006c00440061007400610048006500720065', 
                derivation_index = 100, 
                fee = cryptoapis.models.prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_ribsx_fee.PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBSX_fee(
                    fee_in_drops = '18', 
                    fee_in_xrp = '0.000018', ), 
                nonce = '0', 
                transaction_type = 'legacy-transaction', 
                unit = 'XRP', 
                data = '000000000000000000000000b6d4181ff1e6a1c4f9e480b2696576c4c8c2508c0000000000000000000000000000000000000000000000000000000004f27ac0', 
                expiration = 1666098830000, 
                raw_data = cryptoapis.models.prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_ribst_raw_data.PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBST_rawData(
                    contract = cryptoapis.models.prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_ribst_raw_data_contract.PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBST_rawData_contract(
                        parameter = cryptoapis.models.prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_ribst_raw_data_contract_parameter.PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBST_rawData_contract_parameter(
                            amount = '3', ), ), ), 
                raw_data_hex = '0a029759220830c83aa1c96f007540f0a4b1d9be305a65080112610a2d747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e5472616e73666572436f6e747261637412300a1541d1df5daa4666a5e9f1aae399dc88ec970b23729d121541ede830672838f5096ba2388f2edbeec762f140dc180370ae9ed3b0be30', 
                recipient = 'TXf9JJVsAoGRHUKyhyKbbgcR6F59AN8tgg', 
                ref_block_bytes = '988f', 
                ref_block_hash = 'ba4cba4757883442', 
                sender = '41c36a60df8cf3adf2be1d786800db7ea6dba36578', 
                timestamp = 1666013402728, 
                transaction_id = 'aea90d9be36108ed5ef821c840418d03ccc4f9cd7e5be5eb9021d588c172a36d', 
                type = 'TransferContract', 
                type_url = 'exampleTypeUrl', 
                visible = True, 
                public_key = '03e2f48ffe9b2a3dcdcfe60a308c89fd0658b18a9507f45bd3ab1e152f8b6eb05f', 
                sequence = '31715632'
            )
        else :
            return PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBS(
                data_hex = '0x0079006f00750072004100640064006900740069006f006e0061006c00440061007400610048006500720065',
                derivation_index = 100,
                fee = cryptoapis.models.prepare_a_transaction_from_an_address_in_hd_wallet_x_pub_y_pub_z_pub_ribsx_fee.PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBSX_fee(
                    fee_in_drops = '18', 
                    fee_in_xrp = '0.000018', ),
                nonce = '0',
                transaction_type = 'legacy-transaction',
                unit = 'XRP',
                data = '000000000000000000000000b6d4181ff1e6a1c4f9e480b2696576c4c8c2508c0000000000000000000000000000000000000000000000000000000004f27ac0',
                expiration = 1666098830000,
                raw_data_hex = '0a029759220830c83aa1c96f007540f0a4b1d9be305a65080112610a2d747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e5472616e73666572436f6e747261637412300a1541d1df5daa4666a5e9f1aae399dc88ec970b23729d121541ede830672838f5096ba2388f2edbeec762f140dc180370ae9ed3b0be30',
                recipient = 'TXf9JJVsAoGRHUKyhyKbbgcR6F59AN8tgg',
                ref_block_bytes = '988f',
                ref_block_hash = 'ba4cba4757883442',
                sender = '41c36a60df8cf3adf2be1d786800db7ea6dba36578',
                timestamp = 1666013402728,
                transaction_id = 'aea90d9be36108ed5ef821c840418d03ccc4f9cd7e5be5eb9021d588c172a36d',
                type = 'TransferContract',
                type_url = 'exampleTypeUrl',
                visible = True,
                public_key = '03e2f48ffe9b2a3dcdcfe60a308c89fd0658b18a9507f45bd3ab1e152f8b6eb05f',
                sequence = '31715632',
        )
        """

    def testPrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBS(self):
        """Test PrepareATransactionFromAnAddressInHDWalletXPubYPubZPubRIBS"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
