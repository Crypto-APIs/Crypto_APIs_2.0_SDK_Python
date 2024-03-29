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
from cryptoapis.models.get_transaction_details_by_transaction_id_from_callback_ri import GetTransactionDetailsByTransactionIDFromCallbackRI  # noqa: E501
from cryptoapis.rest import ApiException

class TestGetTransactionDetailsByTransactionIDFromCallbackRI(unittest.TestCase):
    """GetTransactionDetailsByTransactionIDFromCallbackRI unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetTransactionDetailsByTransactionIDFromCallbackRI
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetTransactionDetailsByTransactionIDFromCallbackRI`
        """
        model = cryptoapis.models.get_transaction_details_by_transaction_id_from_callback_ri.GetTransactionDetailsByTransactionIDFromCallbackRI()  # noqa: E501
        if include_optional :
            return GetTransactionDetailsByTransactionIDFromCallbackRI(
                index = 1, 
                is_confirmed = True, 
                mined_in_block_hash = '00000000407f119ecb74b44229228910400aaeb9f4e3b9869955b85a53e9b7db', 
                mined_in_block_height = 1939750, 
                recipients = [
                    cryptoapis.models.get_transaction_details_by_transaction_idri_recipients_inner.GetTransactionDetailsByTransactionIDRI_recipients_inner(
                        address = '2MzakdGTEp8SMWEHKwKM4HYv6uNCBXtHpkV', 
                        amount = '0.000144', )
                    ], 
                senders = [
                    cryptoapis.models.get_transaction_details_by_transaction_idri_senders_inner.GetTransactionDetailsByTransactionIDRI_senders_inner(
                        address = '2N5PcdirZUzKF9bWuGdugNuzcQrCbBudxv1', 
                        amount = '0.00873472', )
                    ], 
                timestamp = 1582202940, 
                transaction_hash = '1ec73b0f61359927d02376b35993b756b1097cb9a857bec23da4c98c4977d2b2', 
                fee = cryptoapis.models.get_transaction_details_by_transaction_id_from_callback_ri_fee.GetTransactionDetailsByTransactionIDFromCallbackRI_fee(
                    amount = '0.00000300', 
                    unit = 'BTC', ), 
                transaction_id = '', 
                blockchain_specific = cryptoapis.models.get_transaction_details_by_transaction_id_from_callback_ribs.GetTransactionDetailsByTransactionIDFromCallbackRIBS()
            )
        else :
            return GetTransactionDetailsByTransactionIDFromCallbackRI(
                index = 1,
                is_confirmed = True,
                mined_in_block_hash = '00000000407f119ecb74b44229228910400aaeb9f4e3b9869955b85a53e9b7db',
                mined_in_block_height = 1939750,
                recipients = [
                    cryptoapis.models.get_transaction_details_by_transaction_idri_recipients_inner.GetTransactionDetailsByTransactionIDRI_recipients_inner(
                        address = '2MzakdGTEp8SMWEHKwKM4HYv6uNCBXtHpkV', 
                        amount = '0.000144', )
                    ],
                senders = [
                    cryptoapis.models.get_transaction_details_by_transaction_idri_senders_inner.GetTransactionDetailsByTransactionIDRI_senders_inner(
                        address = '2N5PcdirZUzKF9bWuGdugNuzcQrCbBudxv1', 
                        amount = '0.00873472', )
                    ],
                timestamp = 1582202940,
                transaction_hash = '1ec73b0f61359927d02376b35993b756b1097cb9a857bec23da4c98c4977d2b2',
                fee = cryptoapis.models.get_transaction_details_by_transaction_id_from_callback_ri_fee.GetTransactionDetailsByTransactionIDFromCallbackRI_fee(
                    amount = '0.00000300', 
                    unit = 'BTC', ),
                transaction_id = '',
                blockchain_specific = cryptoapis.models.get_transaction_details_by_transaction_id_from_callback_ribs.GetTransactionDetailsByTransactionIDFromCallbackRIBS(),
        )
        """

    def testGetTransactionDetailsByTransactionIDFromCallbackRI(self):
        """Test GetTransactionDetailsByTransactionIDFromCallbackRI"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
