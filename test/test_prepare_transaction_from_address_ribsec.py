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
from cryptoapis.models.prepare_transaction_from_address_ribsec import PrepareTransactionFromAddressRIBSEC  # noqa: E501
from cryptoapis.rest import ApiException

class TestPrepareTransactionFromAddressRIBSEC(unittest.TestCase):
    """PrepareTransactionFromAddressRIBSEC unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PrepareTransactionFromAddressRIBSEC
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PrepareTransactionFromAddressRIBSEC`
        """
        model = cryptoapis.models.prepare_transaction_from_address_ribsec.PrepareTransactionFromAddressRIBSEC()  # noqa: E501
        if include_optional :
            return PrepareTransactionFromAddressRIBSEC(
                fee = cryptoapis.models.prepare_transaction_from_address_ribsbsc_fee.PrepareTransactionFromAddressRIBSBSC_fee(
                    gas_limit = '21220', 
                    gas_price = '47125353', ), 
                transaction_type = 'legacy-transaction', 
                unit = 'WEI'
            )
        else :
            return PrepareTransactionFromAddressRIBSEC(
                fee = cryptoapis.models.prepare_transaction_from_address_ribsbsc_fee.PrepareTransactionFromAddressRIBSBSC_fee(
                    gas_limit = '21220', 
                    gas_price = '47125353', ),
                transaction_type = 'legacy-transaction',
                unit = 'WEI',
        )
        """

    def testPrepareTransactionFromAddressRIBSEC(self):
        """Test PrepareTransactionFromAddressRIBSEC"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()