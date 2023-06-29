# LimitGreaterThanAllowed

limit_greater_than_allowed

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Specifies an error code, e.g. error 404. | 
**message** | **str** | Specifies the message of the error, i.e. why the error was returned, e.g. error 404 stands for “not found”. | 
**details** | [**List[BannedIpAddressDetailsInner]**](BannedIpAddressDetailsInner.md) |  | [optional] 

## Example

```python
from cryptoapis.models.limit_greater_than_allowed import LimitGreaterThanAllowed

# TODO update the JSON string below
json = "{}"
# create an instance of LimitGreaterThanAllowed from a JSON string
limit_greater_than_allowed_instance = LimitGreaterThanAllowed.from_json(json)
# print the JSON string representation of the object
print LimitGreaterThanAllowed.to_json()

# convert the object into a dict
limit_greater_than_allowed_dict = limit_greater_than_allowed_instance.to_dict()
# create an instance of LimitGreaterThanAllowed from a dict
limit_greater_than_allowed_form_dict = limit_greater_than_allowed.from_dict(limit_greater_than_allowed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


