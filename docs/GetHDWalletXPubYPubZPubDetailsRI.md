# GetHDWalletXPubYPubZPubDetailsRI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confirmed_balance** | **str** | Specifies the confirmed coins balance of the Wallet. | 
**total_received** | **str** | Defines the total currency received to the Wallet. | [optional] 
**total_spent** | **str** | Defines the total currency spent from the Wallet. | [optional] 

## Example

```python
from cryptoapis.models.get_hd_wallet_x_pub_y_pub_z_pub_details_ri import GetHDWalletXPubYPubZPubDetailsRI

# TODO update the JSON string below
json = "{}"
# create an instance of GetHDWalletXPubYPubZPubDetailsRI from a JSON string
get_hd_wallet_x_pub_y_pub_z_pub_details_ri_instance = GetHDWalletXPubYPubZPubDetailsRI.from_json(json)
# print the JSON string representation of the object
print GetHDWalletXPubYPubZPubDetailsRI.to_json()

# convert the object into a dict
get_hd_wallet_x_pub_y_pub_z_pub_details_ri_dict = get_hd_wallet_x_pub_y_pub_z_pub_details_ri_instance.to_dict()
# create an instance of GetHDWalletXPubYPubZPubDetailsRI from a dict
get_hd_wallet_x_pub_y_pub_z_pub_details_ri_form_dict = get_hd_wallet_x_pub_y_pub_z_pub_details_ri.from_dict(get_hd_wallet_x_pub_y_pub_z_pub_details_ri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


