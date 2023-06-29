# GetBlockDetailsByBlockHeightFromCallbackRIBSE

Ethereum

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**difficulty** | **str** | Represents a mathematical value of how hard it is to find a valid hash for this block. | 
**extra_data** | **str** | Represents any data that can be included by the miner in the block. | 
**gas_limit** | **str** | Defines the total gas limit of all transactions in the block. | 
**gas_used** | **str** | Represents the total amount of gas used by all transactions in this block. | 
**mined_in_seconds** | **int** | Specifies the amount of time required for the block to be mined in seconds. | 
**nonce** | **str** | Represents the sequential running number for an address, starting from 0 for the first transaction. E.g., if the nonce of a transaction is 10, it would be the 11th transaction sent from the sender&#39;s address. | 
**sha3_uncles** | **str** | Defines the combined hash of all uncles for a given parent. | 
**size** | **int** | Represents the total size of the block in Bytes. | 
**total_difficulty** | **str** | Defines the total difficulty of the chain until this block, i.e. how difficult it is for a specific miner to mine a new block. | 
**uncles** | **List[str]** |  | [optional] 

## Example

```python
from cryptoapis.models.get_block_details_by_block_height_from_callback_ribse import GetBlockDetailsByBlockHeightFromCallbackRIBSE

# TODO update the JSON string below
json = "{}"
# create an instance of GetBlockDetailsByBlockHeightFromCallbackRIBSE from a JSON string
get_block_details_by_block_height_from_callback_ribse_instance = GetBlockDetailsByBlockHeightFromCallbackRIBSE.from_json(json)
# print the JSON string representation of the object
print GetBlockDetailsByBlockHeightFromCallbackRIBSE.to_json()

# convert the object into a dict
get_block_details_by_block_height_from_callback_ribse_dict = get_block_details_by_block_height_from_callback_ribse_instance.to_dict()
# create an instance of GetBlockDetailsByBlockHeightFromCallbackRIBSE from a dict
get_block_details_by_block_height_from_callback_ribse_form_dict = get_block_details_by_block_height_from_callback_ribse.from_dict(get_block_details_by_block_height_from_callback_ribse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


