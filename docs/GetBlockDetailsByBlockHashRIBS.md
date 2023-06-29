# GetBlockDetailsByBlockHashRIBS


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**difficulty** | **str** | Represents a mathematical value of how hard it is to find a valid hash for this block. | 
**bits** | **str** | Represents a specific sub-unit of Zcash. Bits have two-decimal precision | 
**chainwork** | **str** | Represents a hexadecimal number of all the hashes necessary to produce the current chain. E.g., when converting 0000000000000000000000000000000000000000000086859f7a841475b236fd to a decimal you get 635262017308958427068157 hashes, or 635262 exahashes. | 
**merkle_root** | **str** | Defines the single and final (root) node of a Merkle tree. It is the combined hash of all transactions&#39; hashes that are part of a blockchain block. | 
**nonce** | **str** | Represents a random value that can be adjusted to satisfy the Proof of Work. | 
**size** | **int** | Represents the total size of the block in Bytes. | 
**stripped_size** | **int** | Defines the numeric representation of the block size excluding the witness data. | 
**version** | **int** | Represents the block version number. | 
**version_hex** | **str** | Is the hexadecimal string representation of the block&#39;s version. | 
**weight** | **int** | Represents a measurement to compare the size of different transactions to each other in proportion to the block size limit. | 
**extra_data** | **str** | Represents any data that can be included by the miner in the block. | 
**gas_limit** | **str** | Defines the total gas limit of all transactions in the block. | 
**gas_used** | **str** | Represents the total amount of gas used by all transactions in this block. | 
**mined_in_seconds** | **int** | Specifies the amount of time required for the block to be mined in seconds. | 
**sha3_uncles** | **str** | Defines the combined hash of all uncles for a given parent. | 
**total_difficulty** | **str** | Defines the total difficulty of the chain until this block, i.e. how difficult it is for a specific miner to mine a new block. | 
**uncles** | **List[str]** |  | 

## Example

```python
from cryptoapis.models.get_block_details_by_block_hash_ribs import GetBlockDetailsByBlockHashRIBS

# TODO update the JSON string below
json = "{}"
# create an instance of GetBlockDetailsByBlockHashRIBS from a JSON string
get_block_details_by_block_hash_ribs_instance = GetBlockDetailsByBlockHashRIBS.from_json(json)
# print the JSON string representation of the object
print GetBlockDetailsByBlockHashRIBS.to_json()

# convert the object into a dict
get_block_details_by_block_hash_ribs_dict = get_block_details_by_block_hash_ribs_instance.to_dict()
# create an instance of GetBlockDetailsByBlockHashRIBS from a dict
get_block_details_by_block_hash_ribs_form_dict = get_block_details_by_block_hash_ribs.from_dict(get_block_details_by_block_hash_ribs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


