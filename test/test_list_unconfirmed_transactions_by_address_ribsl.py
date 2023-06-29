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
from cryptoapis.models.list_unconfirmed_transactions_by_address_ribsl import ListUnconfirmedTransactionsByAddressRIBSL  # noqa: E501
from cryptoapis.rest import ApiException

class TestListUnconfirmedTransactionsByAddressRIBSL(unittest.TestCase):
    """ListUnconfirmedTransactionsByAddressRIBSL unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ListUnconfirmedTransactionsByAddressRIBSL
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListUnconfirmedTransactionsByAddressRIBSL`
        """
        model = cryptoapis.models.list_unconfirmed_transactions_by_address_ribsl.ListUnconfirmedTransactionsByAddressRIBSL()  # noqa: E501
        if include_optional :
            return ListUnconfirmedTransactionsByAddressRIBSL(
                locktime = 2, 
                size = 223, 
                v_size = 141, 
                version = 2, 
                vin = [
                    cryptoapis.models.list_unconfirmed_transactions_by_address_ribsl_vin_inner.ListUnconfirmedTransactionsByAddressRIBSL_vin_inner(
                        addresses = [
                            'tltc1qcefwt8q647lstt5829exynqnecr9uxq9pk3yr5'
                            ], 
                        script_sig = cryptoapis.models.list_unconfirmed_transactions_by_address_ribsl_vin_inner_script_sig.ListUnconfirmedTransactionsByAddressRIBSL_vin_inner_scriptSig(
                            asm = '0 eab6ff0ee1158241737dfa5c78449dc06cf021cc', 
                            hex = '0014eab6ff0ee1158241737dfa5c78449dc06cf021cc', 
                            type = 'scripthash', ), 
                        sequence = '4294967294', 
                        txid = '1db56e1e8dfab84f6f0e33f8ddb160c9b16286471a3b486d79ea85bcf4d076b2', 
                        txinwitness = [
                            '304402204e88dfe79e58b640908812c496ea74d2941c23e70ee3d93ebd469dbd136afe0c02203d7631427c0b5cb96e8a8b23b6c8c0c8112ecb5fb020ee2a7a70841564ed679b01'
                            ], 
                        value = '0.0225', 
                        vout = 1, )
                    ], 
                vout = [
                    cryptoapis.models.list_unconfirmed_transactions_by_address_ribsl_vout_inner.ListUnconfirmedTransactionsByAddressRIBSL_vout_inner(
                        is_spent = False, 
                        script_pub_key = cryptoapis.models.get_transaction_details_by_transaction_idribsl_vout_inner_script_pub_key.GetTransactionDetailsByTransactionIDRIBSL_vout_inner_scriptPubKey(
                            addresses = [
                                '3LAAY4fp88RsNHkVW5DZJgqUdbMD5rVoqZ'
                                ], 
                            asm = 'OP_HASH160 ca94af32587de4e5006685ffffc65a818ccd3fbc OP_EQUAL', 
                            hex = 'a914ca94af32587de4e5006685ffffc65a818ccd3fbc87', 
                            req_sigs = 1, 
                            type = 'scripthash', ), 
                        value = '0.03505975', )
                    ]
            )
        else :
            return ListUnconfirmedTransactionsByAddressRIBSL(
                locktime = 2,
                size = 223,
                v_size = 141,
                version = 2,
                vin = [
                    cryptoapis.models.list_unconfirmed_transactions_by_address_ribsl_vin_inner.ListUnconfirmedTransactionsByAddressRIBSL_vin_inner(
                        addresses = [
                            'tltc1qcefwt8q647lstt5829exynqnecr9uxq9pk3yr5'
                            ], 
                        script_sig = cryptoapis.models.list_unconfirmed_transactions_by_address_ribsl_vin_inner_script_sig.ListUnconfirmedTransactionsByAddressRIBSL_vin_inner_scriptSig(
                            asm = '0 eab6ff0ee1158241737dfa5c78449dc06cf021cc', 
                            hex = '0014eab6ff0ee1158241737dfa5c78449dc06cf021cc', 
                            type = 'scripthash', ), 
                        sequence = '4294967294', 
                        txid = '1db56e1e8dfab84f6f0e33f8ddb160c9b16286471a3b486d79ea85bcf4d076b2', 
                        txinwitness = [
                            '304402204e88dfe79e58b640908812c496ea74d2941c23e70ee3d93ebd469dbd136afe0c02203d7631427c0b5cb96e8a8b23b6c8c0c8112ecb5fb020ee2a7a70841564ed679b01'
                            ], 
                        value = '0.0225', 
                        vout = 1, )
                    ],
                vout = [
                    cryptoapis.models.list_unconfirmed_transactions_by_address_ribsl_vout_inner.ListUnconfirmedTransactionsByAddressRIBSL_vout_inner(
                        is_spent = False, 
                        script_pub_key = cryptoapis.models.get_transaction_details_by_transaction_idribsl_vout_inner_script_pub_key.GetTransactionDetailsByTransactionIDRIBSL_vout_inner_scriptPubKey(
                            addresses = [
                                '3LAAY4fp88RsNHkVW5DZJgqUdbMD5rVoqZ'
                                ], 
                            asm = 'OP_HASH160 ca94af32587de4e5006685ffffc65a818ccd3fbc OP_EQUAL', 
                            hex = 'a914ca94af32587de4e5006685ffffc65a818ccd3fbc87', 
                            req_sigs = 1, 
                            type = 'scripthash', ), 
                        value = '0.03505975', )
                    ],
        )
        """

    def testListUnconfirmedTransactionsByAddressRIBSL(self):
        """Test ListUnconfirmedTransactionsByAddressRIBSL"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
