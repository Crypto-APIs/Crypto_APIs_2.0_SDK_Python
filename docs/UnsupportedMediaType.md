# UnsupportedMediaType

unsupported_media_type

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Specifies an error code, e.g. error 404. | 
**message** | **str** | Specifies the message of the error, i.e. why the error was returned, e.g. error 404 stands for “not found”. | 
**details** | [**List[BannedIpAddressDetailsInner]**](BannedIpAddressDetailsInner.md) |  | [optional] 

## Example

```python
from cryptoapis.models.unsupported_media_type import UnsupportedMediaType

# TODO update the JSON string below
json = "{}"
# create an instance of UnsupportedMediaType from a JSON string
unsupported_media_type_instance = UnsupportedMediaType.from_json(json)
# print the JSON string representation of the object
print UnsupportedMediaType.to_json()

# convert the object into a dict
unsupported_media_type_dict = unsupported_media_type_instance.to_dict()
# create an instance of UnsupportedMediaType from a dict
unsupported_media_type_form_dict = unsupported_media_type.from_dict(unsupported_media_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


