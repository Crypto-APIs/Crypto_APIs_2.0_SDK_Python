# ListAllAssetsFromAllWalletsRICoinsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blockchain** | **str** | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. | 
**confirmed_balance** | **str** | Defines the total balance of the address that is confirmed. It doesn&#39;t include unconfirmed transactions. | 
**network** | **str** | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;goerli\&quot; are test networks. | 
**total_received** | **str** | Defines the total amount of all coins received to the address, based on confirmed transactions. | 
**total_spent** | **str** | Defines the total amount of all spent by this address coins, based on confirmed transactions. | 
**unit** | **str** | Represents the unit of the confirmed balance. | 

## Example

```python
from cryptoapis.models.list_all_assets_from_all_wallets_ri_coins_inner import ListAllAssetsFromAllWalletsRICoinsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListAllAssetsFromAllWalletsRICoinsInner from a JSON string
list_all_assets_from_all_wallets_ri_coins_inner_instance = ListAllAssetsFromAllWalletsRICoinsInner.from_json(json)
# print the JSON string representation of the object
print ListAllAssetsFromAllWalletsRICoinsInner.to_json()

# convert the object into a dict
list_all_assets_from_all_wallets_ri_coins_inner_dict = list_all_assets_from_all_wallets_ri_coins_inner_instance.to_dict()
# create an instance of ListAllAssetsFromAllWalletsRICoinsInner from a dict
list_all_assets_from_all_wallets_ri_coins_inner_form_dict = list_all_assets_from_all_wallets_ri_coins_inner.from_dict(list_all_assets_from_all_wallets_ri_coins_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


