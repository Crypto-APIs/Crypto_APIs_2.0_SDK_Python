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
from cryptoapis.models.get_transaction_details_by_transaction_id_from_callback_ribsec import GetTransactionDetailsByTransactionIDFromCallbackRIBSEC  # noqa: E501
from cryptoapis.rest import ApiException

class TestGetTransactionDetailsByTransactionIDFromCallbackRIBSEC(unittest.TestCase):
    """GetTransactionDetailsByTransactionIDFromCallbackRIBSEC unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetTransactionDetailsByTransactionIDFromCallbackRIBSEC
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetTransactionDetailsByTransactionIDFromCallbackRIBSEC`
        """
        model = cryptoapis.models.get_transaction_details_by_transaction_id_from_callback_ribsec.GetTransactionDetailsByTransactionIDFromCallbackRIBSEC()  # noqa: E501
        if include_optional :
            return GetTransactionDetailsByTransactionIDFromCallbackRIBSEC(
                contract = '0x20fe562d797a42dcb3399062ae9546cd06f63280', 
                gas_limit = '552020', 
                gas_price = cryptoapis.models.get_transaction_details_by_transaction_idribsec_gas_price.GetTransactionDetailsByTransactionIDRIBSEC_gasPrice(
                    amount = '2994782934', 
                    unit = 'WEI', ), 
                gas_used = '24673', 
                input_data = '0xa9059cbb000000000000000000000000acc59ec2f7119dc7a9e69dcd124cff75caae05bf0000000000000000000000000000000000000000000000000000000000989680', 
                nonce = 16
            )
        else :
            return GetTransactionDetailsByTransactionIDFromCallbackRIBSEC(
                contract = '0x20fe562d797a42dcb3399062ae9546cd06f63280',
                gas_limit = '552020',
                gas_price = cryptoapis.models.get_transaction_details_by_transaction_idribsec_gas_price.GetTransactionDetailsByTransactionIDRIBSEC_gasPrice(
                    amount = '2994782934', 
                    unit = 'WEI', ),
                gas_used = '24673',
                input_data = '0xa9059cbb000000000000000000000000acc59ec2f7119dc7a9e69dcd124cff75caae05bf0000000000000000000000000000000000000000000000000000000000989680',
                nonce = 16,
        )
        """

    def testGetTransactionDetailsByTransactionIDFromCallbackRIBSEC(self):
        """Test GetTransactionDetailsByTransactionIDFromCallbackRIBSEC"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
