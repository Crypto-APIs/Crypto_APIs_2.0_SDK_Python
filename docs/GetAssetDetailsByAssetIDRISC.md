# GetAssetDetailsByAssetIDRISC

Crypto Type Data

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_1_hour_price_change_in_percentage** | **str** | Represents the percentage of the asset&#39;s current price against the its price from 1 hour ago. | 
**var_1_week_price_change_in_percentage** | **str** | Represents the percentage of the asset&#39;s current price against the its price from 1 week ago. | 
**var_24_hours_price_change_in_percentage** | **str** | Represents the percentage of the asset&#39;s current price against the its price from 24 hours ago. | 
**var_24_hours_trading_volume** | **str** | Represents the trading volume of the asset for the time frame of 24 hours. | 
**asset_type** | **str** | Represent a subtype of the crypto assets. Could be COIN or TOKEN. | 
**circulating_supply** | **str** | Represents the amount of the asset that is circulating on the market and in public hands. | 
**market_cap_in_usd** | **str** | Defines the total market value of the asset&#39;s circulating supply in USD. | 
**max_supply** | **str** | Represents the maximum amount of all coins of a specific asset that will ever exist in its lifetime. | 

## Example

```python
from cryptoapis.models.get_asset_details_by_asset_idrisc import GetAssetDetailsByAssetIDRISC

# TODO update the JSON string below
json = "{}"
# create an instance of GetAssetDetailsByAssetIDRISC from a JSON string
get_asset_details_by_asset_idrisc_instance = GetAssetDetailsByAssetIDRISC.from_json(json)
# print the JSON string representation of the object
print GetAssetDetailsByAssetIDRISC.to_json()

# convert the object into a dict
get_asset_details_by_asset_idrisc_dict = get_asset_details_by_asset_idrisc_instance.to_dict()
# create an instance of GetAssetDetailsByAssetIDRISC from a dict
get_asset_details_by_asset_idrisc_form_dict = get_asset_details_by_asset_idrisc.from_dict(get_asset_details_by_asset_idrisc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


