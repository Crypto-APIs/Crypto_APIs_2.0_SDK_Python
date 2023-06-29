# GetTransactionDetailsByTransactionIDFromCallbackRIBST

Tron

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Defines the amount of the transaction. | 
**bandwidth_used** | [**GetTransactionDetailsByTransactionIDFromCallbackRIBSTBandwidthUsed**](GetTransactionDetailsByTransactionIDFromCallbackRIBSTBandwidthUsed.md) |  | 
**contract** | **str** | Represents the specific transaction contract. | 
**energy_used** | [**GetTransactionDetailsByTransactionIDFromCallbackRIBSTEnergyUsed**](GetTransactionDetailsByTransactionIDFromCallbackRIBSTEnergyUsed.md) |  | 
**has_internal_transactions** | **bool** | Defines if the transaction includes internal transactions (true) or not (false). | 
**has_token_transfers** | **str** | Defines if the transaction includes token transfers (true) or not (false). | 
**input** | **str** | Represents the transaction&#39;s input value. | 
**recipients** | **str** | Represents the recipient address. | 
**senders** | **str** | Represents the sender address. | 
**transaction_status** | **str** | Represents the status of this transaction. | 

## Example

```python
from cryptoapis.models.get_transaction_details_by_transaction_id_from_callback_ribst import GetTransactionDetailsByTransactionIDFromCallbackRIBST

# TODO update the JSON string below
json = "{}"
# create an instance of GetTransactionDetailsByTransactionIDFromCallbackRIBST from a JSON string
get_transaction_details_by_transaction_id_from_callback_ribst_instance = GetTransactionDetailsByTransactionIDFromCallbackRIBST.from_json(json)
# print the JSON string representation of the object
print GetTransactionDetailsByTransactionIDFromCallbackRIBST.to_json()

# convert the object into a dict
get_transaction_details_by_transaction_id_from_callback_ribst_dict = get_transaction_details_by_transaction_id_from_callback_ribst_instance.to_dict()
# create an instance of GetTransactionDetailsByTransactionIDFromCallbackRIBST from a dict
get_transaction_details_by_transaction_id_from_callback_ribst_form_dict = get_transaction_details_by_transaction_id_from_callback_ribst.from_dict(get_transaction_details_by_transaction_id_from_callback_ribst_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


