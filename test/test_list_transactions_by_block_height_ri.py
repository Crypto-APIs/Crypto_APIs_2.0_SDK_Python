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
from cryptoapis.model.get_transaction_details_by_transaction_idri_recipients import GetTransactionDetailsByTransactionIDRIRecipients
from cryptoapis.model.get_transaction_details_by_transaction_idri_senders import GetTransactionDetailsByTransactionIDRISenders
from cryptoapis.model.list_transactions_by_block_height_ri_fee import ListTransactionsByBlockHeightRIFee
from cryptoapis.model.list_transactions_by_block_height_ribs import ListTransactionsByBlockHeightRIBS
globals()['GetTransactionDetailsByTransactionIDRIRecipients'] = GetTransactionDetailsByTransactionIDRIRecipients
globals()['GetTransactionDetailsByTransactionIDRISenders'] = GetTransactionDetailsByTransactionIDRISenders
globals()['ListTransactionsByBlockHeightRIBS'] = ListTransactionsByBlockHeightRIBS
globals()['ListTransactionsByBlockHeightRIFee'] = ListTransactionsByBlockHeightRIFee
from cryptoapis.model.list_transactions_by_block_height_ri import ListTransactionsByBlockHeightRI


class TestListTransactionsByBlockHeightRI(unittest.TestCase):
    """ListTransactionsByBlockHeightRI unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testListTransactionsByBlockHeightRI(self):
        """Test ListTransactionsByBlockHeightRI"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ListTransactionsByBlockHeightRI()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()