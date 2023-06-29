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
from cryptoapis.models.prepare_a_non_fungible_token_transfer_from_address_r_data import PrepareANonFungibleTokenTransferFromAddressRData  # noqa: E501
from cryptoapis.rest import ApiException

class TestPrepareANonFungibleTokenTransferFromAddressRData(unittest.TestCase):
    """PrepareANonFungibleTokenTransferFromAddressRData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PrepareANonFungibleTokenTransferFromAddressRData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PrepareANonFungibleTokenTransferFromAddressRData`
        """
        model = cryptoapis.models.prepare_a_non_fungible_token_transfer_from_address_r_data.PrepareANonFungibleTokenTransferFromAddressRData()  # noqa: E501
        if include_optional :
            return PrepareANonFungibleTokenTransferFromAddressRData(
                item = cryptoapis.models.prepare_a_non_fungible_token_transfer_from_address_ri.PrepareANonFungibleTokenTransferFromAddressRI(
                    recipient = '0x5668213c59ab2612ecd948f98371d1d291098b5e', 
                    sender = '0xc6d46aba0c6e2eb6358c4e24804158cc4d847922', 
                    token_id = '14', 
                    blockchain_specific = cryptoapis.models.prepare_a_non_fungible_token_transfer_from_address_ribs.PrepareANonFungibleTokenTransferFromAddressRIBS(), )
            )
        else :
            return PrepareANonFungibleTokenTransferFromAddressRData(
                item = cryptoapis.models.prepare_a_non_fungible_token_transfer_from_address_ri.PrepareANonFungibleTokenTransferFromAddressRI(
                    recipient = '0x5668213c59ab2612ecd948f98371d1d291098b5e', 
                    sender = '0xc6d46aba0c6e2eb6358c4e24804158cc4d847922', 
                    token_id = '14', 
                    blockchain_specific = cryptoapis.models.prepare_a_non_fungible_token_transfer_from_address_ribs.PrepareANonFungibleTokenTransferFromAddressRIBS(), ),
        )
        """

    def testPrepareANonFungibleTokenTransferFromAddressRData(self):
        """Test PrepareANonFungibleTokenTransferFromAddressRData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
