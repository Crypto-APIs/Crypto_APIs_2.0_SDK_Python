# GetWalletAssetDetailsRIConfirmedBalance

Specifies the confirmed balance.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Specifies the amount of the confirmed balance. | 
**unit** | **str** | Specifies the unit of the amount of the confirmed balance. | 

## Example

```python
from cryptoapis.models.get_wallet_asset_details_ri_confirmed_balance import GetWalletAssetDetailsRIConfirmedBalance

# TODO update the JSON string below
json = "{}"
# create an instance of GetWalletAssetDetailsRIConfirmedBalance from a JSON string
get_wallet_asset_details_ri_confirmed_balance_instance = GetWalletAssetDetailsRIConfirmedBalance.from_json(json)
# print the JSON string representation of the object
print GetWalletAssetDetailsRIConfirmedBalance.to_json()

# convert the object into a dict
get_wallet_asset_details_ri_confirmed_balance_dict = get_wallet_asset_details_ri_confirmed_balance_instance.to_dict()
# create an instance of GetWalletAssetDetailsRIConfirmedBalance from a dict
get_wallet_asset_details_ri_confirmed_balance_form_dict = get_wallet_asset_details_ri_confirmed_balance.from_dict(get_wallet_asset_details_ri_confirmed_balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


