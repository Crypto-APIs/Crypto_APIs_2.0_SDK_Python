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
from cryptoapis.models.list_confirmed_transactions_by_address_ribsl_vin_inner import ListConfirmedTransactionsByAddressRIBSLVinInner  # noqa: E501
from cryptoapis.rest import ApiException

class TestListConfirmedTransactionsByAddressRIBSLVinInner(unittest.TestCase):
    """ListConfirmedTransactionsByAddressRIBSLVinInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ListConfirmedTransactionsByAddressRIBSLVinInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListConfirmedTransactionsByAddressRIBSLVinInner`
        """
        model = cryptoapis.models.list_confirmed_transactions_by_address_ribsl_vin_inner.ListConfirmedTransactionsByAddressRIBSLVinInner()  # noqa: E501
        if include_optional :
            return ListConfirmedTransactionsByAddressRIBSLVinInner(
                addresses = [
                    'tltc1qcefwt8q647lstt5829exynqnecr9uxq9pk3yr5'
                    ], 
                coinbase = '0399d620046183f4502cfabe6d6d54cff85e53693837dc613bc4cc4b78986c2193a4e2902e3da62aa311957f50844000000000000000042f4c502f08220000b0e1110000', 
                script_sig = cryptoapis.models.list_confirmed_transactions_by_address_ribsl_vin_inner_script_sig.ListConfirmedTransactionsByAddressRIBSL_vin_inner_scriptSig(
                    asm = '0 eab6ff0ee1158241737dfa5c78449dc06cf021cc', 
                    hex = '0014eab6ff0ee1158241737dfa5c78449dc06cf021cc', 
                    type = 'scripthash', ), 
                sequence = '4294967294', 
                txid = '1db56e1e8dfab84f6f0e33f8ddb160c9b16286471a3b486d79ea85bcf4d076b2', 
                txinwitness = [
                    '304402204e88dfe79e58b640908812c496ea74d2941c23e70ee3d93ebd469dbd136afe0c02203d7631427c0b5cb96e8a8b23b6c8c0c8112ecb5fb020ee2a7a70841564ed679b01'
                    ], 
                value = '0.0225', 
                vout = 1
            )
        else :
            return ListConfirmedTransactionsByAddressRIBSLVinInner(
                addresses = [
                    'tltc1qcefwt8q647lstt5829exynqnecr9uxq9pk3yr5'
                    ],
                script_sig = cryptoapis.models.list_confirmed_transactions_by_address_ribsl_vin_inner_script_sig.ListConfirmedTransactionsByAddressRIBSL_vin_inner_scriptSig(
                    asm = '0 eab6ff0ee1158241737dfa5c78449dc06cf021cc', 
                    hex = '0014eab6ff0ee1158241737dfa5c78449dc06cf021cc', 
                    type = 'scripthash', ),
                sequence = '4294967294',
                txid = '1db56e1e8dfab84f6f0e33f8ddb160c9b16286471a3b486d79ea85bcf4d076b2',
                txinwitness = [
                    '304402204e88dfe79e58b640908812c496ea74d2941c23e70ee3d93ebd469dbd136afe0c02203d7631427c0b5cb96e8a8b23b6c8c0c8112ecb5fb020ee2a7a70841564ed679b01'
                    ],
        )
        """

    def testListConfirmedTransactionsByAddressRIBSLVinInner(self):
        """Test ListConfirmedTransactionsByAddressRIBSLVinInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
