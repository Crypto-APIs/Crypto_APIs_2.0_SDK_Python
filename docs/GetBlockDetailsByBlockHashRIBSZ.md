# GetBlockDetailsByBlockHashRIBSZ

Zcash

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**difficulty** | **str** | Represents a mathematical value of how hard it is to find a valid hash for this block. | 
**bits** | **str** | Represents a specific sub-unit of Zcash. Bits have two-decimal precision | 
**chainwork** | **str** | Represents a hexadecimal number of all the hashes necessary to produce the current chain. E.g., when converting 0000000000000000000000000000000000000000000086859f7a841475b236fd to a decimal you get 635262017308958427068157 hashes, or 635262 exahashes. | 
**merkle_root** | **str** | Defines the single and final (root) node of a Merkle tree. It is the combined hash of all transactions&#39; hashes that are part of a blockchain block. | 
**nonce** | **str** | Represents a random value that can be adjusted to satisfy the Proof of Work. | 
**size** | **int** | Represents the total size of the block in Bytes. | 
**version** | **int** | Represents the block version number. | 

## Example

```python
from cryptoapis.models.get_block_details_by_block_hash_ribsz import GetBlockDetailsByBlockHashRIBSZ

# TODO update the JSON string below
json = "{}"
# create an instance of GetBlockDetailsByBlockHashRIBSZ from a JSON string
get_block_details_by_block_hash_ribsz_instance = GetBlockDetailsByBlockHashRIBSZ.from_json(json)
# print the JSON string representation of the object
print GetBlockDetailsByBlockHashRIBSZ.to_json()

# convert the object into a dict
get_block_details_by_block_hash_ribsz_dict = get_block_details_by_block_hash_ribsz_instance.to_dict()
# create an instance of GetBlockDetailsByBlockHashRIBSZ from a dict
get_block_details_by_block_hash_ribsz_form_dict = get_block_details_by_block_hash_ribsz.from_dict(get_block_details_by_block_hash_ribsz_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


