# SyncHDWalletXPubYPubZPubRB


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **str** | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional] 
**data** | [**SyncHDWalletXPubYPubZPubRBData**](SyncHDWalletXPubYPubZPubRBData.md) |  | 

## Example

```python
from cryptoapis.models.sync_hd_wallet_x_pub_y_pub_z_pub_rb import SyncHDWalletXPubYPubZPubRB

# TODO update the JSON string below
json = "{}"
# create an instance of SyncHDWalletXPubYPubZPubRB from a JSON string
sync_hd_wallet_x_pub_y_pub_z_pub_rb_instance = SyncHDWalletXPubYPubZPubRB.from_json(json)
# print the JSON string representation of the object
print SyncHDWalletXPubYPubZPubRB.to_json()

# convert the object into a dict
sync_hd_wallet_x_pub_y_pub_z_pub_rb_dict = sync_hd_wallet_x_pub_y_pub_z_pub_rb_instance.to_dict()
# create an instance of SyncHDWalletXPubYPubZPubRB from a dict
sync_hd_wallet_x_pub_y_pub_z_pub_rb_form_dict = sync_hd_wallet_x_pub_y_pub_z_pub_rb.from_dict(sync_hd_wallet_x_pub_y_pub_z_pub_rb_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


