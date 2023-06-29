# GetLastMinedBlockRIBSBSC

Binance Smart Chain

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**difficulty** | **str** | String representation of the block difficulty | [optional] 
**extra_data** | **str** | Represents any data that can be included by the miner in the block. | 
**gas_limit** | **str** | Defines the total gas limit of all transactions in the block. | 
**gas_used** | **str** | Represents the total amount of gas used by all transactions in this block. | 
**mined_in_seconds** | **int** | Specifies the amount of time required for the block to be mined in second | 
**nonce** | **str** | Represents a random value that can be adjusted to satisfy the proof of work | 
**sha3_uncles** | **str** | Defines the combined hash of all uncles for a given parent. | 
**size** | **int** | Represents the total size of the block in Bytes. | 
**total_difficulty** | **str** | Defines the total difficulty of the chain until this block, i.e. how difficult it is for a specific miner to mine a new block | 
**uncles** | **List[str]** |  | 

## Example

```python
from cryptoapis.models.get_last_mined_block_ribsbsc import GetLastMinedBlockRIBSBSC

# TODO update the JSON string below
json = "{}"
# create an instance of GetLastMinedBlockRIBSBSC from a JSON string
get_last_mined_block_ribsbsc_instance = GetLastMinedBlockRIBSBSC.from_json(json)
# print the JSON string representation of the object
print GetLastMinedBlockRIBSBSC.to_json()

# convert the object into a dict
get_last_mined_block_ribsbsc_dict = get_last_mined_block_ribsbsc_instance.to_dict()
# create an instance of GetLastMinedBlockRIBSBSC from a dict
get_last_mined_block_ribsbsc_form_dict = get_last_mined_block_ribsbsc.from_dict(get_last_mined_block_ribsbsc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


