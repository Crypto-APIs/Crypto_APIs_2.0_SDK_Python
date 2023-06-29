# Unimplemented

unimplemented

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Specifies an error code, e.g. error 404. | 
**message** | **str** | Specifies the message of the error, i.e. why the error was returned, e.g. error 404 stands for “not found”. | 
**details** | [**List[BannedIpAddressDetailsInner]**](BannedIpAddressDetailsInner.md) |  | [optional] 

## Example

```python
from cryptoapis.models.unimplemented import Unimplemented

# TODO update the JSON string below
json = "{}"
# create an instance of Unimplemented from a JSON string
unimplemented_instance = Unimplemented.from_json(json)
# print the JSON string representation of the object
print Unimplemented.to_json()

# convert the object into a dict
unimplemented_dict = unimplemented_instance.to_dict()
# create an instance of Unimplemented from a dict
unimplemented_form_dict = unimplemented.from_dict(unimplemented_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


