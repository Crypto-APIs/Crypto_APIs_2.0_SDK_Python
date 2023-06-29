# DeriveAndSyncNewReceivingAddressesRB


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **str** | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional] 
**data** | [**DeriveAndSyncNewReceivingAddressesRBData**](DeriveAndSyncNewReceivingAddressesRBData.md) |  | 

## Example

```python
from cryptoapis.models.derive_and_sync_new_receiving_addresses_rb import DeriveAndSyncNewReceivingAddressesRB

# TODO update the JSON string below
json = "{}"
# create an instance of DeriveAndSyncNewReceivingAddressesRB from a JSON string
derive_and_sync_new_receiving_addresses_rb_instance = DeriveAndSyncNewReceivingAddressesRB.from_json(json)
# print the JSON string representation of the object
print DeriveAndSyncNewReceivingAddressesRB.to_json()

# convert the object into a dict
derive_and_sync_new_receiving_addresses_rb_dict = derive_and_sync_new_receiving_addresses_rb_instance.to_dict()
# create an instance of DeriveAndSyncNewReceivingAddressesRB from a dict
derive_and_sync_new_receiving_addresses_rb_form_dict = derive_and_sync_new_receiving_addresses_rb.from_dict(derive_and_sync_new_receiving_addresses_rb_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


