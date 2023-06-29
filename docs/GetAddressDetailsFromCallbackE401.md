# GetAddressDetailsFromCallbackE401


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Specifies an error code, e.g. error 404. | 
**message** | **str** | Specifies the message of the error, i.e. why the error was returned, e.g. error 404 stands for “not found”. | 
**details** | [**List[BannedIpAddressDetailsInner]**](BannedIpAddressDetailsInner.md) |  | [optional] 

## Example

```python
from cryptoapis.models.get_address_details_from_callback_e401 import GetAddressDetailsFromCallbackE401

# TODO update the JSON string below
json = "{}"
# create an instance of GetAddressDetailsFromCallbackE401 from a JSON string
get_address_details_from_callback_e401_instance = GetAddressDetailsFromCallbackE401.from_json(json)
# print the JSON string representation of the object
print GetAddressDetailsFromCallbackE401.to_json()

# convert the object into a dict
get_address_details_from_callback_e401_dict = get_address_details_from_callback_e401_instance.to_dict()
# create an instance of GetAddressDetailsFromCallbackE401 from a dict
get_address_details_from_callback_e401_form_dict = get_address_details_from_callback_e401.from_dict(get_address_details_from_callback_e401_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


