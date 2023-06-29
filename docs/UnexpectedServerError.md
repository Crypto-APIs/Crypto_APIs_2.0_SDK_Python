# UnexpectedServerError

unexpected_server_error

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Specifies an error code, e.g. error 404. | 
**message** | **str** | Specifies the message of the error, i.e. why the error was returned, e.g. error 404 stands for “not found”. | 
**details** | [**List[BannedIpAddressDetailsInner]**](BannedIpAddressDetailsInner.md) |  | [optional] 

## Example

```python
from cryptoapis.models.unexpected_server_error import UnexpectedServerError

# TODO update the JSON string below
json = "{}"
# create an instance of UnexpectedServerError from a JSON string
unexpected_server_error_instance = UnexpectedServerError.from_json(json)
# print the JSON string representation of the object
print UnexpectedServerError.to_json()

# convert the object into a dict
unexpected_server_error_dict = unexpected_server_error_instance.to_dict()
# create an instance of UnexpectedServerError from a dict
unexpected_server_error_form_dict = unexpected_server_error.from_dict(unexpected_server_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


