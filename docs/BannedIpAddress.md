# BannedIpAddress

banned_ip_address

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Specifies an error code, e.g. error 404. | 
**message** | **str** | Specifies the message of the error, i.e. why the error was returned, e.g. error 404 stands for “not found”. | 
**details** | [**List[BannedIpAddressDetailsInner]**](BannedIpAddressDetailsInner.md) |  | [optional] 

## Example

```python
from cryptoapis.models.banned_ip_address import BannedIpAddress

# TODO update the JSON string below
json = "{}"
# create an instance of BannedIpAddress from a JSON string
banned_ip_address_instance = BannedIpAddress.from_json(json)
# print the JSON string representation of the object
print BannedIpAddress.to_json()

# convert the object into a dict
banned_ip_address_dict = banned_ip_address_instance.to_dict()
# create an instance of BannedIpAddress from a dict
banned_ip_address_form_dict = banned_ip_address.from_dict(banned_ip_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


