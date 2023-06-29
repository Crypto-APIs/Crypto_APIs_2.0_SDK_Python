# GetBlockDetailsByBlockHashRI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hash** | **str** | Represents the hash of the block, which is its unique identifier. It represents a cryptographic digital fingerprint made by hashing the block header twice through the SHA256 algorithm. | 
**height** | **int** | Represents the number of blocks in the blockchain preceding this specific block. Block numbers have no gaps. A blockchain usually starts with block 0 called the \&quot;Genesis block\&quot;. | 
**next_block_hash** | **str** | Represents the hash of the next block. When this is the last block of the blockchain this value will be an empty string. | 
**previous_block_hash** | **str** | Represents the hash of the previous block, also known as the parent block. | 
**timestamp** | **int** | Defines the exact date/time when this block was mined in Unix Timestamp. | 
**transactions_count** | **int** | Represents the total number of all transactions as part of this block. | 
**blockchain_specific** | [**GetBlockDetailsByBlockHashRIBS**](GetBlockDetailsByBlockHashRIBS.md) |  | 

## Example

```python
from cryptoapis.models.get_block_details_by_block_hash_ri import GetBlockDetailsByBlockHashRI

# TODO update the JSON string below
json = "{}"
# create an instance of GetBlockDetailsByBlockHashRI from a JSON string
get_block_details_by_block_hash_ri_instance = GetBlockDetailsByBlockHashRI.from_json(json)
# print the JSON string representation of the object
print GetBlockDetailsByBlockHashRI.to_json()

# convert the object into a dict
get_block_details_by_block_hash_ri_dict = get_block_details_by_block_hash_ri_instance.to_dict()
# create an instance of GetBlockDetailsByBlockHashRI from a dict
get_block_details_by_block_hash_ri_form_dict = get_block_details_by_block_hash_ri.from_dict(get_block_details_by_block_hash_ri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


