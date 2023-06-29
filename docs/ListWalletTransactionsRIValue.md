# ListWalletTransactionsRIValue


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Defines the transaction amount. | 
**converted_amount** | **str** | Defines the converted amount of the transaction as a string. | 
**exchange_rate_unit** | **str** | Defines the exchange rate&#39;s unit. | 
**symbol** | **str** | Defines the unit of the transaction&#39;s amount. | 

## Example

```python
from cryptoapis.models.list_wallet_transactions_ri_value import ListWalletTransactionsRIValue

# TODO update the JSON string below
json = "{}"
# create an instance of ListWalletTransactionsRIValue from a JSON string
list_wallet_transactions_ri_value_instance = ListWalletTransactionsRIValue.from_json(json)
# print the JSON string representation of the object
print ListWalletTransactionsRIValue.to_json()

# convert the object into a dict
list_wallet_transactions_ri_value_dict = list_wallet_transactions_ri_value_instance.to_dict()
# create an instance of ListWalletTransactionsRIValue from a dict
list_wallet_transactions_ri_value_form_dict = list_wallet_transactions_ri_value.from_dict(list_wallet_transactions_ri_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


