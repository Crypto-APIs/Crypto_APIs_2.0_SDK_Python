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
from cryptoapis.models.prepare_a_fungible_token_transfer_from_address_ribse import PrepareAFungibleTokenTransferFromAddressRIBSE  # noqa: E501
from cryptoapis.rest import ApiException

class TestPrepareAFungibleTokenTransferFromAddressRIBSE(unittest.TestCase):
    """PrepareAFungibleTokenTransferFromAddressRIBSE unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PrepareAFungibleTokenTransferFromAddressRIBSE
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PrepareAFungibleTokenTransferFromAddressRIBSE`
        """
        model = cryptoapis.models.prepare_a_fungible_token_transfer_from_address_ribse.PrepareAFungibleTokenTransferFromAddressRIBSE()  # noqa: E501
        if include_optional :
            return PrepareAFungibleTokenTransferFromAddressRIBSE(
                data_hex = '0x0079006f00750072004100640064006900740069006f006e0061006c00440061007400610048006500720065', 
                sig_hash = '9f59f25bc9f6cbff293ceee32c1fb25ae82fab23a99b860e26cad800ceadd123', 
                fee = cryptoapis.models.prepare_a_fungible_token_transfer_from_address_ribse_fee.PrepareAFungibleTokenTransferFromAddressRIBSE_fee(
                    gas_limit = '552020', 
                    gas_price = '2500000007', 
                    max_fee_per_gas = '2000000008', 
                    max_priority_fee_per_gas = '2000000000', ), 
                transaction_type = 'access-list-transaction'
            )
        else :
            return PrepareAFungibleTokenTransferFromAddressRIBSE(
                sig_hash = '9f59f25bc9f6cbff293ceee32c1fb25ae82fab23a99b860e26cad800ceadd123',
                fee = cryptoapis.models.prepare_a_fungible_token_transfer_from_address_ribse_fee.PrepareAFungibleTokenTransferFromAddressRIBSE_fee(
                    gas_limit = '552020', 
                    gas_price = '2500000007', 
                    max_fee_per_gas = '2000000008', 
                    max_priority_fee_per_gas = '2000000000', ),
                transaction_type = 'access-list-transaction',
        )
        """

    def testPrepareAFungibleTokenTransferFromAddressRIBSE(self):
        """Test PrepareAFungibleTokenTransferFromAddressRIBSE"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()