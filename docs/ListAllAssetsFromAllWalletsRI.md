# ListAllAssetsFromAllWalletsRI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coins** | [**List[ListAllAssetsFromAllWalletsRICoinsInner]**](ListAllAssetsFromAllWalletsRICoinsInner.md) |  | 
**fungible_tokens** | [**List[ListAllAssetsFromAllWalletsRIFungibleTokensInner]**](ListAllAssetsFromAllWalletsRIFungibleTokensInner.md) | Represents fungible tokens&#39;es detailed information | 
**non_fungible_tokens** | [**List[ListAllAssetsFromAllWalletsRINonFungibleTokensInner]**](ListAllAssetsFromAllWalletsRINonFungibleTokensInner.md) | Represents non-fungible tokens&#39;es detailed information. | 
**wallet_id** | **str** | Defines the unique ID of the Wallet. | 
**wallet_name** | **str** | Represents the name of the wallet. | 

## Example

```python
from cryptoapis.models.list_all_assets_from_all_wallets_ri import ListAllAssetsFromAllWalletsRI

# TODO update the JSON string below
json = "{}"
# create an instance of ListAllAssetsFromAllWalletsRI from a JSON string
list_all_assets_from_all_wallets_ri_instance = ListAllAssetsFromAllWalletsRI.from_json(json)
# print the JSON string representation of the object
print ListAllAssetsFromAllWalletsRI.to_json()

# convert the object into a dict
list_all_assets_from_all_wallets_ri_dict = list_all_assets_from_all_wallets_ri_instance.to_dict()
# create an instance of ListAllAssetsFromAllWalletsRI from a dict
list_all_assets_from_all_wallets_ri_form_dict = list_all_assets_from_all_wallets_ri.from_dict(list_all_assets_from_all_wallets_ri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


