# ListTransactionsByBlockHashRIBSZVJoinSplitInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anchor** | **str** | Defines a Merkle tree root of a note commitment tree which uniquely identifies a note commitment tree state given the assumed security properties of the Merkle tree’s  hash function. | 
**cipher_texts** | **List[str]** |  | 
**commitments** | **List[str]** |  | 
**macs** | **List[str]** |  | 
**nullifiers** | **List[str]** |  | 
**one_time_pub_key** | **str** | Defines the one time public key. | 
**proof** | **str** | Defines the proof. | 
**random_seed** | **str** | Represents a 256-bit seed that must be chosen independently at random for each JoinSplit description. | 
**v_pub_new** | **str** | Defines the value that the joinSplit transfer will insert into the transparent transaction value pool. | 
**v_pub_old** | **str** | Defines the value that the joinSplit transfer will remove from the transparent transaction value pool. | 

## Example

```python
from cryptoapis.models.list_transactions_by_block_hash_ribszv_join_split_inner import ListTransactionsByBlockHashRIBSZVJoinSplitInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListTransactionsByBlockHashRIBSZVJoinSplitInner from a JSON string
list_transactions_by_block_hash_ribszv_join_split_inner_instance = ListTransactionsByBlockHashRIBSZVJoinSplitInner.from_json(json)
# print the JSON string representation of the object
print ListTransactionsByBlockHashRIBSZVJoinSplitInner.to_json()

# convert the object into a dict
list_transactions_by_block_hash_ribszv_join_split_inner_dict = list_transactions_by_block_hash_ribszv_join_split_inner_instance.to_dict()
# create an instance of ListTransactionsByBlockHashRIBSZVJoinSplitInner from a dict
list_transactions_by_block_hash_ribszv_join_split_inner_form_dict = list_transactions_by_block_hash_ribszv_join_split_inner.from_dict(list_transactions_by_block_hash_ribszv_join_split_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


