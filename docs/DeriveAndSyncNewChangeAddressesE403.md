# DeriveAndSyncNewChangeAddressesE403


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Specifies an error code, e.g. error 404. | 
**message** | **str** | Specifies the message of the error, i.e. why the error was returned, e.g. error 404 stands for “not found”. | 
**details** | [**List[BannedIpAddressDetailsInner]**](BannedIpAddressDetailsInner.md) |  | [optional] 

## Example

```python
from cryptoapis.models.derive_and_sync_new_change_addresses_e403 import DeriveAndSyncNewChangeAddressesE403

# TODO update the JSON string below
json = "{}"
# create an instance of DeriveAndSyncNewChangeAddressesE403 from a JSON string
derive_and_sync_new_change_addresses_e403_instance = DeriveAndSyncNewChangeAddressesE403.from_json(json)
# print the JSON string representation of the object
print DeriveAndSyncNewChangeAddressesE403.to_json()

# convert the object into a dict
derive_and_sync_new_change_addresses_e403_dict = derive_and_sync_new_change_addresses_e403_instance.to_dict()
# create an instance of DeriveAndSyncNewChangeAddressesE403 from a dict
derive_and_sync_new_change_addresses_e403_form_dict = derive_and_sync_new_change_addresses_e403.from_dict(derive_and_sync_new_change_addresses_e403_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


