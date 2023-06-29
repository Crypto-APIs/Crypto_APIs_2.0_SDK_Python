# ListLatestMinedBlocksRIBSB

Bitcoin

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bits** | **str** | A sub-unit of BCH equal to 0.000001 BCH, or 100 Satoshi, and is the same as microbitcoincash (μBCH). Bits have two-decimal precision. | 
**chainwork** | **str** | Represents a hexadecimal number of all the hashes necessary to produce the current chain. E.g., when converting 0000000000000000000000000000000000000000000086859f7a841475b236fd to a decimal you get 635262017308958427068157 hashes, or 635262 exahashes. | 
**difficulty** | **str** | Represents a mathematical value of how hard it is to find a valid hash for this block. | [optional] 
**merkle_root** | **str** | Defines the single and final (root) node of a Merkle tree. It is the combined hash of all transactions&#39; hashes that are part of a blockchain block. | 
**nonce** | **int** | Represents a random value that can be adjusted to satisfy the proof of work | [optional] 
**size** | **int** | Represents the block size | [optional] 
**stripped_size** | **int** | Defines the numeric representation of the block size excluding the witness data. | 
**version** | **int** | Represents the version of the specific block on the blockchain. | 
**version_hex** | **str** | Is the hexadecimal string representation of the block&#39;s version. | 
**weight** | **int** | Represents a measurement to compare the size of different transactions to each other in proportion to the block size limit. | 

## Example

```python
from cryptoapis.models.list_latest_mined_blocks_ribsb import ListLatestMinedBlocksRIBSB

# TODO update the JSON string below
json = "{}"
# create an instance of ListLatestMinedBlocksRIBSB from a JSON string
list_latest_mined_blocks_ribsb_instance = ListLatestMinedBlocksRIBSB.from_json(json)
# print the JSON string representation of the object
print ListLatestMinedBlocksRIBSB.to_json()

# convert the object into a dict
list_latest_mined_blocks_ribsb_dict = list_latest_mined_blocks_ribsb_instance.to_dict()
# create an instance of ListLatestMinedBlocksRIBSB from a dict
list_latest_mined_blocks_ribsb_form_dict = list_latest_mined_blocks_ribsb.from_dict(list_latest_mined_blocks_ribsb_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


