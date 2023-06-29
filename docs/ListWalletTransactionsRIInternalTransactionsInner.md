# ListWalletTransactionsRIInternalTransactionsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Defines the specific amount of the transaction. | 
**converted_amount** | **str** | Represents the converted amount. | 
**exchange_rate_unit** | **str** | Defines the base asset symbol to get a rate for. | 
**operation_id** | **str** | Represents the unique internal transaction ID in regards to the parent transaction (type trace address). | 
**recipient** | **str** | Represents the recipient address with the respective amount. | 
**sender** | **str** | Represents the sender address with the respective amount. | 
**symbol** | **str** | Represents the unique unit symbol. | 

## Example

```python
from cryptoapis.models.list_wallet_transactions_ri_internal_transactions_inner import ListWalletTransactionsRIInternalTransactionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListWalletTransactionsRIInternalTransactionsInner from a JSON string
list_wallet_transactions_ri_internal_transactions_inner_instance = ListWalletTransactionsRIInternalTransactionsInner.from_json(json)
# print the JSON string representation of the object
print ListWalletTransactionsRIInternalTransactionsInner.to_json()

# convert the object into a dict
list_wallet_transactions_ri_internal_transactions_inner_dict = list_wallet_transactions_ri_internal_transactions_inner_instance.to_dict()
# create an instance of ListWalletTransactionsRIInternalTransactionsInner from a dict
list_wallet_transactions_ri_internal_transactions_inner_form_dict = list_wallet_transactions_ri_internal_transactions_inner.from_dict(list_wallet_transactions_ri_internal_transactions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


