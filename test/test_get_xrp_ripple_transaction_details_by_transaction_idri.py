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
from cryptoapis.models.get_xrp_ripple_transaction_details_by_transaction_idri import GetXRPRippleTransactionDetailsByTransactionIDRI  # noqa: E501
from cryptoapis.rest import ApiException

class TestGetXRPRippleTransactionDetailsByTransactionIDRI(unittest.TestCase):
    """GetXRPRippleTransactionDetailsByTransactionIDRI unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetXRPRippleTransactionDetailsByTransactionIDRI
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetXRPRippleTransactionDetailsByTransactionIDRI`
        """
        model = cryptoapis.models.get_xrp_ripple_transaction_details_by_transaction_idri.GetXRPRippleTransactionDetailsByTransactionIDRI()  # noqa: E501
        if include_optional :
            return GetXRPRippleTransactionDetailsByTransactionIDRI(
                additional_data = 'rPmPErQe4g9725pcNxJpuvKkdqTESTQ6Tu', 
                destination_tag = 3999472835, 
                index = '2', 
                mined_in_block_hash = '3f7af58d6cf1cd9020fb285d8e3e215131800d5109e42647ffd9b3aeae59df33', 
                mined_in_block_height = '15973802', 
                offer = cryptoapis.models.get_xrp_ripple_transaction_details_by_transaction_idri_offer.GetXRPRippleTransactionDetailsByTransactionIDRI_offer(
                    amount = '3.0154', 
                    unit = 'XRP', ), 
                receive = cryptoapis.models.get_xrp_ripple_transaction_details_by_transaction_idri_receive.GetXRPRippleTransactionDetailsByTransactionIDRI_receive(
                    amount = '2.1256', 
                    unit = 'XRP', ), 
                recipients = [
                    cryptoapis.models.get_xrp_ripple_transaction_details_by_transaction_idri_recipients_inner.GetXRPRippleTransactionDetailsByTransactionIDRI_recipients_inner(
                        address = 'rNUY3X3HovAXuTesTbMh8PAX6CM5V2RzMY', 
                        amount = '0.00001', )
                    ], 
                senders = [
                    cryptoapis.models.get_xrp_ripple_transaction_details_by_transaction_idri_senders_inner.GetXRPRippleTransactionDetailsByTransactionIDRI_senders_inner(
                        address = 'rNUY3X3HovAXuTesTbMh8PAX6CM5V2RzMY', 
                        amount = '0.00001', )
                    ], 
                sequence = 4294967295, 
                status = '', 
                timestamp = 1582202940, 
                transaction_hash = '36a1737481edec87bacc3101dfb752ae2c76f9171e7edebe587e330c1ea77c8d', 
                type = 'Payment', 
                fee = cryptoapis.models.get_xrp_ripple_transaction_details_by_transaction_idri_fee.GetXRPRippleTransactionDetailsByTransactionIDRI_fee(
                    amount = '0.0021', 
                    unit = 'XRP', ), 
                value = cryptoapis.models.get_xrp_ripple_transaction_details_by_transaction_idri_value.GetXRPRippleTransactionDetailsByTransactionIDRI_value(
                    amount = '3.0254', 
                    unit = 'XRP', )
            )
        else :
            return GetXRPRippleTransactionDetailsByTransactionIDRI(
                additional_data = 'rPmPErQe4g9725pcNxJpuvKkdqTESTQ6Tu',
                index = '2',
                mined_in_block_hash = '3f7af58d6cf1cd9020fb285d8e3e215131800d5109e42647ffd9b3aeae59df33',
                mined_in_block_height = '15973802',
                offer = cryptoapis.models.get_xrp_ripple_transaction_details_by_transaction_idri_offer.GetXRPRippleTransactionDetailsByTransactionIDRI_offer(
                    amount = '3.0154', 
                    unit = 'XRP', ),
                receive = cryptoapis.models.get_xrp_ripple_transaction_details_by_transaction_idri_receive.GetXRPRippleTransactionDetailsByTransactionIDRI_receive(
                    amount = '2.1256', 
                    unit = 'XRP', ),
                recipients = [
                    cryptoapis.models.get_xrp_ripple_transaction_details_by_transaction_idri_recipients_inner.GetXRPRippleTransactionDetailsByTransactionIDRI_recipients_inner(
                        address = 'rNUY3X3HovAXuTesTbMh8PAX6CM5V2RzMY', 
                        amount = '0.00001', )
                    ],
                senders = [
                    cryptoapis.models.get_xrp_ripple_transaction_details_by_transaction_idri_senders_inner.GetXRPRippleTransactionDetailsByTransactionIDRI_senders_inner(
                        address = 'rNUY3X3HovAXuTesTbMh8PAX6CM5V2RzMY', 
                        amount = '0.00001', )
                    ],
                sequence = 4294967295,
                timestamp = 1582202940,
                transaction_hash = '36a1737481edec87bacc3101dfb752ae2c76f9171e7edebe587e330c1ea77c8d',
                type = 'Payment',
                fee = cryptoapis.models.get_xrp_ripple_transaction_details_by_transaction_idri_fee.GetXRPRippleTransactionDetailsByTransactionIDRI_fee(
                    amount = '0.0021', 
                    unit = 'XRP', ),
                value = cryptoapis.models.get_xrp_ripple_transaction_details_by_transaction_idri_value.GetXRPRippleTransactionDetailsByTransactionIDRI_value(
                    amount = '3.0254', 
                    unit = 'XRP', ),
        )
        """

    def testGetXRPRippleTransactionDetailsByTransactionIDRI(self):
        """Test GetXRPRippleTransactionDetailsByTransactionIDRI"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
