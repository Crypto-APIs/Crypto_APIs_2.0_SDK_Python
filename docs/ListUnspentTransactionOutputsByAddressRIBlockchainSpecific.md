# ListUnspentTransactionOutputsByAddressRIBlockchainSpecific


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**v_size** | **int** | Represents the virtual size of this transaction | 
**binding_sig** | **str** | It is used to enforce balance of Spend and Output transfers, in order to prevent their replay across transactions. | 
**expiry_height** | **int** | Represents a block height after which the transaction will expire. | 
**join_split_pub_key** | **str** | Represents an encoding of a JoinSplitSig public validating key. | 
**join_split_sig** | **str** | Is used to sign transactions that contain at least one JoinSplit description. | 
**overwintered** | **bool** | \&quot;Overwinter\&quot; is the network upgrade for the Zcash blockchain. | 
**v_shielded_spend** | [**[ListUnspentTransactionOutputsByAddressRIBlockchainSpecificVShieldedSpend]**](ListUnspentTransactionOutputsByAddressRIBlockchainSpecificVShieldedSpend.md) | Object Array representation of transaction spend descriptions | 
**value_balance** | **str** | Defines the transaction value balance. | 
**version_group_id** | **str** | Represents the transaction version group ID. | 
**v_join_split** | [**[ListUnspentTransactionOutputsByAddressRIBlockchainSpecificVJoinSplit]**](ListUnspentTransactionOutputsByAddressRIBlockchainSpecificVJoinSplit.md) | Represents a sequence of JoinSplit descriptions using BCTV14 proofs. | [optional] 
**v_shielded_output** | [**[GetTransactionDetailsByTransactionIDRIBSZVShieldedOutput]**](GetTransactionDetailsByTransactionIDRIBSZVShieldedOutput.md) | Object Array representation of transaction output descriptions | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


