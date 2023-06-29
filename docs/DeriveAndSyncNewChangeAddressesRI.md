# DeriveAndSyncNewChangeAddressesRI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Represents the public address, which is a compressed and shortened form of a public key. | 
**address_format** | **str** | Represents the format of the address. | 
**address_type** | **str** | Defines the address type. | 
**derivation_type** | **str** | Represents the derivation type. | 
**index** | **str** | Represents the output index. It refers to the UTXO sequence in the transaction outputs (vout). | 

## Example

```python
from cryptoapis.models.derive_and_sync_new_change_addresses_ri import DeriveAndSyncNewChangeAddressesRI

# TODO update the JSON string below
json = "{}"
# create an instance of DeriveAndSyncNewChangeAddressesRI from a JSON string
derive_and_sync_new_change_addresses_ri_instance = DeriveAndSyncNewChangeAddressesRI.from_json(json)
# print the JSON string representation of the object
print DeriveAndSyncNewChangeAddressesRI.to_json()

# convert the object into a dict
derive_and_sync_new_change_addresses_ri_dict = derive_and_sync_new_change_addresses_ri_instance.to_dict()
# create an instance of DeriveAndSyncNewChangeAddressesRI from a dict
derive_and_sync_new_change_addresses_ri_form_dict = derive_and_sync_new_change_addresses_ri.from_dict(derive_and_sync_new_change_addresses_ri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


