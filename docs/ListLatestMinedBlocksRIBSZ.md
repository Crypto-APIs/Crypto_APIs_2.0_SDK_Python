# ListLatestMinedBlocksRIBSZ

Zcash

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bits** | **str** | Represents a specific sub-unit of Zcash. Bits have two-decimal precision | 
**chainwork** | **str** | Represents a hexadecimal number of all the hashes necessary to produce the current chain. E.g., when converting 0000000000000000000000000000000000000000000086859f7a841475b236fd to a decimal you get 635262017308958427068157 hashes, or 635262 exahashes. | 
**difficulty** | **str** | Represents a mathematical value of how hard it is to find a valid hash for this block. | 
**merkle_root** | **str** | Defines the single and final (root) node of a Merkle tree. It is the combined hash of all transactions&#39; hashes that are part of a blockchain block. | 
**nonce** | **str** | Represents a random value that can be adjusted to satisfy the proof of work | 
**size** | **int** | Represents the total size of the block in Bytes. | 
**version** | **int** | Represents the transaction version number. | 

## Example

```python
from cryptoapis.models.list_latest_mined_blocks_ribsz import ListLatestMinedBlocksRIBSZ

# TODO update the JSON string below
json = "{}"
# create an instance of ListLatestMinedBlocksRIBSZ from a JSON string
list_latest_mined_blocks_ribsz_instance = ListLatestMinedBlocksRIBSZ.from_json(json)
# print the JSON string representation of the object
print ListLatestMinedBlocksRIBSZ.to_json()

# convert the object into a dict
list_latest_mined_blocks_ribsz_dict = list_latest_mined_blocks_ribsz_instance.to_dict()
# create an instance of ListLatestMinedBlocksRIBSZ from a dict
list_latest_mined_blocks_ribsz_form_dict = list_latest_mined_blocks_ribsz.from_dict(list_latest_mined_blocks_ribsz_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


