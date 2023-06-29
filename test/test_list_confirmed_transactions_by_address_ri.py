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
from cryptoapis.models.list_confirmed_transactions_by_address_ri import ListConfirmedTransactionsByAddressRI  # noqa: E501
from cryptoapis.rest import ApiException

class TestListConfirmedTransactionsByAddressRI(unittest.TestCase):
    """ListConfirmedTransactionsByAddressRI unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ListConfirmedTransactionsByAddressRI
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListConfirmedTransactionsByAddressRI`
        """
        model = cryptoapis.models.list_confirmed_transactions_by_address_ri.ListConfirmedTransactionsByAddressRI()  # noqa: E501
        if include_optional :
            return ListConfirmedTransactionsByAddressRI(
                transaction_id = '4b66461bf88b61e1e4326356534c135129defb504c7acb2fd6c92697d79eb250', 
                index = 1, 
                mined_in_block_hash = '0000000000000029aecac30e663a8c97060d56f9a8c62e73fe646dc5e02f72bb', 
                mined_in_block_height = 2408785, 
                recipients = [
                    cryptoapis.models.list_confirmed_transactions_by_address_ri_recipients_inner.ListConfirmedTransactionsByAddressRI_recipients_inner(
                        address = 'mho4jHBcrNCncKt38trJahXakuaBnS7LK5', 
                        amount = '0.00010000', )
                    ], 
                senders = [
                    cryptoapis.models.list_confirmed_transactions_by_address_ri_senders_inner.ListConfirmedTransactionsByAddressRI_senders_inner(
                        address = 'mho4jHBcrNCncKt38trJahXakuaBnS7LK5', 
                        amount = '0.00010000', )
                    ], 
                timestamp = 1669627454, 
                transaction_hash = '0000000000000029aecac30e663a8c97060d56f9a8c62e73fe646dc5e02f72bb', 
                fee = cryptoapis.models.list_confirmed_transactions_by_address_ri_fee.ListConfirmedTransactionsByAddressRI_fee(
                    amount = '0.00010000', 
                    unit = 'BTC', ), 
                blockchain_specific = cryptoapis.models.list_confirmed_transactions_by_address_ribs.ListConfirmedTransactionsByAddressRIBS()
            )
        else :
            return ListConfirmedTransactionsByAddressRI(
                transaction_id = '4b66461bf88b61e1e4326356534c135129defb504c7acb2fd6c92697d79eb250',
                index = 1,
                mined_in_block_hash = '0000000000000029aecac30e663a8c97060d56f9a8c62e73fe646dc5e02f72bb',
                mined_in_block_height = 2408785,
                recipients = [
                    cryptoapis.models.list_confirmed_transactions_by_address_ri_recipients_inner.ListConfirmedTransactionsByAddressRI_recipients_inner(
                        address = 'mho4jHBcrNCncKt38trJahXakuaBnS7LK5', 
                        amount = '0.00010000', )
                    ],
                senders = [
                    cryptoapis.models.list_confirmed_transactions_by_address_ri_senders_inner.ListConfirmedTransactionsByAddressRI_senders_inner(
                        address = 'mho4jHBcrNCncKt38trJahXakuaBnS7LK5', 
                        amount = '0.00010000', )
                    ],
                timestamp = 1669627454,
                transaction_hash = '0000000000000029aecac30e663a8c97060d56f9a8c62e73fe646dc5e02f72bb',
                fee = cryptoapis.models.list_confirmed_transactions_by_address_ri_fee.ListConfirmedTransactionsByAddressRI_fee(
                    amount = '0.00010000', 
                    unit = 'BTC', ),
                blockchain_specific = cryptoapis.models.list_confirmed_transactions_by_address_ribs.ListConfirmedTransactionsByAddressRIBS(),
        )
        """

    def testListConfirmedTransactionsByAddressRI(self):
        """Test ListConfirmedTransactionsByAddressRI"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
