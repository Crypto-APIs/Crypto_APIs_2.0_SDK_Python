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
from cryptoapis.models.get_transaction_details_by_transaction_idribsl_vin_inner import GetTransactionDetailsByTransactionIDRIBSLVinInner  # noqa: E501
from cryptoapis.rest import ApiException

class TestGetTransactionDetailsByTransactionIDRIBSLVinInner(unittest.TestCase):
    """GetTransactionDetailsByTransactionIDRIBSLVinInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetTransactionDetailsByTransactionIDRIBSLVinInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetTransactionDetailsByTransactionIDRIBSLVinInner`
        """
        model = cryptoapis.models.get_transaction_details_by_transaction_idribsl_vin_inner.GetTransactionDetailsByTransactionIDRIBSLVinInner()  # noqa: E501
        if include_optional :
            return GetTransactionDetailsByTransactionIDRIBSLVinInner(
                addresses = [
                    'LZ891CJWn54CpE6yJ4T3mzP8Xxwrg9gDpH'
                    ], 
                coinbase = '0399d620046183f4502cfabe6d6d54cff85e53693837dc613bc4cc4b78986c2193a4e2902e3da62aa311957f50844000000000000000042f4c502f08220000b0e1110000', 
                script_sig = cryptoapis.models.get_transaction_details_by_transaction_idribsl_vin_inner_script_sig.GetTransactionDetailsByTransactionIDRIBSL_vin_inner_scriptSig(
                    asm = '3045022100f031442894c0fd60c195fbdb29c0bf72f143a815689b8840cd31ec31cc6a7721022028f74f0869e4666761c9ba1035cc714528a17de873dfc7b3a541d29f3942a2d8[ALL] 028c533b6c0ce0ad714a8af36b64d207c4f61cd6d5af210362447c92b4105a4fab', 
                    hex = '483045022100f031442894c0fd60c195fbdb29c0bf72f143a815689b8840cd31ec31cc6a7721022028f74f0869e4666761c9ba1035cc714528a17de873dfc7b3a541d29f3942a2d80121028c533b6c0ce0ad714a8af36b64d207c4f61cd6d5af210362447c92b4105a4fab', 
                    type = 'scripthash', ), 
                sequence = 4294967294, 
                txid = '1db56e1e8dfab84f6f0e33f8ddb160c9b16286471a3b486d79ea85bcf4d076b2', 
                txinwitness = [
                    '304402204e88dfe79e58b640908812c496ea74d2941c23e70ee3d93ebd469dbd136afe0c02203d7631427c0b5cb96e8a8b23b6c8c0c8112ecb5fb020ee2a7a70841564ed679b01'
                    ], 
                value = '0.0225', 
                vout = 1
            )
        else :
            return GetTransactionDetailsByTransactionIDRIBSLVinInner(
                addresses = [
                    'LZ891CJWn54CpE6yJ4T3mzP8Xxwrg9gDpH'
                    ],
                script_sig = cryptoapis.models.get_transaction_details_by_transaction_idribsl_vin_inner_script_sig.GetTransactionDetailsByTransactionIDRIBSL_vin_inner_scriptSig(
                    asm = '3045022100f031442894c0fd60c195fbdb29c0bf72f143a815689b8840cd31ec31cc6a7721022028f74f0869e4666761c9ba1035cc714528a17de873dfc7b3a541d29f3942a2d8[ALL] 028c533b6c0ce0ad714a8af36b64d207c4f61cd6d5af210362447c92b4105a4fab', 
                    hex = '483045022100f031442894c0fd60c195fbdb29c0bf72f143a815689b8840cd31ec31cc6a7721022028f74f0869e4666761c9ba1035cc714528a17de873dfc7b3a541d29f3942a2d80121028c533b6c0ce0ad714a8af36b64d207c4f61cd6d5af210362447c92b4105a4fab', 
                    type = 'scripthash', ),
                sequence = 4294967294,
                txinwitness = [
                    '304402204e88dfe79e58b640908812c496ea74d2941c23e70ee3d93ebd469dbd136afe0c02203d7631427c0b5cb96e8a8b23b6c8c0c8112ecb5fb020ee2a7a70841564ed679b01'
                    ],
        )
        """

    def testGetTransactionDetailsByTransactionIDRIBSLVinInner(self):
        """Test GetTransactionDetailsByTransactionIDRIBSLVinInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
