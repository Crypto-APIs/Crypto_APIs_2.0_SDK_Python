# DeriveAndSyncNewChangeAddressesRData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | Defines how many items should be returned in the response per page basis. | 
**offset** | **int** | The starting index of the response items, i.e. where the response should start listing the returned items. | 
**total** | **int** | Defines the total number of items returned in the response. | 
**items** | [**List[DeriveAndSyncNewChangeAddressesRI]**](DeriveAndSyncNewChangeAddressesRI.md) |  | 

## Example

```python
from cryptoapis.models.derive_and_sync_new_change_addresses_r_data import DeriveAndSyncNewChangeAddressesRData

# TODO update the JSON string below
json = "{}"
# create an instance of DeriveAndSyncNewChangeAddressesRData from a JSON string
derive_and_sync_new_change_addresses_r_data_instance = DeriveAndSyncNewChangeAddressesRData.from_json(json)
# print the JSON string representation of the object
print DeriveAndSyncNewChangeAddressesRData.to_json()

# convert the object into a dict
derive_and_sync_new_change_addresses_r_data_dict = derive_and_sync_new_change_addresses_r_data_instance.to_dict()
# create an instance of DeriveAndSyncNewChangeAddressesRData from a dict
derive_and_sync_new_change_addresses_r_data_form_dict = derive_and_sync_new_change_addresses_r_data.from_dict(derive_and_sync_new_change_addresses_r_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


