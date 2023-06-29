# DeriveAndSyncNewChangeAddressesRB


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **str** | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional] 
**data** | [**DeriveAndSyncNewChangeAddressesRBData**](DeriveAndSyncNewChangeAddressesRBData.md) |  | 

## Example

```python
from cryptoapis.models.derive_and_sync_new_change_addresses_rb import DeriveAndSyncNewChangeAddressesRB

# TODO update the JSON string below
json = "{}"
# create an instance of DeriveAndSyncNewChangeAddressesRB from a JSON string
derive_and_sync_new_change_addresses_rb_instance = DeriveAndSyncNewChangeAddressesRB.from_json(json)
# print the JSON string representation of the object
print DeriveAndSyncNewChangeAddressesRB.to_json()

# convert the object into a dict
derive_and_sync_new_change_addresses_rb_dict = derive_and_sync_new_change_addresses_rb_instance.to_dict()
# create an instance of DeriveAndSyncNewChangeAddressesRB from a dict
derive_and_sync_new_change_addresses_rb_form_dict = derive_and_sync_new_change_addresses_rb.from_dict(derive_and_sync_new_change_addresses_rb_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


