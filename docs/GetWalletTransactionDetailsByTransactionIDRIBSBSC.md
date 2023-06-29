# GetWalletTransactionDetailsByTransactionIDRIBSBSC

Binance Smart Chain

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract** | **str** | Represents the specific transaction contract | 
**gas_limit** | **str** | Represents the amount of gas used by this specific transaction alone. | 
**gas_price** | [**GetTransactionDetailsByTransactionIDRIBSBSCGasPrice**](GetTransactionDetailsByTransactionIDRIBSBSCGasPrice.md) |  | 
**gas_used** | **str** | Defines the unit of the gas price amount, e.g. BTC, ETH, XRP. | 
**input_data** | **str** | Represents additional information that is required for the transaction. | 
**nonce** | **int** | Represents the sequential running number for an address, starting from 0 for the first transaction. E.g., if the nonce of a transaction is 10, it would be the 11th transaction sent from the sender&#39;s address. | 

## Example

```python
from cryptoapis.models.get_wallet_transaction_details_by_transaction_idribsbsc import GetWalletTransactionDetailsByTransactionIDRIBSBSC

# TODO update the JSON string below
json = "{}"
# create an instance of GetWalletTransactionDetailsByTransactionIDRIBSBSC from a JSON string
get_wallet_transaction_details_by_transaction_idribsbsc_instance = GetWalletTransactionDetailsByTransactionIDRIBSBSC.from_json(json)
# print the JSON string representation of the object
print GetWalletTransactionDetailsByTransactionIDRIBSBSC.to_json()

# convert the object into a dict
get_wallet_transaction_details_by_transaction_idribsbsc_dict = get_wallet_transaction_details_by_transaction_idribsbsc_instance.to_dict()
# create an instance of GetWalletTransactionDetailsByTransactionIDRIBSBSC from a dict
get_wallet_transaction_details_by_transaction_idribsbsc_form_dict = get_wallet_transaction_details_by_transaction_idribsbsc.from_dict(get_wallet_transaction_details_by_transaction_idribsbsc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


