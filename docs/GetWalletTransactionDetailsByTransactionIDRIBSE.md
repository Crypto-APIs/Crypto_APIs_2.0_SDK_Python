# GetWalletTransactionDetailsByTransactionIDRIBSE

Ethereum

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract** | **str** | Represents the specific transaction contract. | 
**gas_limit** | **str** | Represents the amount of gas used by this specific transaction alone. | 
**gas_price** | [**GetWalletTransactionDetailsByTransactionIDRIBSEGasPrice**](GetWalletTransactionDetailsByTransactionIDRIBSEGasPrice.md) |  | 
**gas_used** | **str** | Represents the exact unit of gas that was used for the transaction. | 
**input_data** | **str** | Represents additional information that is required for the transaction. | 
**nonce** | **int** | Represents the sequential running number for an address, starting from 0 for the first transaction. E.g., if the nonce of a transaction is 10, it would be the 11th transaction sent from the sender&#39;s address. | 
**transaction_status** | **str** | String representation of the transaction status | 

## Example

```python
from cryptoapis.models.get_wallet_transaction_details_by_transaction_idribse import GetWalletTransactionDetailsByTransactionIDRIBSE

# TODO update the JSON string below
json = "{}"
# create an instance of GetWalletTransactionDetailsByTransactionIDRIBSE from a JSON string
get_wallet_transaction_details_by_transaction_idribse_instance = GetWalletTransactionDetailsByTransactionIDRIBSE.from_json(json)
# print the JSON string representation of the object
print GetWalletTransactionDetailsByTransactionIDRIBSE.to_json()

# convert the object into a dict
get_wallet_transaction_details_by_transaction_idribse_dict = get_wallet_transaction_details_by_transaction_idribse_instance.to_dict()
# create an instance of GetWalletTransactionDetailsByTransactionIDRIBSE from a dict
get_wallet_transaction_details_by_transaction_idribse_form_dict = get_wallet_transaction_details_by_transaction_idribse.from_dict(get_wallet_transaction_details_by_transaction_idribse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


