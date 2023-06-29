# ListWalletTransactionsRIFee


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Defines the fee for the transaction. | 
**converted_amount** | **str** | Defines the converted amount of the transaction&#39;s fee. | 
**exchange_rate_unit** | **str** | Defines the exchange rate for the transaction&#39;s unit. | 
**symbol** | **str** | Defines the unit of the transaction&#39;s fee. | 

## Example

```python
from cryptoapis.models.list_wallet_transactions_ri_fee import ListWalletTransactionsRIFee

# TODO update the JSON string below
json = "{}"
# create an instance of ListWalletTransactionsRIFee from a JSON string
list_wallet_transactions_ri_fee_instance = ListWalletTransactionsRIFee.from_json(json)
# print the JSON string representation of the object
print ListWalletTransactionsRIFee.to_json()

# convert the object into a dict
list_wallet_transactions_ri_fee_dict = list_wallet_transactions_ri_fee_instance.to_dict()
# create an instance of ListWalletTransactionsRIFee from a dict
list_wallet_transactions_ri_fee_form_dict = list_wallet_transactions_ri_fee.from_dict(list_wallet_transactions_ri_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


