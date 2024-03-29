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
from cryptoapis.models.get_wallet_transaction_details_by_transaction_idribsl_vin_inner_script_sig import GetWalletTransactionDetailsByTransactionIDRIBSLVinInnerScriptSig  # noqa: E501
from cryptoapis.rest import ApiException

class TestGetWalletTransactionDetailsByTransactionIDRIBSLVinInnerScriptSig(unittest.TestCase):
    """GetWalletTransactionDetailsByTransactionIDRIBSLVinInnerScriptSig unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetWalletTransactionDetailsByTransactionIDRIBSLVinInnerScriptSig
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetWalletTransactionDetailsByTransactionIDRIBSLVinInnerScriptSig`
        """
        model = cryptoapis.models.get_wallet_transaction_details_by_transaction_idribsl_vin_inner_script_sig.GetWalletTransactionDetailsByTransactionIDRIBSLVinInnerScriptSig()  # noqa: E501
        if include_optional :
            return GetWalletTransactionDetailsByTransactionIDRIBSLVinInnerScriptSig(
                asm = '3045022100f031442894c0fd60c195fbdb29c0bf72f143a815689b8840cd31ec31cc6a7721022028f74f0869e4666761c9ba1035cc714528a17de873dfc7b3a541d29f3942a2d8[ALL] 028c533b6c0ce0ad714a8af36b64d207c4f61cd6d5af210362447c92b4105a4fab', 
                hex = '483045022100f031442894c0fd60c195fbdb29c0bf72f143a815689b8840cd31ec31cc6a7721022028f74f0869e4666761c9ba1035cc714528a17de873dfc7b3a541d29f3942a2d80121028c533b6c0ce0ad714a8af36b64d207c4f61cd6d5af210362447c92b4105a4fab', 
                type = 'scripthash'
            )
        else :
            return GetWalletTransactionDetailsByTransactionIDRIBSLVinInnerScriptSig(
                asm = '3045022100f031442894c0fd60c195fbdb29c0bf72f143a815689b8840cd31ec31cc6a7721022028f74f0869e4666761c9ba1035cc714528a17de873dfc7b3a541d29f3942a2d8[ALL] 028c533b6c0ce0ad714a8af36b64d207c4f61cd6d5af210362447c92b4105a4fab',
                hex = '483045022100f031442894c0fd60c195fbdb29c0bf72f143a815689b8840cd31ec31cc6a7721022028f74f0869e4666761c9ba1035cc714528a17de873dfc7b3a541d29f3942a2d80121028c533b6c0ce0ad714a8af36b64d207c4f61cd6d5af210362447c92b4105a4fab',
                type = 'scripthash',
        )
        """

    def testGetWalletTransactionDetailsByTransactionIDRIBSLVinInnerScriptSig(self):
        """Test GetWalletTransactionDetailsByTransactionIDRIBSLVinInnerScriptSig"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
