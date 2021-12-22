"""
    CryptoAPIs

    Crypto APIs 2.0 is a complex and innovative infrastructure layer that radically simplifies the development of any Blockchain and Crypto related applications. Organized around REST, Crypto APIs 2.0 can assist both novice Bitcoin/Ethereum enthusiasts and crypto experts with the development of their blockchain applications. Crypto APIs 2.0 provides unified endpoints and data, raw data, automatic tokens and coins forwardings, callback functionalities, and much more.  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: developers@cryptoapis.io
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import cryptoapis
from cryptoapis.model.get_transaction_details_by_transaction_idribsz_vin import GetTransactionDetailsByTransactionIDRIBSZVin
from cryptoapis.model.get_transaction_details_by_transaction_idribsz_vout import GetTransactionDetailsByTransactionIDRIBSZVout
from cryptoapis.model.get_transaction_details_by_transaction_idribszv_shielded_output import GetTransactionDetailsByTransactionIDRIBSZVShieldedOutput
from cryptoapis.model.get_transaction_details_by_transaction_idribszv_shielded_spend import GetTransactionDetailsByTransactionIDRIBSZVShieldedSpend
from cryptoapis.model.list_confirmed_transactions_by_address_ribszv_join_split import ListConfirmedTransactionsByAddressRIBSZVJoinSplit
globals()['GetTransactionDetailsByTransactionIDRIBSZVShieldedOutput'] = GetTransactionDetailsByTransactionIDRIBSZVShieldedOutput
globals()['GetTransactionDetailsByTransactionIDRIBSZVShieldedSpend'] = GetTransactionDetailsByTransactionIDRIBSZVShieldedSpend
globals()['GetTransactionDetailsByTransactionIDRIBSZVin'] = GetTransactionDetailsByTransactionIDRIBSZVin
globals()['GetTransactionDetailsByTransactionIDRIBSZVout'] = GetTransactionDetailsByTransactionIDRIBSZVout
globals()['ListConfirmedTransactionsByAddressRIBSZVJoinSplit'] = ListConfirmedTransactionsByAddressRIBSZVJoinSplit
from cryptoapis.model.list_unconfirmed_transactions_by_address_ribsz import ListUnconfirmedTransactionsByAddressRIBSZ


class TestListUnconfirmedTransactionsByAddressRIBSZ(unittest.TestCase):
    """ListUnconfirmedTransactionsByAddressRIBSZ unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testListUnconfirmedTransactionsByAddressRIBSZ(self):
        """Test ListUnconfirmedTransactionsByAddressRIBSZ"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ListUnconfirmedTransactionsByAddressRIBSZ()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
