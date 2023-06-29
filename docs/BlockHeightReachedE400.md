# BlockHeightReachedE400


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Specifies an error code, e.g. error 404. | 
**message** | **str** | Specifies the message of the error, i.e. why the error was returned, e.g. error 404 stands for “not found”. | 
**details** | [**List[BannedIpAddressDetailsInner]**](BannedIpAddressDetailsInner.md) |  | [optional] 

## Example

```python
from cryptoapis.models.block_height_reached_e400 import BlockHeightReachedE400

# TODO update the JSON string below
json = "{}"
# create an instance of BlockHeightReachedE400 from a JSON string
block_height_reached_e400_instance = BlockHeightReachedE400.from_json(json)
# print the JSON string representation of the object
print BlockHeightReachedE400.to_json()

# convert the object into a dict
block_height_reached_e400_dict = block_height_reached_e400_instance.to_dict()
# create an instance of BlockHeightReachedE400 from a dict
block_height_reached_e400_form_dict = block_height_reached_e400.from_dict(block_height_reached_e400_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


