# ListHDWalletXPubYPubZPubUTXOsRData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | Defines how many items should be returned in the response per page basis. | 
**offset** | **int** | The starting index of the response items, i.e. where the response should start listing the returned items. | 
**total** | **int** | Defines the total number of items returned in the response. | 
**items** | [**List[ListHDWalletXPubYPubZPubUTXOsRI]**](ListHDWalletXPubYPubZPubUTXOsRI.md) |  | 

## Example

```python
from cryptoapis.models.list_hd_wallet_x_pub_y_pub_z_pub_utxos_r_data import ListHDWalletXPubYPubZPubUTXOsRData

# TODO update the JSON string below
json = "{}"
# create an instance of ListHDWalletXPubYPubZPubUTXOsRData from a JSON string
list_hd_wallet_x_pub_y_pub_z_pub_utxos_r_data_instance = ListHDWalletXPubYPubZPubUTXOsRData.from_json(json)
# print the JSON string representation of the object
print ListHDWalletXPubYPubZPubUTXOsRData.to_json()

# convert the object into a dict
list_hd_wallet_x_pub_y_pub_z_pub_utxos_r_data_dict = list_hd_wallet_x_pub_y_pub_z_pub_utxos_r_data_instance.to_dict()
# create an instance of ListHDWalletXPubYPubZPubUTXOsRData from a dict
list_hd_wallet_x_pub_y_pub_z_pub_utxos_r_data_form_dict = list_hd_wallet_x_pub_y_pub_z_pub_utxos_r_data.from_dict(list_hd_wallet_x_pub_y_pub_z_pub_utxos_r_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


