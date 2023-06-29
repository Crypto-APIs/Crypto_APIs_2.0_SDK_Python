# GetBlockDetailsByBlockHashFromCallbackRI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hash** | **str** | Represents the hash of the block, which is its unique identifier. It represents a cryptographic digital fingerprint made by hashing the block header twice through the SHA256 algorithm. | 
**height** | **int** | Represents the number of blocks in the blockchain preceding this specific block. Block numbers have no gaps. A blockchain usually starts with block 0 called the \&quot;Genesis block\&quot;. | 
**previous_block_hash** | **str** | Represents the hash of the previous block, also known as the parent block. | 
**timestamp** | **int** | Defines the exact date/time when this block was mined in Unix Timestamp. | 
**transactions_count** | **int** | Represents the total number of all transactions as part of this block. | 
**difficulty** | **str** | Represents a mathematical value of how hard it is to find a valid hash for this block. | 
**extra_data** | **str** | Represents any data that can be included by the miner in the block. | 
**gas_limit** | **str** | Represents the amount of gas used by this specific transaction alone. | 
**gas_used** | **str** | Represents the exact unit of gas that was used for the transaction. | 
**mined_in_seconds** | **int** | Specifies the amount of time required for the block to be mined in seconds. | 
**nonce** | **str** | Represents the sequential running number for an address, starting from 0 for the first transaction. E.g., if the nonce of a transaction is 10, it would be the 11th transaction sent from the sender&#39;s address. | 
**sha3_uncles** | **str** | Defines the combined hash of all uncles for a given parent. | 
**size** | **int** | Represents the total size of the block in Bytes. | 
**total_difficulty** | **str** | Defines the total difficulty of the chain until this block, i.e. how difficult it is for a specific miner to mine a new block. | 
**uncles** | **List[str]** |  | 
**blockchain_specific** | [**GetBlockDetailsByBlockHashFromCallbackRIBS**](GetBlockDetailsByBlockHashFromCallbackRIBS.md) |  | 

## Example

```python
from cryptoapis.models.get_block_details_by_block_hash_from_callback_ri import GetBlockDetailsByBlockHashFromCallbackRI

# TODO update the JSON string below
json = "{}"
# create an instance of GetBlockDetailsByBlockHashFromCallbackRI from a JSON string
get_block_details_by_block_hash_from_callback_ri_instance = GetBlockDetailsByBlockHashFromCallbackRI.from_json(json)
# print the JSON string representation of the object
print GetBlockDetailsByBlockHashFromCallbackRI.to_json()

# convert the object into a dict
get_block_details_by_block_hash_from_callback_ri_dict = get_block_details_by_block_hash_from_callback_ri_instance.to_dict()
# create an instance of GetBlockDetailsByBlockHashFromCallbackRI from a dict
get_block_details_by_block_hash_from_callback_ri_form_dict = get_block_details_by_block_hash_from_callback_ri.from_dict(get_block_details_by_block_hash_from_callback_ri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


