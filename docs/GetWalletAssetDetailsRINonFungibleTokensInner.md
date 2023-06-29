# GetWalletAssetDetailsRINonFungibleTokensInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Defines the specific token identifier. For Bitcoin-based transactions it should be the propertyId and for Ethereum-based transactions - the contract. | 
**symbol** | **str** | Defines the symbol of the non-fungible tokens. | 
**token_id** | **str** | Represents tokens&#39; unique identifier. | 
**type** | **str** | Defines the specific token type. | 

## Example

```python
from cryptoapis.models.get_wallet_asset_details_ri_non_fungible_tokens_inner import GetWalletAssetDetailsRINonFungibleTokensInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetWalletAssetDetailsRINonFungibleTokensInner from a JSON string
get_wallet_asset_details_ri_non_fungible_tokens_inner_instance = GetWalletAssetDetailsRINonFungibleTokensInner.from_json(json)
# print the JSON string representation of the object
print GetWalletAssetDetailsRINonFungibleTokensInner.to_json()

# convert the object into a dict
get_wallet_asset_details_ri_non_fungible_tokens_inner_dict = get_wallet_asset_details_ri_non_fungible_tokens_inner_instance.to_dict()
# create an instance of GetWalletAssetDetailsRINonFungibleTokensInner from a dict
get_wallet_asset_details_ri_non_fungible_tokens_inner_form_dict = get_wallet_asset_details_ri_non_fungible_tokens_inner.from_dict(get_wallet_asset_details_ri_non_fungible_tokens_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


