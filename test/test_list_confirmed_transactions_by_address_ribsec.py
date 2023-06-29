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
from cryptoapis.models.list_confirmed_transactions_by_address_ribsec import ListConfirmedTransactionsByAddressRIBSEC  # noqa: E501
from cryptoapis.rest import ApiException

class TestListConfirmedTransactionsByAddressRIBSEC(unittest.TestCase):
    """ListConfirmedTransactionsByAddressRIBSEC unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ListConfirmedTransactionsByAddressRIBSEC
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListConfirmedTransactionsByAddressRIBSEC`
        """
        model = cryptoapis.models.list_confirmed_transactions_by_address_ribsec.ListConfirmedTransactionsByAddressRIBSEC()  # noqa: E501
        if include_optional :
            return ListConfirmedTransactionsByAddressRIBSEC(
                contract = '0x20fe562d797a42dcb3399062ae9546cd06f63280', 
                gas_limit = '21000', 
                gas_price = cryptoapis.models.list_confirmed_transactions_by_address_ribsec_gas_price.ListConfirmedTransactionsByAddressRIBSEC_gasPrice(
                    amount = '21000', 
                    unit = 'ETC', ), 
                gas_used = '21000', 
                input_data = '0xa9059cbb000000000000000000000000acc59ec2f7119dc7a9e69dcd124cff75caae05bf0000000000000000000000000000000000000000000000000000000000989680', 
                internal_transactions_count = 2, 
                nonce = 16, 
                token_transfers_count = 2, 
                transaction_status = '0x1'
            )
        else :
            return ListConfirmedTransactionsByAddressRIBSEC(
                gas_limit = '21000',
                gas_price = cryptoapis.models.list_confirmed_transactions_by_address_ribsec_gas_price.ListConfirmedTransactionsByAddressRIBSEC_gasPrice(
                    amount = '21000', 
                    unit = 'ETC', ),
                gas_used = '21000',
                internal_transactions_count = 2,
                nonce = 16,
                token_transfers_count = 2,
                transaction_status = '0x1',
        )
        """

    def testListConfirmedTransactionsByAddressRIBSEC(self):
        """Test ListConfirmedTransactionsByAddressRIBSEC"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
