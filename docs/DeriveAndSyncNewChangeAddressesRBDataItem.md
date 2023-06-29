# DeriveAndSyncNewChangeAddressesRBDataItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extended_public_key** | **str** | Defines the account extended publicly known key which is used to derive all child public keys. | 

## Example

```python
from cryptoapis.models.derive_and_sync_new_change_addresses_rb_data_item import DeriveAndSyncNewChangeAddressesRBDataItem

# TODO update the JSON string below
json = "{}"
# create an instance of DeriveAndSyncNewChangeAddressesRBDataItem from a JSON string
derive_and_sync_new_change_addresses_rb_data_item_instance = DeriveAndSyncNewChangeAddressesRBDataItem.from_json(json)
# print the JSON string representation of the object
print DeriveAndSyncNewChangeAddressesRBDataItem.to_json()

# convert the object into a dict
derive_and_sync_new_change_addresses_rb_data_item_dict = derive_and_sync_new_change_addresses_rb_data_item_instance.to_dict()
# create an instance of DeriveAndSyncNewChangeAddressesRBDataItem from a dict
derive_and_sync_new_change_addresses_rb_data_item_form_dict = derive_and_sync_new_change_addresses_rb_data_item.from_dict(derive_and_sync_new_change_addresses_rb_data_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


