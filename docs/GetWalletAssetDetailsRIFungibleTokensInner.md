# GetWalletAssetDetailsRIFungibleTokensInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confirmed_amount** | **str** | Defines the amount of the fungible tokens. | 
**identifier** | **str** | Defines the specific token identifier. For Bitcoin-based transactions it should be the propertyId and for Ethereum-based transactions - the contract. | 
**symbol** | **str** | Defines the symbol of the fungible tokens. | 
**type** | **str** | Defines the specific token type. | 

## Example

```python
from cryptoapis.models.get_wallet_asset_details_ri_fungible_tokens_inner import GetWalletAssetDetailsRIFungibleTokensInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetWalletAssetDetailsRIFungibleTokensInner from a JSON string
get_wallet_asset_details_ri_fungible_tokens_inner_instance = GetWalletAssetDetailsRIFungibleTokensInner.from_json(json)
# print the JSON string representation of the object
print GetWalletAssetDetailsRIFungibleTokensInner.to_json()

# convert the object into a dict
get_wallet_asset_details_ri_fungible_tokens_inner_dict = get_wallet_asset_details_ri_fungible_tokens_inner_instance.to_dict()
# create an instance of GetWalletAssetDetailsRIFungibleTokensInner from a dict
get_wallet_asset_details_ri_fungible_tokens_inner_form_dict = get_wallet_asset_details_ri_fungible_tokens_inner.from_dict(get_wallet_asset_details_ri_fungible_tokens_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


