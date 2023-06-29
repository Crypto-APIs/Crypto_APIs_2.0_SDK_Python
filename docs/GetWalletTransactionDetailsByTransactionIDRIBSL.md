# GetWalletTransactionDetailsByTransactionIDRIBSL

Litecoin

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locktime** | **int** | Represents the time at which a particular transaction can be added to the blockchain. | 
**size** | **int** | Represents the total size of this transaction. | 
**v_size** | **int** | Represents the virtual size of this transaction. | 
**version** | **int** | Represents the transaction version number. | 
**vin** | [**List[GetWalletTransactionDetailsByTransactionIDRIBSLVinInner]**](GetWalletTransactionDetailsByTransactionIDRIBSLVinInner.md) | Object Array representation of transaction inputs | 
**vout** | [**List[GetTransactionDetailsByTransactionIDRIBSLVoutInner]**](GetTransactionDetailsByTransactionIDRIBSLVoutInner.md) | Object Array representation of transaction outputs | 

## Example

```python
from cryptoapis.models.get_wallet_transaction_details_by_transaction_idribsl import GetWalletTransactionDetailsByTransactionIDRIBSL

# TODO update the JSON string below
json = "{}"
# create an instance of GetWalletTransactionDetailsByTransactionIDRIBSL from a JSON string
get_wallet_transaction_details_by_transaction_idribsl_instance = GetWalletTransactionDetailsByTransactionIDRIBSL.from_json(json)
# print the JSON string representation of the object
print GetWalletTransactionDetailsByTransactionIDRIBSL.to_json()

# convert the object into a dict
get_wallet_transaction_details_by_transaction_idribsl_dict = get_wallet_transaction_details_by_transaction_idribsl_instance.to_dict()
# create an instance of GetWalletTransactionDetailsByTransactionIDRIBSL from a dict
get_wallet_transaction_details_by_transaction_idribsl_form_dict = get_wallet_transaction_details_by_transaction_idribsl.from_dict(get_wallet_transaction_details_by_transaction_idribsl_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


