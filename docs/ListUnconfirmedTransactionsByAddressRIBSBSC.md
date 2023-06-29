# ListUnconfirmedTransactionsByAddressRIBSBSC

Binance Smart Chain

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gas_limit** | **str** | Represents the amount of gas used by this specific transaction alone. | 
**gas_price** | [**ListConfirmedTransactionsByAddressRIBSBSCGasPrice**](ListConfirmedTransactionsByAddressRIBSBSCGasPrice.md) |  | 
**input_data** | **str** | Represents additional information that is required for the transaction. | 
**nonce** | **int** | Represents the sequential running number for an address, starting from 0 for the first transaction. E.g., if the nonce of a transaction is 10, it would be the 11th transaction sent from the sender&#39;s address. | 
**transaction_status** | **str** | String representation of the transaction status | 

## Example

```python
from cryptoapis.models.list_unconfirmed_transactions_by_address_ribsbsc import ListUnconfirmedTransactionsByAddressRIBSBSC

# TODO update the JSON string below
json = "{}"
# create an instance of ListUnconfirmedTransactionsByAddressRIBSBSC from a JSON string
list_unconfirmed_transactions_by_address_ribsbsc_instance = ListUnconfirmedTransactionsByAddressRIBSBSC.from_json(json)
# print the JSON string representation of the object
print ListUnconfirmedTransactionsByAddressRIBSBSC.to_json()

# convert the object into a dict
list_unconfirmed_transactions_by_address_ribsbsc_dict = list_unconfirmed_transactions_by_address_ribsbsc_instance.to_dict()
# create an instance of ListUnconfirmedTransactionsByAddressRIBSBSC from a dict
list_unconfirmed_transactions_by_address_ribsbsc_form_dict = list_unconfirmed_transactions_by_address_ribsbsc.from_dict(list_unconfirmed_transactions_by_address_ribsbsc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


