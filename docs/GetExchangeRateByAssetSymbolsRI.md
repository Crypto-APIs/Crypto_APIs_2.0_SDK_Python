# GetExchangeRateByAssetSymbolsRI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calculation_timestamp** | **int** | Defines the time of the market data used to calculate the exchange rate in UNIX Timestamp. Oldest possible timestamp is 30 days. | 
**from_asset_id** | **str** | Defines the base asset Reference ID to get a rate for. | 
**from_asset_symbol** | **str** | Defines the base asset symbol to get a rate for. | 
**rate** | **str** | Defines the exchange rate between assets calculated by weighted average of the last trades in every exchange for the last 24 hours by giving more weight to exchanges with higher volume. | 
**to_asset_id** | **str** | Defines the relation asset Reference ID in which the base asset rate will be displayed. | 
**to_asset_symbol** | **str** | Defines the relation asset symbol in which the base asset rate will be displayed. | 

## Example

```python
from cryptoapis.models.get_exchange_rate_by_asset_symbols_ri import GetExchangeRateByAssetSymbolsRI

# TODO update the JSON string below
json = "{}"
# create an instance of GetExchangeRateByAssetSymbolsRI from a JSON string
get_exchange_rate_by_asset_symbols_ri_instance = GetExchangeRateByAssetSymbolsRI.from_json(json)
# print the JSON string representation of the object
print GetExchangeRateByAssetSymbolsRI.to_json()

# convert the object into a dict
get_exchange_rate_by_asset_symbols_ri_dict = get_exchange_rate_by_asset_symbols_ri_instance.to_dict()
# create an instance of GetExchangeRateByAssetSymbolsRI from a dict
get_exchange_rate_by_asset_symbols_ri_form_dict = get_exchange_rate_by_asset_symbols_ri.from_dict(get_exchange_rate_by_asset_symbols_ri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


