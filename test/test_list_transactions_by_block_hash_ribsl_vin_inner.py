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
from cryptoapis.models.list_transactions_by_block_hash_ribsl_vin_inner import ListTransactionsByBlockHashRIBSLVinInner  # noqa: E501
from cryptoapis.rest import ApiException

class TestListTransactionsByBlockHashRIBSLVinInner(unittest.TestCase):
    """ListTransactionsByBlockHashRIBSLVinInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ListTransactionsByBlockHashRIBSLVinInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListTransactionsByBlockHashRIBSLVinInner`
        """
        model = cryptoapis.models.list_transactions_by_block_hash_ribsl_vin_inner.ListTransactionsByBlockHashRIBSLVinInner()  # noqa: E501
        if include_optional :
            return ListTransactionsByBlockHashRIBSLVinInner(
                addresses = [
                    'tltc1q48j65qu543qvzq0u6eedflsdks56zja8wfqs29'
                    ], 
                coinbase = '0382221c04d6e05160086800002d090000000d2f6e6f64655374726174756d2f', 
                script_sig = cryptoapis.models.list_transactions_by_block_hash_ribsl_vin_inner_script_sig.ListTransactionsByBlockHashRIBSL_vin_inner_scriptSig(
                    asm = '0 a9e5aa0394ac40c101fcd672d4fe0db429a14ba7', 
                    hex = '0014a9e5aa0394ac40c101fcd672d4fe0db429a14ba7', 
                    type = 'scripthash', ), 
                sequence = '4294967294', 
                txid = '1db56e1e8dfab84f6f0e33f8ddb160c9b16286471a3b486d79ea85bcf4d076b2', 
                txinwitness = [
                    '304402204e88dfe79e58b640908812c496ea74d2941c23e70ee3d93ebd469dbd136afe0c02203d7631427c0b5cb96e8a8b23b6c8c0c8112ecb5fb020ee2a7a70841564ed679b01'
                    ], 
                value = '0.0225', 
                vout = 2
            )
        else :
            return ListTransactionsByBlockHashRIBSLVinInner(
                addresses = [
                    'tltc1q48j65qu543qvzq0u6eedflsdks56zja8wfqs29'
                    ],
                script_sig = cryptoapis.models.list_transactions_by_block_hash_ribsl_vin_inner_script_sig.ListTransactionsByBlockHashRIBSL_vin_inner_scriptSig(
                    asm = '0 a9e5aa0394ac40c101fcd672d4fe0db429a14ba7', 
                    hex = '0014a9e5aa0394ac40c101fcd672d4fe0db429a14ba7', 
                    type = 'scripthash', ),
                sequence = '4294967294',
                txid = '1db56e1e8dfab84f6f0e33f8ddb160c9b16286471a3b486d79ea85bcf4d076b2',
                txinwitness = [
                    '304402204e88dfe79e58b640908812c496ea74d2941c23e70ee3d93ebd469dbd136afe0c02203d7631427c0b5cb96e8a8b23b6c8c0c8112ecb5fb020ee2a7a70841564ed679b01'
                    ],
                value = '0.0225',
                vout = 2,
        )
        """

    def testListTransactionsByBlockHashRIBSLVinInner(self):
        """Test ListTransactionsByBlockHashRIBSLVinInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()