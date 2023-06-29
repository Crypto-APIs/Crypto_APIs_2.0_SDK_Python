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
from cryptoapis.models.list_xrp_ripple_transactions_by_block_hash_ri import ListXRPRippleTransactionsByBlockHashRI  # noqa: E501
from cryptoapis.rest import ApiException

class TestListXRPRippleTransactionsByBlockHashRI(unittest.TestCase):
    """ListXRPRippleTransactionsByBlockHashRI unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ListXRPRippleTransactionsByBlockHashRI
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListXRPRippleTransactionsByBlockHashRI`
        """
        model = cryptoapis.models.list_xrp_ripple_transactions_by_block_hash_ri.ListXRPRippleTransactionsByBlockHashRI()  # noqa: E501
        if include_optional :
            return ListXRPRippleTransactionsByBlockHashRI(
                additional_data = 'r4CmvbkDWGt9AZmkfuubmiSdsxGZFxAKBY', 
                destination_tag = 3999472835, 
                index = 3, 
                mined_in_block_height = 15971358, 
                offer = cryptoapis.models.list_xrp_ripple_transactions_by_block_hash_ri_offer.ListXRPRippleTransactionsByBlockHashRI_offer(
                    amount = '8.2365', 
                    unit = 'XRP', ), 
                recipients = [
                    cryptoapis.models.list_xrp_ripple_transactions_by_block_hash_ri_recipients_inner.ListXRPRippleTransactionsByBlockHashRI_recipients_inner(
                        address = 'rNUY3X3HovAXuTesTbMh8PAX6CM5V2RzMY', 
                        amount = '0.0001', )
                    ], 
                senders = [
                    cryptoapis.models.list_xrp_ripple_transactions_by_block_hash_ri_senders_inner.ListXRPRippleTransactionsByBlockHashRI_senders_inner(
                        address = 'rPmPErQe4g9725pcNxJpuvKkdqTESTQ6Tu', 
                        amount = '0.0001', )
                    ], 
                sequence = 32568, 
                status = 'tesSUCCESS', 
                timestamp = 236589, 
                transaction_hash = 'ba3bc1337071c8e73b441fe12a1911f4365d7ea82cace7c8ecba3ee9f364978b', 
                type = 'Payment', 
                fee = cryptoapis.models.list_xrp_ripple_transactions_by_block_hash_ri_fee.ListXRPRippleTransactionsByBlockHashRI_fee(
                    amount = '2.0325', 
                    unit = 'XRP', ), 
                receive = cryptoapis.models.list_xrp_ripple_transactions_by_block_hash_ri_receive.ListXRPRippleTransactionsByBlockHashRI_receive(
                    amount = '6.2354', 
                    unit = 'XRP', ), 
                value = cryptoapis.models.list_xrp_ripple_transactions_by_block_hash_ri_value.ListXRPRippleTransactionsByBlockHashRI_value(
                    amount = '22.023', 
                    unit = 'XRP', )
            )
        else :
            return ListXRPRippleTransactionsByBlockHashRI(
                index = 3,
                mined_in_block_height = 15971358,
                offer = cryptoapis.models.list_xrp_ripple_transactions_by_block_hash_ri_offer.ListXRPRippleTransactionsByBlockHashRI_offer(
                    amount = '8.2365', 
                    unit = 'XRP', ),
                recipients = [
                    cryptoapis.models.list_xrp_ripple_transactions_by_block_hash_ri_recipients_inner.ListXRPRippleTransactionsByBlockHashRI_recipients_inner(
                        address = 'rNUY3X3HovAXuTesTbMh8PAX6CM5V2RzMY', 
                        amount = '0.0001', )
                    ],
                senders = [
                    cryptoapis.models.list_xrp_ripple_transactions_by_block_hash_ri_senders_inner.ListXRPRippleTransactionsByBlockHashRI_senders_inner(
                        address = 'rPmPErQe4g9725pcNxJpuvKkdqTESTQ6Tu', 
                        amount = '0.0001', )
                    ],
                sequence = 32568,
                status = 'tesSUCCESS',
                timestamp = 236589,
                transaction_hash = 'ba3bc1337071c8e73b441fe12a1911f4365d7ea82cace7c8ecba3ee9f364978b',
                type = 'Payment',
                fee = cryptoapis.models.list_xrp_ripple_transactions_by_block_hash_ri_fee.ListXRPRippleTransactionsByBlockHashRI_fee(
                    amount = '2.0325', 
                    unit = 'XRP', ),
                receive = cryptoapis.models.list_xrp_ripple_transactions_by_block_hash_ri_receive.ListXRPRippleTransactionsByBlockHashRI_receive(
                    amount = '6.2354', 
                    unit = 'XRP', ),
                value = cryptoapis.models.list_xrp_ripple_transactions_by_block_hash_ri_value.ListXRPRippleTransactionsByBlockHashRI_value(
                    amount = '22.023', 
                    unit = 'XRP', ),
        )
        """

    def testListXRPRippleTransactionsByBlockHashRI(self):
        """Test ListXRPRippleTransactionsByBlockHashRI"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
