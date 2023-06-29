# ListLatestMinedBlocksRIBST

Tron

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bandwidth_used** | **str** | Representation of the blocks&#39; bandwidth limit. | [optional] 
**burned_trx** | **str** | Representation of the blocks&#39; burned TRX. | [optional] 
**energy_used** | **str** | Representation of the blocks&#39; energy used. | [optional] 
**size** | **int** | Represents the total size of the block in Bytes. | 

## Example

```python
from cryptoapis.models.list_latest_mined_blocks_ribst import ListLatestMinedBlocksRIBST

# TODO update the JSON string below
json = "{}"
# create an instance of ListLatestMinedBlocksRIBST from a JSON string
list_latest_mined_blocks_ribst_instance = ListLatestMinedBlocksRIBST.from_json(json)
# print the JSON string representation of the object
print ListLatestMinedBlocksRIBST.to_json()

# convert the object into a dict
list_latest_mined_blocks_ribst_dict = list_latest_mined_blocks_ribst_instance.to_dict()
# create an instance of ListLatestMinedBlocksRIBST from a dict
list_latest_mined_blocks_ribst_form_dict = list_latest_mined_blocks_ribst.from_dict(list_latest_mined_blocks_ribst_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


