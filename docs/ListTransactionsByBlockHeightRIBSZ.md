# ListTransactionsByBlockHeightRIBSZ

Zcash

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**binding_sig** | **str** | It is used to enforce balance of Spend and Output transfers, in order to prevent their replay across transactions. | 
**expiry_height** | **int** | Represents a block height after which the transaction will expire. | 
**join_split_pub_key** | **str** | Represents an encoding of a JoinSplitSig public validating key. | 
**join_split_sig** | **str** | Is used to sign transactions that contain at least one JoinSplit description. | 
**locktime** | **int** | Represents the time at which a particular transaction can be added to the blockchain. | 
**overwintered** | **bool** | \&quot;Overwinter\&quot; is the network upgrade for the Zcash blockchain. | 
**size** | **int** | Represents the total size of this transaction. | 
**v_join_split** | [**List[ListTransactionsByBlockHeightRIBSZVJoinSplitInner]**](ListTransactionsByBlockHeightRIBSZVJoinSplitInner.md) | Represents a sequence of JoinSplit descriptions using BCTV14 proofs. | 
**v_shielded_output** | [**List[ListTransactionsByBlockHeightRIBSZVShieldedOutputInner]**](ListTransactionsByBlockHeightRIBSZVShieldedOutputInner.md) | Object Array representation of transaction output descriptions | 
**v_shielded_spend** | [**List[GetTransactionDetailsByTransactionIDRIBSZVShieldedSpendInner]**](GetTransactionDetailsByTransactionIDRIBSZVShieldedSpendInner.md) | Object Array representation of transaction spend descriptions | 
**value_balance** | **str** | Defines the transaction value balance. | 
**version** | **int** | Represents the transaction version number. | 
**version_group_id** | **str** | Represents the transaction version group ID. | 
**vin** | [**List[ListTransactionsByBlockHeightRIBSZVinInner]**](ListTransactionsByBlockHeightRIBSZVinInner.md) | Object Array representation of transaction inputs | 
**vout** | [**List[ListTransactionsByBlockHeightRIBSZVoutInner]**](ListTransactionsByBlockHeightRIBSZVoutInner.md) | Object Array representation of transaction outputs | 

## Example

```python
from cryptoapis.models.list_transactions_by_block_height_ribsz import ListTransactionsByBlockHeightRIBSZ

# TODO update the JSON string below
json = "{}"
# create an instance of ListTransactionsByBlockHeightRIBSZ from a JSON string
list_transactions_by_block_height_ribsz_instance = ListTransactionsByBlockHeightRIBSZ.from_json(json)
# print the JSON string representation of the object
print ListTransactionsByBlockHeightRIBSZ.to_json()

# convert the object into a dict
list_transactions_by_block_height_ribsz_dict = list_transactions_by_block_height_ribsz_instance.to_dict()
# create an instance of ListTransactionsByBlockHeightRIBSZ from a dict
list_transactions_by_block_height_ribsz_form_dict = list_transactions_by_block_height_ribsz.from_dict(list_transactions_by_block_height_ribsz_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


