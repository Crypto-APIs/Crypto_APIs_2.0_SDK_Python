# ListSyncedAddressesRI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Represents the address. | 
**index** | **int** | Represents the index position of the transaction in the specific block. | 

## Example

```python
from cryptoapis.models.list_synced_addresses_ri import ListSyncedAddressesRI

# TODO update the JSON string below
json = "{}"
# create an instance of ListSyncedAddressesRI from a JSON string
list_synced_addresses_ri_instance = ListSyncedAddressesRI.from_json(json)
# print the JSON string representation of the object
print ListSyncedAddressesRI.to_json()

# convert the object into a dict
list_synced_addresses_ri_dict = list_synced_addresses_ri_instance.to_dict()
# create an instance of ListSyncedAddressesRI from a dict
list_synced_addresses_ri_form_dict = list_synced_addresses_ri.from_dict(list_synced_addresses_ri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


