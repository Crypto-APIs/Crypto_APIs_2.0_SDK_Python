# SyncNewHDWalletXPubYPubZPubRB


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **str** | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional] 
**data** | [**SyncHDWalletXPubYPubZPubRBData**](SyncHDWalletXPubYPubZPubRBData.md) |  | 

## Example

```python
from cryptoapis.models.sync_new_hd_wallet_x_pub_y_pub_z_pub_rb import SyncNewHDWalletXPubYPubZPubRB

# TODO update the JSON string below
json = "{}"
# create an instance of SyncNewHDWalletXPubYPubZPubRB from a JSON string
sync_new_hd_wallet_x_pub_y_pub_z_pub_rb_instance = SyncNewHDWalletXPubYPubZPubRB.from_json(json)
# print the JSON string representation of the object
print SyncNewHDWalletXPubYPubZPubRB.to_json()

# convert the object into a dict
sync_new_hd_wallet_x_pub_y_pub_z_pub_rb_dict = sync_new_hd_wallet_x_pub_y_pub_z_pub_rb_instance.to_dict()
# create an instance of SyncNewHDWalletXPubYPubZPubRB from a dict
sync_new_hd_wallet_x_pub_y_pub_z_pub_rb_form_dict = sync_new_hd_wallet_x_pub_y_pub_z_pub_rb.from_dict(sync_new_hd_wallet_x_pub_y_pub_z_pub_rb_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


