# NewBlockE409


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Specifies an error code, e.g. error 404. | 
**message** | **str** | Specifies the message of the error, i.e. why the error was returned, e.g. error 404 stands for “not found”. | 
**details** | [**List[BannedIpAddressDetailsInner]**](BannedIpAddressDetailsInner.md) |  | [optional] 

## Example

```python
from cryptoapis.models.new_block_e409 import NewBlockE409

# TODO update the JSON string below
json = "{}"
# create an instance of NewBlockE409 from a JSON string
new_block_e409_instance = NewBlockE409.from_json(json)
# print the JSON string representation of the object
print NewBlockE409.to_json()

# convert the object into a dict
new_block_e409_dict = new_block_e409_instance.to_dict()
# create an instance of NewBlockE409 from a dict
new_block_e409_form_dict = new_block_e409.from_dict(new_block_e409_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


