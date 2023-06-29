# InsufficientCredits

insufficient_credits

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Specifies an error code, e.g. error 404. | 
**message** | **str** | Specifies the message of the error, i.e. why the error was returned, e.g. error 404 stands for “not found”. | 
**details** | [**List[BannedIpAddressDetailsInner]**](BannedIpAddressDetailsInner.md) |  | [optional] 

## Example

```python
from cryptoapis.models.insufficient_credits import InsufficientCredits

# TODO update the JSON string below
json = "{}"
# create an instance of InsufficientCredits from a JSON string
insufficient_credits_instance = InsufficientCredits.from_json(json)
# print the JSON string representation of the object
print InsufficientCredits.to_json()

# convert the object into a dict
insufficient_credits_dict = insufficient_credits_instance.to_dict()
# create an instance of InsufficientCredits from a dict
insufficient_credits_form_dict = insufficient_credits.from_dict(insufficient_credits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


