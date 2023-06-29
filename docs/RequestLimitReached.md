# RequestLimitReached

request_limit_reached

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Specifies an error code, e.g. error 404. | 
**message** | **str** | Specifies the message of the error, i.e. why the error was returned, e.g. error 404 stands for “not found”. | 
**details** | [**List[BannedIpAddressDetailsInner]**](BannedIpAddressDetailsInner.md) |  | [optional] 

## Example

```python
from cryptoapis.models.request_limit_reached import RequestLimitReached

# TODO update the JSON string below
json = "{}"
# create an instance of RequestLimitReached from a JSON string
request_limit_reached_instance = RequestLimitReached.from_json(json)
# print the JSON string representation of the object
print RequestLimitReached.to_json()

# convert the object into a dict
request_limit_reached_dict = request_limit_reached_instance.to_dict()
# create an instance of RequestLimitReached from a dict
request_limit_reached_form_dict = request_limit_reached.from_dict(request_limit_reached_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


