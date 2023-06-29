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
from cryptoapis.models.list_confirmed_transactions_by_address_ribsz import ListConfirmedTransactionsByAddressRIBSZ  # noqa: E501
from cryptoapis.rest import ApiException

class TestListConfirmedTransactionsByAddressRIBSZ(unittest.TestCase):
    """ListConfirmedTransactionsByAddressRIBSZ unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ListConfirmedTransactionsByAddressRIBSZ
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListConfirmedTransactionsByAddressRIBSZ`
        """
        model = cryptoapis.models.list_confirmed_transactions_by_address_ribsz.ListConfirmedTransactionsByAddressRIBSZ()  # noqa: E501
        if include_optional :
            return ListConfirmedTransactionsByAddressRIBSZ(
                binding_sig = '603624b3e78e0de0415dea320797a107076a9f7aabd39f44bc4957803330e9891cb33744ac2ec749c2d2d341f29467c49c0ae35bf34765e2fb7c4cda68584804', 
                expiry_height = 0, 
                join_split_pub_key = '5d2673b4c727241410e42f214a39218e4f13354d77db8ec31243a7be7ed8e2b7', 
                join_split_sig = '8b06b926d619ead780b0769e5997ded93f9851fd0efd4b667afc5bcc2792b26cd4a565b4efa7733535fdc09fa566ca59042785d7fd8043d37fdf9e144465080a', 
                locktime = 1781965, 
                overwintered = True, 
                size = 234, 
                v_join_split = [
                    cryptoapis.models.list_confirmed_transactions_by_address_ribsz_v_join_split_inner.ListConfirmedTransactionsByAddressRIBSZ_vJoinSplit_inner(
                        anchor = 'd32ddbaf0d9dc8c10783c01fd9ba5bd0bc2e5efe3d1665d7d6771eb4393736b4', 
                        cipher_texts = [
                            '988a182a3e561e0cca18e38e3273b3c538c3e6f79077867eca4305e48cbc5e6d3ff680de602e44fb8869f1a8747d9e3775f2418d33c41233e3612d6ecf277346b85bcd0c1fbdf4c4c0da107bf84e02c82588bf02f4a6c23ed36f70a436f69a6fe6cc38634d69e34e3d3942ff06a7921153689b4b50e3799f0ce3d8a35d165beaecc0c91018e9a8c618ff7036fd14b95641229e42974054c70d1e080c909c382297c5698b9af9b9291d6851c718d3e771e6376bd6dd52f4624ad024b4d85426e32fcf531019eeea547fda3ecca87aceaa80982e8fe22db152c01635d24fe4f59d1979610cad898c169d88559bcd8847f82b2ac5ab2f8623eed55b0273982297a52e9cbb4523d6411a0d40f59faf0ff9f23783790027d5f5153d421d897c11b9da48e7218b7ce64c653283ecaffab78006b771aec20e05761d768f9347f96c566d47014eff083268622e81ce6c17e1e66227ee795cd3a7efb77c3b5b4a896d75111a2a846be94c0fcdaab69ca2101a499c817590c4d1ea8b39145f0168210af4ac86cc6018e95c0699a6f1275c2934cbe1cf84bbeee12ed77b54fe4c2f6b1c0187e7ab31750e03cf72467e9bf7c8a89bb8f4160b5d56def4cb24f595303bcdf065bf2ec7161c8165a6be7252b7cd8c3aa9bf9baf78690f19c1d4fc1d39e558bd4f4fdb3e56fb1b2e287cf67b0e0cf8df5c28c7bb94393cb837c180d380814a63e7db94e4e9652933e67f28f93dd92ee45be8f824cd9469dd0a872e130d4c1621a56d2a33ffb51c04b4151f0a471472a977d771b0eb13bf9fde44804ef755b97e1cae1e8d807f5eb692d7ffc20d8e451ce9ccd75b1a270836db80'
                            ], 
                        commitments = [
                            '2f7f341d6af9a75b317d0753d2fc0514baf38bb602cd66dc7d221aa371e6062c'
                            ], 
                        macs = [
                            '52f677a49eb36bcce6b30f94bee481d73c4fdd61963bda54b68f3a90ca007b59'
                            ], 
                        nullifiers = [
                            '30e41a9a6605933a75ec42439ab65eb347025002f6486e5549abb82438447dbe'
                            ], 
                        one_time_pub_key = '0a2e7ba03903480af852cb47d8ce76eb6546aef69bdb35b28b8ae815012d4d13', 
                        proof = '8dd9c988c9f337bd55c07fa9e2fa405cf4dda2cb915214fc0b5924870eed0f0187a0db001b5d8ea43a537e423d91d0fc868a456fa3e0bf9e99d1b04f43c6983a05a99458a69903add73ccaa4177844df9056d40c5a71ae14a70835cb30ca7d810fa1d48c9180ddec2ca1cecfaa8706ab514d6e8fe2dd228d7dc012d9407517523b774107a6a78dc972b175b94d1681b980e2b9ba7d39f880973787080a12bf14dc3f038333245a60bbcd9cb1fe2baba30ed083535752cc26ea0c57134e0c774e', 
                        random_seed = '05eb35ce1cec5f5824f708ee9d95467d2318d24c8d4220040df92d48b1f182e8', 
                        v_pub_new = '50.02989193', 
                        v_pub_old = '0', )
                    ], 
                v_shielded_output = [
                    cryptoapis.models.get_transaction_details_by_transaction_idribsz_v_shielded_output_inner.GetTransactionDetailsByTransactionIDRIBSZ_vShieldedOutput_inner(
                        cmu = '4eb188a762d4fd4358ae70b2dac1b6a596ad653be92471792bf4b157850a1011', 
                        cv = '547a9cef4937304f97acacfcd9827b5aa1b2e5b1ae32e360fae828b955564a0e', 
                        enc_cipher_text = 'a6c0084214eef0058f4b51c1e25b4c05ac282fec0edc5938c4283aa2a6d7c426d7a3c927d11596f81780b18c0eee90848702eb7fa512f7a6386e52d9bc17d5bc0e20bc24608ece560a314570aaf4c095bc988a9a0f8ef72ed91d0eee7d927eb37428c62af28c6a5c9379ac48aef3cdfb9b83eed77edde50acab7615f8fecdb1f24500fab6b8a72440e6fadbf0e6ad0ff8989df4d27bb2bc56c3a99c6da2e82c68a319857902842cf15aec180b6ea0ff3ebedf1cfd02b434ac715bc4afb17f67286d5708864a7aabb461461f080bbcf0315c38d782be6d0aae7ac3beb6574babf12c9182574d6c6e900888b5c4da40952c403b7d4ebe96e051893e388bcb7026d839e1d49ddbb132706fbadae1ef272d7e8dbf297dfbe7867651cfd843e52239d8270c1b6d46f2589643a5a325018f2d0b82b53955a5a3c5c3cecf8f0829594777887028456bd708c7c4ad88e588609c1b33d9060d8cf0015bfc18676ebc7022956ab6d4c6aae24550422e702733da234e2ce6f5adbafc4e2d97ae9846febddeacfaefda7f186b7e8182f4692c34bff4bd31eeeab15c5b5f7a41c93acae05a4f3c378fbe6cf33ab3628f4c5b8e04b9368ec69ea1c7c816c803d9ef7bbafe232f43959c7b49dd7c3328dc028040f440fd3cb2e08449db77c191288f120c065870d800ebdca234e6c2ba1fa6d44d04f4fed2e41b1c65d273b0ce58287274e8dc71a2a174244f026971bb9c698e7f7964eec615515910c627a201b52c3c2c504623ac45f5606d0400120bd5b6e1f431775fe92fb2c9eb5546c9dc12693ee9b679e49fce2cf71', 
                        ephemeral_key = '04c59e908296aeac1160ba8def90916988bf8389564343e6fb3b9e52c27fba0a', 
                        out_cipher_text = 'b3f02b333a61b69e63dfeaf1ad430534985cd6958abe92664abe85449ca68b5c145f536e9a636a881aab5e314b4f550b2b8f5600dc1ed636f643b11e00bb6c469bf5205f16197372dcf5e4b0871e42f4', 
                        proof = '8dd9c988c9f337bd55c07fa9e2fa405cf4dda2cb915214fc0b5924870eed0f0187a0db001b5d8ea43a537e423d91d0fc868a456fa3e0bf9e99d1b04f43c6983a05a99458a69903add73ccaa4177844df9056d40c5a71ae14a70835cb30ca7d810fa1d48c9180ddec2ca1cecfaa8706ab514d6e8fe2dd228d7dc012d9407517523b774107a6a78dc972b175b94d1681b980e2b9ba7d39f880973787080a12bf14dc3f038333245a60bbcd9cb1fe2baba30ed083535752cc26ea0c57134e0c774e', )
                    ], 
                v_shielded_spend = [
                    cryptoapis.models.get_transaction_details_by_transaction_idribsz_v_shielded_spend_inner.GetTransactionDetailsByTransactionIDRIBSZ_vShieldedSpend_inner(
                        anchor = 'd32ddbaf0d9dc8c10783c01fd9ba5bd0bc2e5efe3d1665d7d6771eb4393736b4', 
                        cv = '547a9cef4937304f97acacfcd9827b5aa1b2e5b1ae32e360fae828b955564a0e', 
                        nullifier = '30e41a9a6605933a75ec42439ab65eb347025002f6486e5549abb82438447dbe', 
                        proof = '030ff7fdb006db7f9acb0d2d6fae180e4395f0b6a979f6ddf48a349bc03ad2e7bb0324a5c3c7e6be131c34126ad22c74138f45f6f77bba706dfc87335a9adffcfef20a03e47751f403a37f9c5e1874aa50818c3eef09304c57c77b111057c09ed2112a7ed310ad285e0b778a4f44b654032b642b8b2df3be16bea011da7a2221bc0f0a0309f51f87caef2ea0f665f1a77d0dd50766d835d181e534818d8c3413b4d555990222574d9c92f81f17ff0af7a0583e76b3d3d4df2927561f37e57e15bc07b3f5d70306a9624c496d0bcb40085894bf32ef05db6469ec145c0ce5529e2697b6a0252c0216930cf7b3a7381762a6a91868e9d2bf823bfc7fb885de1fbd6a6cacae02db590318ffeb357ffd6832893ab0ccd3b15cef1df0fef45c091cf33fccee43a2834d44', 
                        rk = '39bdf742e16c4d1533a56df956bebe4d0214d4a361820db58a293847b6344d30', 
                        spend_auth_sig = '0f3b38a91fffbbf58f99d2d070002c0868be6804204b7bf4be0df47f62ee5e0d43222776a71fd7e1421ec54502194192d73681701b743ad427573ca18a95a405', )
                    ], 
                value_balance = '0', 
                version = 1, 
                version_group_id = '0x892f2085', 
                vin = [
                    cryptoapis.models.list_confirmed_transactions_by_address_ribsz_vin_inner.ListConfirmedTransactionsByAddressRIBSZ_vin_inner(
                        addresses = [
                            't2UNzUUx8mWBCRYPRezvA363EYXyEpHokyi'
                            ], 
                        coinbase = '02d3080c4e060000000000002f4e614e', 
                        script_sig = cryptoapis.models.get_transaction_details_by_transaction_idribsz_vin_inner_script_sig.GetTransactionDetailsByTransactionIDRIBSZ_vin_inner_scriptSig(
                            asm = 'OP_HASH160 ef775f1f997f122a062fff1a2d7443abd1f9c642 OP_EQUAL', 
                            hex = 'a914ef775f1f997f122a062fff1a2d7443abd1f9c64287', 
                            type = 'pubkeyhash', ), 
                        sequence = 4294967295, 
                        txid = '4b66461bf88b61e1e4326356534c135129defb504c7acb2fd6c92697d79eb250', 
                        txinwitness = [
                            '3045022100c11ea5740bcd69f0f68a4914279838014d28923134d18e05c5a5486dfd06cc8c02200dadccec3f07bed0d1040f9e5a155efa5fdd40fc91f92342578d26848da4c6b901'
                            ], 
                        value = '0.000144', 
                        vout = 1, )
                    ], 
                vout = [
                    cryptoapis.models.get_transaction_details_by_transaction_idribsz_vout_inner.GetTransactionDetailsByTransactionIDRIBSZ_vout_inner(
                        is_spent = True, 
                        script_pub_key = cryptoapis.models.get_transaction_details_by_transaction_idribsz_vout_inner_script_pub_key.GetTransactionDetailsByTransactionIDRIBSZ_vout_inner_scriptPubKey(
                            addresses = [
                                't2UNzUUx8mWBCRYPRezvA363EYXyEpHokyi'
                                ], 
                            asm = 'OP_HASH160 ef775f1f997f122a062fff1a2d7443abd1f9c642 OP_EQUAL', 
                            hex = 'a914ef775f1f997f122a062fff1a2d7443abd1f9c64287', 
                            req_sigs = 1, 
                            type = 'pubkeyhash', ), 
                        value = '0.000144', )
                    ]
            )
        else :
            return ListConfirmedTransactionsByAddressRIBSZ(
                binding_sig = '603624b3e78e0de0415dea320797a107076a9f7aabd39f44bc4957803330e9891cb33744ac2ec749c2d2d341f29467c49c0ae35bf34765e2fb7c4cda68584804',
                expiry_height = 0,
                join_split_pub_key = '5d2673b4c727241410e42f214a39218e4f13354d77db8ec31243a7be7ed8e2b7',
                join_split_sig = '8b06b926d619ead780b0769e5997ded93f9851fd0efd4b667afc5bcc2792b26cd4a565b4efa7733535fdc09fa566ca59042785d7fd8043d37fdf9e144465080a',
                locktime = 1781965,
                overwintered = True,
                size = 234,
                v_join_split = [
                    cryptoapis.models.list_confirmed_transactions_by_address_ribsz_v_join_split_inner.ListConfirmedTransactionsByAddressRIBSZ_vJoinSplit_inner(
                        anchor = 'd32ddbaf0d9dc8c10783c01fd9ba5bd0bc2e5efe3d1665d7d6771eb4393736b4', 
                        cipher_texts = [
                            '988a182a3e561e0cca18e38e3273b3c538c3e6f79077867eca4305e48cbc5e6d3ff680de602e44fb8869f1a8747d9e3775f2418d33c41233e3612d6ecf277346b85bcd0c1fbdf4c4c0da107bf84e02c82588bf02f4a6c23ed36f70a436f69a6fe6cc38634d69e34e3d3942ff06a7921153689b4b50e3799f0ce3d8a35d165beaecc0c91018e9a8c618ff7036fd14b95641229e42974054c70d1e080c909c382297c5698b9af9b9291d6851c718d3e771e6376bd6dd52f4624ad024b4d85426e32fcf531019eeea547fda3ecca87aceaa80982e8fe22db152c01635d24fe4f59d1979610cad898c169d88559bcd8847f82b2ac5ab2f8623eed55b0273982297a52e9cbb4523d6411a0d40f59faf0ff9f23783790027d5f5153d421d897c11b9da48e7218b7ce64c653283ecaffab78006b771aec20e05761d768f9347f96c566d47014eff083268622e81ce6c17e1e66227ee795cd3a7efb77c3b5b4a896d75111a2a846be94c0fcdaab69ca2101a499c817590c4d1ea8b39145f0168210af4ac86cc6018e95c0699a6f1275c2934cbe1cf84bbeee12ed77b54fe4c2f6b1c0187e7ab31750e03cf72467e9bf7c8a89bb8f4160b5d56def4cb24f595303bcdf065bf2ec7161c8165a6be7252b7cd8c3aa9bf9baf78690f19c1d4fc1d39e558bd4f4fdb3e56fb1b2e287cf67b0e0cf8df5c28c7bb94393cb837c180d380814a63e7db94e4e9652933e67f28f93dd92ee45be8f824cd9469dd0a872e130d4c1621a56d2a33ffb51c04b4151f0a471472a977d771b0eb13bf9fde44804ef755b97e1cae1e8d807f5eb692d7ffc20d8e451ce9ccd75b1a270836db80'
                            ], 
                        commitments = [
                            '2f7f341d6af9a75b317d0753d2fc0514baf38bb602cd66dc7d221aa371e6062c'
                            ], 
                        macs = [
                            '52f677a49eb36bcce6b30f94bee481d73c4fdd61963bda54b68f3a90ca007b59'
                            ], 
                        nullifiers = [
                            '30e41a9a6605933a75ec42439ab65eb347025002f6486e5549abb82438447dbe'
                            ], 
                        one_time_pub_key = '0a2e7ba03903480af852cb47d8ce76eb6546aef69bdb35b28b8ae815012d4d13', 
                        proof = '8dd9c988c9f337bd55c07fa9e2fa405cf4dda2cb915214fc0b5924870eed0f0187a0db001b5d8ea43a537e423d91d0fc868a456fa3e0bf9e99d1b04f43c6983a05a99458a69903add73ccaa4177844df9056d40c5a71ae14a70835cb30ca7d810fa1d48c9180ddec2ca1cecfaa8706ab514d6e8fe2dd228d7dc012d9407517523b774107a6a78dc972b175b94d1681b980e2b9ba7d39f880973787080a12bf14dc3f038333245a60bbcd9cb1fe2baba30ed083535752cc26ea0c57134e0c774e', 
                        random_seed = '05eb35ce1cec5f5824f708ee9d95467d2318d24c8d4220040df92d48b1f182e8', 
                        v_pub_new = '50.02989193', 
                        v_pub_old = '0', )
                    ],
                v_shielded_output = [
                    cryptoapis.models.get_transaction_details_by_transaction_idribsz_v_shielded_output_inner.GetTransactionDetailsByTransactionIDRIBSZ_vShieldedOutput_inner(
                        cmu = '4eb188a762d4fd4358ae70b2dac1b6a596ad653be92471792bf4b157850a1011', 
                        cv = '547a9cef4937304f97acacfcd9827b5aa1b2e5b1ae32e360fae828b955564a0e', 
                        enc_cipher_text = 'a6c0084214eef0058f4b51c1e25b4c05ac282fec0edc5938c4283aa2a6d7c426d7a3c927d11596f81780b18c0eee90848702eb7fa512f7a6386e52d9bc17d5bc0e20bc24608ece560a314570aaf4c095bc988a9a0f8ef72ed91d0eee7d927eb37428c62af28c6a5c9379ac48aef3cdfb9b83eed77edde50acab7615f8fecdb1f24500fab6b8a72440e6fadbf0e6ad0ff8989df4d27bb2bc56c3a99c6da2e82c68a319857902842cf15aec180b6ea0ff3ebedf1cfd02b434ac715bc4afb17f67286d5708864a7aabb461461f080bbcf0315c38d782be6d0aae7ac3beb6574babf12c9182574d6c6e900888b5c4da40952c403b7d4ebe96e051893e388bcb7026d839e1d49ddbb132706fbadae1ef272d7e8dbf297dfbe7867651cfd843e52239d8270c1b6d46f2589643a5a325018f2d0b82b53955a5a3c5c3cecf8f0829594777887028456bd708c7c4ad88e588609c1b33d9060d8cf0015bfc18676ebc7022956ab6d4c6aae24550422e702733da234e2ce6f5adbafc4e2d97ae9846febddeacfaefda7f186b7e8182f4692c34bff4bd31eeeab15c5b5f7a41c93acae05a4f3c378fbe6cf33ab3628f4c5b8e04b9368ec69ea1c7c816c803d9ef7bbafe232f43959c7b49dd7c3328dc028040f440fd3cb2e08449db77c191288f120c065870d800ebdca234e6c2ba1fa6d44d04f4fed2e41b1c65d273b0ce58287274e8dc71a2a174244f026971bb9c698e7f7964eec615515910c627a201b52c3c2c504623ac45f5606d0400120bd5b6e1f431775fe92fb2c9eb5546c9dc12693ee9b679e49fce2cf71', 
                        ephemeral_key = '04c59e908296aeac1160ba8def90916988bf8389564343e6fb3b9e52c27fba0a', 
                        out_cipher_text = 'b3f02b333a61b69e63dfeaf1ad430534985cd6958abe92664abe85449ca68b5c145f536e9a636a881aab5e314b4f550b2b8f5600dc1ed636f643b11e00bb6c469bf5205f16197372dcf5e4b0871e42f4', 
                        proof = '8dd9c988c9f337bd55c07fa9e2fa405cf4dda2cb915214fc0b5924870eed0f0187a0db001b5d8ea43a537e423d91d0fc868a456fa3e0bf9e99d1b04f43c6983a05a99458a69903add73ccaa4177844df9056d40c5a71ae14a70835cb30ca7d810fa1d48c9180ddec2ca1cecfaa8706ab514d6e8fe2dd228d7dc012d9407517523b774107a6a78dc972b175b94d1681b980e2b9ba7d39f880973787080a12bf14dc3f038333245a60bbcd9cb1fe2baba30ed083535752cc26ea0c57134e0c774e', )
                    ],
                v_shielded_spend = [
                    cryptoapis.models.get_transaction_details_by_transaction_idribsz_v_shielded_spend_inner.GetTransactionDetailsByTransactionIDRIBSZ_vShieldedSpend_inner(
                        anchor = 'd32ddbaf0d9dc8c10783c01fd9ba5bd0bc2e5efe3d1665d7d6771eb4393736b4', 
                        cv = '547a9cef4937304f97acacfcd9827b5aa1b2e5b1ae32e360fae828b955564a0e', 
                        nullifier = '30e41a9a6605933a75ec42439ab65eb347025002f6486e5549abb82438447dbe', 
                        proof = '030ff7fdb006db7f9acb0d2d6fae180e4395f0b6a979f6ddf48a349bc03ad2e7bb0324a5c3c7e6be131c34126ad22c74138f45f6f77bba706dfc87335a9adffcfef20a03e47751f403a37f9c5e1874aa50818c3eef09304c57c77b111057c09ed2112a7ed310ad285e0b778a4f44b654032b642b8b2df3be16bea011da7a2221bc0f0a0309f51f87caef2ea0f665f1a77d0dd50766d835d181e534818d8c3413b4d555990222574d9c92f81f17ff0af7a0583e76b3d3d4df2927561f37e57e15bc07b3f5d70306a9624c496d0bcb40085894bf32ef05db6469ec145c0ce5529e2697b6a0252c0216930cf7b3a7381762a6a91868e9d2bf823bfc7fb885de1fbd6a6cacae02db590318ffeb357ffd6832893ab0ccd3b15cef1df0fef45c091cf33fccee43a2834d44', 
                        rk = '39bdf742e16c4d1533a56df956bebe4d0214d4a361820db58a293847b6344d30', 
                        spend_auth_sig = '0f3b38a91fffbbf58f99d2d070002c0868be6804204b7bf4be0df47f62ee5e0d43222776a71fd7e1421ec54502194192d73681701b743ad427573ca18a95a405', )
                    ],
                value_balance = '0',
                version = 1,
                version_group_id = '0x892f2085',
                vin = [
                    cryptoapis.models.list_confirmed_transactions_by_address_ribsz_vin_inner.ListConfirmedTransactionsByAddressRIBSZ_vin_inner(
                        addresses = [
                            't2UNzUUx8mWBCRYPRezvA363EYXyEpHokyi'
                            ], 
                        coinbase = '02d3080c4e060000000000002f4e614e', 
                        script_sig = cryptoapis.models.get_transaction_details_by_transaction_idribsz_vin_inner_script_sig.GetTransactionDetailsByTransactionIDRIBSZ_vin_inner_scriptSig(
                            asm = 'OP_HASH160 ef775f1f997f122a062fff1a2d7443abd1f9c642 OP_EQUAL', 
                            hex = 'a914ef775f1f997f122a062fff1a2d7443abd1f9c64287', 
                            type = 'pubkeyhash', ), 
                        sequence = 4294967295, 
                        txid = '4b66461bf88b61e1e4326356534c135129defb504c7acb2fd6c92697d79eb250', 
                        txinwitness = [
                            '3045022100c11ea5740bcd69f0f68a4914279838014d28923134d18e05c5a5486dfd06cc8c02200dadccec3f07bed0d1040f9e5a155efa5fdd40fc91f92342578d26848da4c6b901'
                            ], 
                        value = '0.000144', 
                        vout = 1, )
                    ],
                vout = [
                    cryptoapis.models.get_transaction_details_by_transaction_idribsz_vout_inner.GetTransactionDetailsByTransactionIDRIBSZ_vout_inner(
                        is_spent = True, 
                        script_pub_key = cryptoapis.models.get_transaction_details_by_transaction_idribsz_vout_inner_script_pub_key.GetTransactionDetailsByTransactionIDRIBSZ_vout_inner_scriptPubKey(
                            addresses = [
                                't2UNzUUx8mWBCRYPRezvA363EYXyEpHokyi'
                                ], 
                            asm = 'OP_HASH160 ef775f1f997f122a062fff1a2d7443abd1f9c642 OP_EQUAL', 
                            hex = 'a914ef775f1f997f122a062fff1a2d7443abd1f9c64287', 
                            req_sigs = 1, 
                            type = 'pubkeyhash', ), 
                        value = '0.000144', )
                    ],
        )
        """

    def testListConfirmedTransactionsByAddressRIBSZ(self):
        """Test ListConfirmedTransactionsByAddressRIBSZ"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
