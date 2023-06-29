# GetBlockDetailsByBlockHashFromCallbackRIBST

Tron

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bandwidth_used** | **str** | Represents the bandwidth used for the transaction. | 
**burned_trx** | **str** | Represents the block burned TRX. | 
**energy_used** | **str** | Representats the used energy for the transaction. | 
**size** | **int** | Represents the total size of the block in Bytes. | 

## Example

```python
from cryptoapis.models.get_block_details_by_block_hash_from_callback_ribst import GetBlockDetailsByBlockHashFromCallbackRIBST

# TODO update the JSON string below
json = "{}"
# create an instance of GetBlockDetailsByBlockHashFromCallbackRIBST from a JSON string
get_block_details_by_block_hash_from_callback_ribst_instance = GetBlockDetailsByBlockHashFromCallbackRIBST.from_json(json)
# print the JSON string representation of the object
print GetBlockDetailsByBlockHashFromCallbackRIBST.to_json()

# convert the object into a dict
get_block_details_by_block_hash_from_callback_ribst_dict = get_block_details_by_block_hash_from_callback_ribst_instance.to_dict()
# create an instance of GetBlockDetailsByBlockHashFromCallbackRIBST from a dict
get_block_details_by_block_hash_from_callback_ribst_form_dict = get_block_details_by_block_hash_from_callback_ribst.from_dict(get_block_details_by_block_hash_from_callback_ribst_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


