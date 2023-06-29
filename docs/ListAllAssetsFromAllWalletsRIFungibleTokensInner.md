# ListAllAssetsFromAllWalletsRIFungibleTokensInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Defines the amount of the fungible tokens. | 
**blockchain** | **str** | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. | 
**identifier** | **str** | Defines the specific token identifier. For Bitcoin-based transactions it should be the propertyId and for Ethereum-based transactions - the contract. | 
**network** | **str** | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;goerli\&quot; are test networks. | 
**symbol** | **str** | Defines the symbol of the fungible tokens. | 
**type** | **str** | Defines the specific token type. | 

## Example

```python
from cryptoapis.models.list_all_assets_from_all_wallets_ri_fungible_tokens_inner import ListAllAssetsFromAllWalletsRIFungibleTokensInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListAllAssetsFromAllWalletsRIFungibleTokensInner from a JSON string
list_all_assets_from_all_wallets_ri_fungible_tokens_inner_instance = ListAllAssetsFromAllWalletsRIFungibleTokensInner.from_json(json)
# print the JSON string representation of the object
print ListAllAssetsFromAllWalletsRIFungibleTokensInner.to_json()

# convert the object into a dict
list_all_assets_from_all_wallets_ri_fungible_tokens_inner_dict = list_all_assets_from_all_wallets_ri_fungible_tokens_inner_instance.to_dict()
# create an instance of ListAllAssetsFromAllWalletsRIFungibleTokensInner from a dict
list_all_assets_from_all_wallets_ri_fungible_tokens_inner_form_dict = list_all_assets_from_all_wallets_ri_fungible_tokens_inner.from_dict(list_all_assets_from_all_wallets_ri_fungible_tokens_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


