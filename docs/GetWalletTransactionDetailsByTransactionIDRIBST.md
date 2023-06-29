# GetWalletTransactionDetailsByTransactionIDRIBST

Tron

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | String representation of the amount value | 
**bandwidth_used** | **str** | Numeric representation of the transaction used bandwidth | 
**contract** | **str** | Numeric representation of the transaction contract | 
**energy_used** | **str** | String representation of the transaction used energy | 
**has_internal_transactions** | **bool** |  | 
**has_token_transfers** | **bool** |  | 
**input** | **str** | Numeric representation of the transaction input | 
**status** | **str** | String representation of the transaction status | 

## Example

```python
from cryptoapis.models.get_wallet_transaction_details_by_transaction_idribst import GetWalletTransactionDetailsByTransactionIDRIBST

# TODO update the JSON string below
json = "{}"
# create an instance of GetWalletTransactionDetailsByTransactionIDRIBST from a JSON string
get_wallet_transaction_details_by_transaction_idribst_instance = GetWalletTransactionDetailsByTransactionIDRIBST.from_json(json)
# print the JSON string representation of the object
print GetWalletTransactionDetailsByTransactionIDRIBST.to_json()

# convert the object into a dict
get_wallet_transaction_details_by_transaction_idribst_dict = get_wallet_transaction_details_by_transaction_idribst_instance.to_dict()
# create an instance of GetWalletTransactionDetailsByTransactionIDRIBST from a dict
get_wallet_transaction_details_by_transaction_idribst_form_dict = get_wallet_transaction_details_by_transaction_idribst.from_dict(get_wallet_transaction_details_by_transaction_idribst_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


