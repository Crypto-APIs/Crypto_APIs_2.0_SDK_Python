# ListSyncedAddressesE400


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Specifies an error code, e.g. error 404. | 
**message** | **str** | Specifies the message of the error, i.e. why the error was returned, e.g. error 404 stands for “not found”. | 
**details** | [**List[BannedIpAddressDetailsInner]**](BannedIpAddressDetailsInner.md) |  | [optional] 

## Example

```python
from cryptoapis.models.list_synced_addresses_e400 import ListSyncedAddressesE400

# TODO update the JSON string below
json = "{}"
# create an instance of ListSyncedAddressesE400 from a JSON string
list_synced_addresses_e400_instance = ListSyncedAddressesE400.from_json(json)
# print the JSON string representation of the object
print ListSyncedAddressesE400.to_json()

# convert the object into a dict
list_synced_addresses_e400_dict = list_synced_addresses_e400_instance.to_dict()
# create an instance of ListSyncedAddressesE400 from a dict
list_synced_addresses_e400_form_dict = list_synced_addresses_e400.from_dict(list_synced_addresses_e400_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


