# EndpointNotAllowedForApiKey

endpoint_not_allowed_for_api_key

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Specifies an error code, e.g. error 404. | 
**message** | **str** | Specifies the message of the error, i.e. why the error was returned, e.g. error 404 stands for “not found”. | 
**details** | [**List[BannedIpAddressDetailsInner]**](BannedIpAddressDetailsInner.md) |  | [optional] 

## Example

```python
from cryptoapis.models.endpoint_not_allowed_for_api_key import EndpointNotAllowedForApiKey

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointNotAllowedForApiKey from a JSON string
endpoint_not_allowed_for_api_key_instance = EndpointNotAllowedForApiKey.from_json(json)
# print the JSON string representation of the object
print EndpointNotAllowedForApiKey.to_json()

# convert the object into a dict
endpoint_not_allowed_for_api_key_dict = endpoint_not_allowed_for_api_key_instance.to_dict()
# create an instance of EndpointNotAllowedForApiKey from a dict
endpoint_not_allowed_for_api_key_form_dict = endpoint_not_allowed_for_api_key.from_dict(endpoint_not_allowed_for_api_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


