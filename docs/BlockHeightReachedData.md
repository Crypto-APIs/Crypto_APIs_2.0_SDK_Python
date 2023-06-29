# BlockHeightReachedData

Specifies all data, as attributes, included into the callback notification, which depends on the `event`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product** | **str** | Represents the Crypto APIs 2.0 product which sends the callback. | 
**event** | **str** | Defines the specific event, for which a callback subscription is set. | 
**item** | [**BlockHeightReachedDataItem**](BlockHeightReachedDataItem.md) |  | 

## Example

```python
from cryptoapis.models.block_height_reached_data import BlockHeightReachedData

# TODO update the JSON string below
json = "{}"
# create an instance of BlockHeightReachedData from a JSON string
block_height_reached_data_instance = BlockHeightReachedData.from_json(json)
# print the JSON string representation of the object
print BlockHeightReachedData.to_json()

# convert the object into a dict
block_height_reached_data_dict = block_height_reached_data_instance.to_dict()
# create an instance of BlockHeightReachedData from a dict
block_height_reached_data_form_dict = block_height_reached_data.from_dict(block_height_reached_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


