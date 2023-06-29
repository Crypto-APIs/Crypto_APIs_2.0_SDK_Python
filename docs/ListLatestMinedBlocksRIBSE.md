# ListLatestMinedBlocksRIBSE

Ethereum

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**difficulty** | **str** | Represents a mathematical value of how hard it is to find a valid hash for this block. | 
**extra_data** | **str** | Represents any data that can be included by the miner in the block. | 
**gas_limit** | **str** | Defines the total gas limit of all transactions in the block. | 
**gas_used** | **str** | Represents the total amount of gas used by all transactions in this block. | 
**mined_in_seconds** | **int** | Specifies the amount of time required for the block to be mined in seconds. | 
**nonce** | **str** | Represents a random value that can be adjusted to satisfy the proof of work | 
**sha3_uncles** | **str** | Defines the combined hash of all uncles for a given parent. | 
**size** | **int** | Represents the total size of the block in Bytes. | 
**total_difficulty** | **str** | Defines the total difficulty of the chain until this block, i.e. how difficult it is for a specific miner to mine a new block. | 
**uncles** | **List[str]** |  | 

## Example

```python
from cryptoapis.models.list_latest_mined_blocks_ribse import ListLatestMinedBlocksRIBSE

# TODO update the JSON string below
json = "{}"
# create an instance of ListLatestMinedBlocksRIBSE from a JSON string
list_latest_mined_blocks_ribse_instance = ListLatestMinedBlocksRIBSE.from_json(json)
# print the JSON string representation of the object
print ListLatestMinedBlocksRIBSE.to_json()

# convert the object into a dict
list_latest_mined_blocks_ribse_dict = list_latest_mined_blocks_ribse_instance.to_dict()
# create an instance of ListLatestMinedBlocksRIBSE from a dict
list_latest_mined_blocks_ribse_form_dict = list_latest_mined_blocks_ribse.from_dict(list_latest_mined_blocks_ribse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


