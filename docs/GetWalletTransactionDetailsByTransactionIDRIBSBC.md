# GetWalletTransactionDetailsByTransactionIDRIBSBC

Bitcoin Cash

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locktime** | **int** | Represents the time at which a particular transaction can be added to the blockchain. | 
**size** | **int** | Represents the total size of this transaction. | 
**version** | **int** | Represents the transaction version number. | 
**vin** | [**List[GetWalletTransactionDetailsByTransactionIDRIBSBCVinInner]**](GetWalletTransactionDetailsByTransactionIDRIBSBCVinInner.md) | Object Array representation of transaction inputs | 
**vout** | [**List[GetWalletTransactionDetailsByTransactionIDRIBSBCVoutInner]**](GetWalletTransactionDetailsByTransactionIDRIBSBCVoutInner.md) | Object Array representation of transaction outputs | 

## Example

```python
from cryptoapis.models.get_wallet_transaction_details_by_transaction_idribsbc import GetWalletTransactionDetailsByTransactionIDRIBSBC

# TODO update the JSON string below
json = "{}"
# create an instance of GetWalletTransactionDetailsByTransactionIDRIBSBC from a JSON string
get_wallet_transaction_details_by_transaction_idribsbc_instance = GetWalletTransactionDetailsByTransactionIDRIBSBC.from_json(json)
# print the JSON string representation of the object
print GetWalletTransactionDetailsByTransactionIDRIBSBC.to_json()

# convert the object into a dict
get_wallet_transaction_details_by_transaction_idribsbc_dict = get_wallet_transaction_details_by_transaction_idribsbc_instance.to_dict()
# create an instance of GetWalletTransactionDetailsByTransactionIDRIBSBC from a dict
get_wallet_transaction_details_by_transaction_idribsbc_form_dict = get_wallet_transaction_details_by_transaction_idribsbc.from_dict(get_wallet_transaction_details_by_transaction_idribsbc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


