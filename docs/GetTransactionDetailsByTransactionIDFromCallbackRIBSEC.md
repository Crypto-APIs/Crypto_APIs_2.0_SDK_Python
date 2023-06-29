# GetTransactionDetailsByTransactionIDFromCallbackRIBSEC

Ethereum Classic

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract** | **str** | Represents the specific transaction contract. | 
**gas_limit** | **str** | Represents the amount of gas used by this specific transaction alone. | 
**gas_price** | [**GetTransactionDetailsByTransactionIDRIBSECGasPrice**](GetTransactionDetailsByTransactionIDRIBSECGasPrice.md) |  | 
**gas_used** | **str** | Represents the exact unit of gas that was used for the transaction. | 
**input_data** | **str** | Represents additional information that is required for the transaction. | 
**nonce** | **int** | Represents the sequential running number for an address, starting from 0 for the first transaction. E.g., if the nonce of a transaction is 10, it would be the 11th transaction sent from the sender&#39;s address. | 

## Example

```python
from cryptoapis.models.get_transaction_details_by_transaction_id_from_callback_ribsec import GetTransactionDetailsByTransactionIDFromCallbackRIBSEC

# TODO update the JSON string below
json = "{}"
# create an instance of GetTransactionDetailsByTransactionIDFromCallbackRIBSEC from a JSON string
get_transaction_details_by_transaction_id_from_callback_ribsec_instance = GetTransactionDetailsByTransactionIDFromCallbackRIBSEC.from_json(json)
# print the JSON string representation of the object
print GetTransactionDetailsByTransactionIDFromCallbackRIBSEC.to_json()

# convert the object into a dict
get_transaction_details_by_transaction_id_from_callback_ribsec_dict = get_transaction_details_by_transaction_id_from_callback_ribsec_instance.to_dict()
# create an instance of GetTransactionDetailsByTransactionIDFromCallbackRIBSEC from a dict
get_transaction_details_by_transaction_id_from_callback_ribsec_form_dict = get_transaction_details_by_transaction_id_from_callback_ribsec.from_dict(get_transaction_details_by_transaction_id_from_callback_ribsec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


