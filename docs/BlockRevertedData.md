# BlockRevertedData

Specifies all data, as attributes, included into the callback notification, which depends on the `event`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product** | **str** | Represents the Crypto APIs 2.0 product which sends the callback. | 
**event** | **str** | Defines the specific event, for which a callback subscription is set. | 
**item** | [**BlockRevertedDataItem**](BlockRevertedDataItem.md) |  | 

## Example

```python
from cryptoapis.models.block_reverted_data import BlockRevertedData

# TODO update the JSON string below
json = "{}"
# create an instance of BlockRevertedData from a JSON string
block_reverted_data_instance = BlockRevertedData.from_json(json)
# print the JSON string representation of the object
print BlockRevertedData.to_json()

# convert the object into a dict
block_reverted_data_dict = block_reverted_data_instance.to_dict()
# create an instance of BlockRevertedData from a dict
block_reverted_data_form_dict = block_reverted_data.from_dict(block_reverted_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


