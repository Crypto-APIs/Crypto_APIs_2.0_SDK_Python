# GetExchangeRateByAssetSymbolsE400


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Specifies an error code, e.g. error 404. | 
**message** | **str** | Specifies the message of the error, i.e. why the error was returned, e.g. error 404 stands for “not found”. | 
**details** | [**List[BannedIpAddressDetailsInner]**](BannedIpAddressDetailsInner.md) |  | [optional] 

## Example

```python
from cryptoapis.models.get_exchange_rate_by_asset_symbols_e400 import GetExchangeRateByAssetSymbolsE400

# TODO update the JSON string below
json = "{}"
# create an instance of GetExchangeRateByAssetSymbolsE400 from a JSON string
get_exchange_rate_by_asset_symbols_e400_instance = GetExchangeRateByAssetSymbolsE400.from_json(json)
# print the JSON string representation of the object
print GetExchangeRateByAssetSymbolsE400.to_json()

# convert the object into a dict
get_exchange_rate_by_asset_symbols_e400_dict = get_exchange_rate_by_asset_symbols_e400_instance.to_dict()
# create an instance of GetExchangeRateByAssetSymbolsE400 from a dict
get_exchange_rate_by_asset_symbols_e400_form_dict = get_exchange_rate_by_asset_symbols_e400.from_dict(get_exchange_rate_by_asset_symbols_e400_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


