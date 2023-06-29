# GetLastMinedBlockRIBSBC

Bitcoin Cash

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bits** | **str** | A sub-unit of BCH equal to 0.000001 BCH, or 100 Satoshi, and is the same as microbitcoincash (μBCH). Bits have two-decimal precision. | 
**chainwork** | **str** | Represents a hexadecimal number of all the hashes necessary to produce the current chain. E.g., when converting 0000000000000000000000000000000000000000000086859f7a841475b236fd to a decimal you get 635262017308958427068157 hashes, or 635262 exahashes. | 
**difficulty** | **str** | Numeric representation of the block difficulty | [optional] 
**merkle_root** | **str** | Defines the single and final (root) node of a Merkle tree. It is the combined hash of all transactions&#39; hashes that are part of a blockchain block. | 
**nonce** | **str** | Represents a random value that can be adjusted to satisfy the proof of work | 
**size** | **int** | Represents the total size of the block in Bytes. | 
**version** | **int** | Represents the version of the specific block on the blockchain. | 
**version_hex** | **str** | Is the hexadecimal string representation of the block&#39;s version. | 

## Example

```python
from cryptoapis.models.get_last_mined_block_ribsbc import GetLastMinedBlockRIBSBC

# TODO update the JSON string below
json = "{}"
# create an instance of GetLastMinedBlockRIBSBC from a JSON string
get_last_mined_block_ribsbc_instance = GetLastMinedBlockRIBSBC.from_json(json)
# print the JSON string representation of the object
print GetLastMinedBlockRIBSBC.to_json()

# convert the object into a dict
get_last_mined_block_ribsbc_dict = get_last_mined_block_ribsbc_instance.to_dict()
# create an instance of GetLastMinedBlockRIBSBC from a dict
get_last_mined_block_ribsbc_form_dict = get_last_mined_block_ribsbc.from_dict(get_last_mined_block_ribsbc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


