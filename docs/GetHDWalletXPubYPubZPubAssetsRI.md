# GetHDWalletXPubYPubZPubAssetsRI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fungible_tokens** | [**List[GetHDWalletXPubYPubZPubAssetsRIFungibleTokensInner]**](GetHDWalletXPubYPubZPubAssetsRIFungibleTokensInner.md) | Represents fungible tokens&#39;es detailed information | [optional] 
**non_fungible_tokens** | [**List[GetHDWalletXPubYPubZPubAssetsRINonFungibleTokensInner]**](GetHDWalletXPubYPubZPubAssetsRINonFungibleTokensInner.md) | Represents non-fungible tokens&#39;es detailed information. | [optional] 
**confirmed_balance** | [**GetHDWalletXPubYPubZPubAssetsRIConfirmedBalance**](GetHDWalletXPubYPubZPubAssetsRIConfirmedBalance.md) |  | 

## Example

```python
from cryptoapis.models.get_hd_wallet_x_pub_y_pub_z_pub_assets_ri import GetHDWalletXPubYPubZPubAssetsRI

# TODO update the JSON string below
json = "{}"
# create an instance of GetHDWalletXPubYPubZPubAssetsRI from a JSON string
get_hd_wallet_x_pub_y_pub_z_pub_assets_ri_instance = GetHDWalletXPubYPubZPubAssetsRI.from_json(json)
# print the JSON string representation of the object
print GetHDWalletXPubYPubZPubAssetsRI.to_json()

# convert the object into a dict
get_hd_wallet_x_pub_y_pub_z_pub_assets_ri_dict = get_hd_wallet_x_pub_y_pub_z_pub_assets_ri_instance.to_dict()
# create an instance of GetHDWalletXPubYPubZPubAssetsRI from a dict
get_hd_wallet_x_pub_y_pub_z_pub_assets_ri_form_dict = get_hd_wallet_x_pub_y_pub_z_pub_assets_ri.from_dict(get_hd_wallet_x_pub_y_pub_z_pub_assets_ri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


