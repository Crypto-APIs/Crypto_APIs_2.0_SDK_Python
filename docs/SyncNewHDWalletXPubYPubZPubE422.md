# SyncNewHDWalletXPubYPubZPubE422


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Specifies an error code, e.g. error 404. | 
**message** | **str** | Specifies the message of the error, i.e. why the error was returned, e.g. error 404 stands for “not found”. | 
**details** | [**List[BannedIpAddressDetailsInner]**](BannedIpAddressDetailsInner.md) |  | [optional] 

## Example

```python
from cryptoapis.models.sync_new_hd_wallet_x_pub_y_pub_z_pub_e422 import SyncNewHDWalletXPubYPubZPubE422

# TODO update the JSON string below
json = "{}"
# create an instance of SyncNewHDWalletXPubYPubZPubE422 from a JSON string
sync_new_hd_wallet_x_pub_y_pub_z_pub_e422_instance = SyncNewHDWalletXPubYPubZPubE422.from_json(json)
# print the JSON string representation of the object
print SyncNewHDWalletXPubYPubZPubE422.to_json()

# convert the object into a dict
sync_new_hd_wallet_x_pub_y_pub_z_pub_e422_dict = sync_new_hd_wallet_x_pub_y_pub_z_pub_e422_instance.to_dict()
# create an instance of SyncNewHDWalletXPubYPubZPubE422 from a dict
sync_new_hd_wallet_x_pub_y_pub_z_pub_e422_form_dict = sync_new_hd_wallet_x_pub_y_pub_z_pub_e422.from_dict(sync_new_hd_wallet_x_pub_y_pub_z_pub_e422_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


