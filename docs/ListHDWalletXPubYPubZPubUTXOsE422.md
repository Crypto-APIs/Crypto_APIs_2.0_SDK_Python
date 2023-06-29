# ListHDWalletXPubYPubZPubUTXOsE422


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Specifies an error code, e.g. error 404. | 
**message** | **str** | Specifies the message of the error, i.e. why the error was returned, e.g. error 404 stands for “not found”. | 
**details** | [**List[BannedIpAddressDetailsInner]**](BannedIpAddressDetailsInner.md) |  | [optional] 

## Example

```python
from cryptoapis.models.list_hd_wallet_x_pub_y_pub_z_pub_utxos_e422 import ListHDWalletXPubYPubZPubUTXOsE422

# TODO update the JSON string below
json = "{}"
# create an instance of ListHDWalletXPubYPubZPubUTXOsE422 from a JSON string
list_hd_wallet_x_pub_y_pub_z_pub_utxos_e422_instance = ListHDWalletXPubYPubZPubUTXOsE422.from_json(json)
# print the JSON string representation of the object
print ListHDWalletXPubYPubZPubUTXOsE422.to_json()

# convert the object into a dict
list_hd_wallet_x_pub_y_pub_z_pub_utxos_e422_dict = list_hd_wallet_x_pub_y_pub_z_pub_utxos_e422_instance.to_dict()
# create an instance of ListHDWalletXPubYPubZPubUTXOsE422 from a dict
list_hd_wallet_x_pub_y_pub_z_pub_utxos_e422_form_dict = list_hd_wallet_x_pub_y_pub_z_pub_utxos_e422.from_dict(list_hd_wallet_x_pub_y_pub_z_pub_utxos_e422_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


