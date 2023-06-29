# UriNotFound

uri_not_found

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Specifies an error code, e.g. error 404. | 
**message** | **str** | Specifies the message of the error, i.e. why the error was returned, e.g. error 404 stands for “not found”. | 
**details** | [**List[BannedIpAddressDetailsInner]**](BannedIpAddressDetailsInner.md) |  | [optional] 

## Example

```python
from cryptoapis.models.uri_not_found import UriNotFound

# TODO update the JSON string below
json = "{}"
# create an instance of UriNotFound from a JSON string
uri_not_found_instance = UriNotFound.from_json(json)
# print the JSON string representation of the object
print UriNotFound.to_json()

# convert the object into a dict
uri_not_found_dict = uri_not_found_instance.to_dict()
# create an instance of UriNotFound from a dict
uri_not_found_form_dict = uri_not_found.from_dict(uri_not_found_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


