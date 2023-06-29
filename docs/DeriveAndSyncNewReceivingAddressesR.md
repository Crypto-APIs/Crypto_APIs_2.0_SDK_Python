# DeriveAndSyncNewReceivingAddressesR


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | Specifies the version of the API that incorporates this endpoint. | 
**request_id** | **str** | Defines the ID of the request. The &#x60;requestId&#x60; is generated by Crypto APIs and it&#39;s unique for every request. | 
**context** | **str** | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional] 
**data** | [**DeriveAndSyncNewReceivingAddressesRData**](DeriveAndSyncNewReceivingAddressesRData.md) |  | 

## Example

```python
from cryptoapis.models.derive_and_sync_new_receiving_addresses_r import DeriveAndSyncNewReceivingAddressesR

# TODO update the JSON string below
json = "{}"
# create an instance of DeriveAndSyncNewReceivingAddressesR from a JSON string
derive_and_sync_new_receiving_addresses_r_instance = DeriveAndSyncNewReceivingAddressesR.from_json(json)
# print the JSON string representation of the object
print DeriveAndSyncNewReceivingAddressesR.to_json()

# convert the object into a dict
derive_and_sync_new_receiving_addresses_r_dict = derive_and_sync_new_receiving_addresses_r_instance.to_dict()
# create an instance of DeriveAndSyncNewReceivingAddressesR from a dict
derive_and_sync_new_receiving_addresses_r_form_dict = derive_and_sync_new_receiving_addresses_r.from_dict(derive_and_sync_new_receiving_addresses_r_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

