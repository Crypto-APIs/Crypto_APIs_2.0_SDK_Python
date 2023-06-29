# GetBlockDetailsByBlockHashRIBSB

Bitcoin

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**difficulty** | **str** | Represents a mathematical value of how hard it is to find a valid hash for this block. | 
**bits** | **str** | A sub-unit of BTC equal to 0.000001 BTC, or 100 Satoshi, and is the same as microbitcoin (μBTC). Bits have two-decimal precision. | 
**chainwork** | **str** | Represents a hexadecimal number of all the hashes necessary to produce the current chain. E.g., when converting 0000000000000000000000000000000000000000000086859f7a841475b236fd to a decimal you get 635262017308958427068157 hashes, or 635262 exahashes. | 
**merkle_root** | **str** | Defines the single and final (root) node of a Merkle tree. It is the combined hash of all transactions&#39; hashes that are part of a blockchain block. | 
**nonce** | **int** | Represents a random value that can be adjusted to satisfy the Proof of Work. | 
**size** | **int** | Represents the total size of the block in Bytes. | 
**stripped_size** | **int** | Defines the numeric representation of the block size excluding the witness data. | 
**version** | **int** | Represents the version of the specific block on the blockchain. | 
**version_hex** | **str** | Is the hexadecimal string representation of the block&#39;s version. | 
**weight** | **int** | Represents a measurement to compare the size of different transactions to each other in proportion to the block size limit. | 

## Example

```python
from cryptoapis.models.get_block_details_by_block_hash_ribsb import GetBlockDetailsByBlockHashRIBSB

# TODO update the JSON string below
json = "{}"
# create an instance of GetBlockDetailsByBlockHashRIBSB from a JSON string
get_block_details_by_block_hash_ribsb_instance = GetBlockDetailsByBlockHashRIBSB.from_json(json)
# print the JSON string representation of the object
print GetBlockDetailsByBlockHashRIBSB.to_json()

# convert the object into a dict
get_block_details_by_block_hash_ribsb_dict = get_block_details_by_block_hash_ribsb_instance.to_dict()
# create an instance of GetBlockDetailsByBlockHashRIBSB from a dict
get_block_details_by_block_hash_ribsb_form_dict = get_block_details_by_block_hash_ribsb.from_dict(get_block_details_by_block_hash_ribsb_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


