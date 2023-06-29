# MissingApiKey

missing_api_key

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Specifies an error code, e.g. error 404. | 
**message** | **str** | Specifies the message of the error, i.e. why the error was returned, e.g. error 404 stands for “not found”. | 
**details** | [**List[BannedIpAddressDetailsInner]**](BannedIpAddressDetailsInner.md) |  | [optional] 

## Example

```python
from cryptoapis.models.missing_api_key import MissingApiKey

# TODO update the JSON string below
json = "{}"
# create an instance of MissingApiKey from a JSON string
missing_api_key_instance = MissingApiKey.from_json(json)
# print the JSON string representation of the object
print MissingApiKey.to_json()

# convert the object into a dict
missing_api_key_dict = missing_api_key_instance.to_dict()
# create an instance of MissingApiKey from a dict
missing_api_key_form_dict = missing_api_key.from_dict(missing_api_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


