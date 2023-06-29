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
from cryptoapis.models.create_coins_transaction_request_from_address_r_data import CreateCoinsTransactionRequestFromAddressRData  # noqa: E501
from cryptoapis.rest import ApiException

class TestCreateCoinsTransactionRequestFromAddressRData(unittest.TestCase):
    """CreateCoinsTransactionRequestFromAddressRData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreateCoinsTransactionRequestFromAddressRData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateCoinsTransactionRequestFromAddressRData`
        """
        model = cryptoapis.models.create_coins_transaction_request_from_address_r_data.CreateCoinsTransactionRequestFromAddressRData()  # noqa: E501
        if include_optional :
            return CreateCoinsTransactionRequestFromAddressRData(
                item = cryptoapis.models.create_coins_transaction_request_from_address_ri.CreateCoinsTransactionRequestFromAddressRI(
                    address_tag = 3999472835, 
                    callback_secret_key = 'yourSecretString', 
                    callback_url = 'https://example.com', 
                    classic_address = 'rA9bXGJcXvZKaWofrRphdJsBWzhyCfH3z', 
                    fee_priority = 'standard', 
                    note = 'yourAdditionalInformationhere', 
                    recipients = [
                        cryptoapis.models.create_coins_transaction_request_from_address_ri_recipients_inner.CreateCoinsTransactionRequestFromAddressRI_recipients_inner(
                            address = '0xc6d46aba0c6e2eb6358c4e24804158cc4d847922', 
                            address_tag = 3999472835, 
                            amount = '0.0023', 
                            classic_address = 'rA9bXGJcXvZKaWofrRphdJsBWzhyCfH3z', )
                        ], 
                    senders = cryptoapis.models.create_coins_transaction_request_from_address_ri_senders.CreateCoinsTransactionRequestFromAddressRI_senders(
                        address = '0x0902a667d6a3f287835e0a4593cae4167384abc6', ), 
                    transaction_request_id = '6017dd02a309213863be9e55', 
                    transaction_request_status = 'created', )
            )
        else :
            return CreateCoinsTransactionRequestFromAddressRData(
                item = cryptoapis.models.create_coins_transaction_request_from_address_ri.CreateCoinsTransactionRequestFromAddressRI(
                    address_tag = 3999472835, 
                    callback_secret_key = 'yourSecretString', 
                    callback_url = 'https://example.com', 
                    classic_address = 'rA9bXGJcXvZKaWofrRphdJsBWzhyCfH3z', 
                    fee_priority = 'standard', 
                    note = 'yourAdditionalInformationhere', 
                    recipients = [
                        cryptoapis.models.create_coins_transaction_request_from_address_ri_recipients_inner.CreateCoinsTransactionRequestFromAddressRI_recipients_inner(
                            address = '0xc6d46aba0c6e2eb6358c4e24804158cc4d847922', 
                            address_tag = 3999472835, 
                            amount = '0.0023', 
                            classic_address = 'rA9bXGJcXvZKaWofrRphdJsBWzhyCfH3z', )
                        ], 
                    senders = cryptoapis.models.create_coins_transaction_request_from_address_ri_senders.CreateCoinsTransactionRequestFromAddressRI_senders(
                        address = '0x0902a667d6a3f287835e0a4593cae4167384abc6', ), 
                    transaction_request_id = '6017dd02a309213863be9e55', 
                    transaction_request_status = 'created', ),
        )
        """

    def testCreateCoinsTransactionRequestFromAddressRData(self):
        """Test CreateCoinsTransactionRequestFromAddressRData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
