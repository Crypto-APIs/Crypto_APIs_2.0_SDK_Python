# GetWalletAssetDetailsRI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confirmed_balance** | [**GetWalletAssetDetailsRIConfirmedBalance**](GetWalletAssetDetailsRIConfirmedBalance.md) |  | 
**deposit_addresses_count** | **int** | Specifies the count of deposit addresses in the Wallet. | 
**fungible_tokens** | [**List[GetWalletAssetDetailsRIFungibleTokensInner]**](GetWalletAssetDetailsRIFungibleTokensInner.md) | Represents fungible tokens&#39;es detailed information | 
**name** | **str** | Defines the name of the Wallet given to it by the user. | 
**non_fungible_tokens** | [**List[GetWalletAssetDetailsRINonFungibleTokensInner]**](GetWalletAssetDetailsRINonFungibleTokensInner.md) | Represents non-fungible tokens&#39;es detailed information. | 
**recieved_confirmed_amount** | [**GetWalletAssetDetailsRIRecievedConfirmedAmount**](GetWalletAssetDetailsRIRecievedConfirmedAmount.md) |  | 
**sent_confirmed_amount** | [**GetWalletAssetDetailsRISentConfirmedAmount**](GetWalletAssetDetailsRISentConfirmedAmount.md) |  | 

## Example

```python
from cryptoapis.models.get_wallet_asset_details_ri import GetWalletAssetDetailsRI

# TODO update the JSON string below
json = "{}"
# create an instance of GetWalletAssetDetailsRI from a JSON string
get_wallet_asset_details_ri_instance = GetWalletAssetDetailsRI.from_json(json)
# print the JSON string representation of the object
print GetWalletAssetDetailsRI.to_json()

# convert the object into a dict
get_wallet_asset_details_ri_dict = get_wallet_asset_details_ri_instance.to_dict()
# create an instance of GetWalletAssetDetailsRI from a dict
get_wallet_asset_details_ri_form_dict = get_wallet_asset_details_ri.from_dict(get_wallet_asset_details_ri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


