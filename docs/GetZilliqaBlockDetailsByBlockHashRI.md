# GetZilliqaBlockDetailsByBlockHashRI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_height** | **int** | Represents the number of blocks in the blockchain preceding this specific block. Block numbers have no gaps. A blockchain usually starts with block 0 called the \&quot;Genesis block\&quot;. | 
**difficulty** | **str** | Defines how difficult it is for a specific miner to mine the block. | 
**ds_block** | **int** | Represents the Directory Service block which contains metadata about the miners who participate in the consensus protocol. | 
**ds_difficulty** | **str** | Defines how difficult it is to mine the dsBlocks. | 
**ds_leader** | **str** | Represents a part of the DS Committee which leads the consensus protocol for the epoch. | 
**gas_limit** | **int** | Represents the maximum amount of gas allowed in the block in order to determine how many transactions it can fit. | 
**gas_used** | **int** | Defines how much of the gas for the block has been used. | 
**micro_blocks** | **List[str]** |  | 
**next_block_hash** | **str** | Defines the hash of the next block from the specific blockchain. | 
**previous_block_hash** | **str** | Represents the hash of the previous block, also known as the parent block. | 
**timestamp** | **int** | Defines the exact date/time when this block was mined in Unix Timestamp. | 
**transactions_count** | **int** | Represents the total number of all transactions as part of this block. | 

## Example

```python
from cryptoapis.models.get_zilliqa_block_details_by_block_hash_ri import GetZilliqaBlockDetailsByBlockHashRI

# TODO update the JSON string below
json = "{}"
# create an instance of GetZilliqaBlockDetailsByBlockHashRI from a JSON string
get_zilliqa_block_details_by_block_hash_ri_instance = GetZilliqaBlockDetailsByBlockHashRI.from_json(json)
# print the JSON string representation of the object
print GetZilliqaBlockDetailsByBlockHashRI.to_json()

# convert the object into a dict
get_zilliqa_block_details_by_block_hash_ri_dict = get_zilliqa_block_details_by_block_hash_ri_instance.to_dict()
# create an instance of GetZilliqaBlockDetailsByBlockHashRI from a dict
get_zilliqa_block_details_by_block_hash_ri_form_dict = get_zilliqa_block_details_by_block_hash_ri.from_dict(get_zilliqa_block_details_by_block_hash_ri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


