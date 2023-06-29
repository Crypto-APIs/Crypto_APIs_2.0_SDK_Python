# ListTransactionsByBlockHeightRIBSBSC

Binance Smart Chain

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract** | **str** | Represents the specific transaction contract. | [optional] 
**gas_limit** | **str** | Represents the amount of gas used by this specific transaction alone. | 
**gas_price** | [**ListTransactionsByBlockHeightRIBSBSCGasPrice**](ListTransactionsByBlockHeightRIBSBSCGasPrice.md) |  | 
**gas_used** | **str** | Represents the exact unit of gas that was used for the transaction. | 
**input_data** | **str** | Represents additional information that is required for the transaction. | 
**nonce** | **int** | Represents the sequential running number for an address, starting from 0 for the first transaction. E.g., if the nonce of a transaction is 10, it would be the 11th transaction sent from the sender&#39;s address. | 
**transaction_status** | **str** | Represents the status of this transaction | 

## Example

```python
from cryptoapis.models.list_transactions_by_block_height_ribsbsc import ListTransactionsByBlockHeightRIBSBSC

# TODO update the JSON string below
json = "{}"
# create an instance of ListTransactionsByBlockHeightRIBSBSC from a JSON string
list_transactions_by_block_height_ribsbsc_instance = ListTransactionsByBlockHeightRIBSBSC.from_json(json)
# print the JSON string representation of the object
print ListTransactionsByBlockHeightRIBSBSC.to_json()

# convert the object into a dict
list_transactions_by_block_height_ribsbsc_dict = list_transactions_by_block_height_ribsbsc_instance.to_dict()
# create an instance of ListTransactionsByBlockHeightRIBSBSC from a dict
list_transactions_by_block_height_ribsbsc_form_dict = list_transactions_by_block_height_ribsbsc.from_dict(list_transactions_by_block_height_ribsbsc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


