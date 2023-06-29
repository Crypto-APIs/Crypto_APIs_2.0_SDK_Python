# BannedIpAddressDetailsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute** | **str** | Specifies an attribute of the error by name. | 
**message** | **str** | Specifies the details of an attribute as part from the error. | 

## Example

```python
from cryptoapis.models.banned_ip_address_details_inner import BannedIpAddressDetailsInner

# TODO update the JSON string below
json = "{}"
# create an instance of BannedIpAddressDetailsInner from a JSON string
banned_ip_address_details_inner_instance = BannedIpAddressDetailsInner.from_json(json)
# print the JSON string representation of the object
print BannedIpAddressDetailsInner.to_json()

# convert the object into a dict
banned_ip_address_details_inner_dict = banned_ip_address_details_inner_instance.to_dict()
# create an instance of BannedIpAddressDetailsInner from a dict
banned_ip_address_details_inner_form_dict = banned_ip_address_details_inner.from_dict(banned_ip_address_details_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


