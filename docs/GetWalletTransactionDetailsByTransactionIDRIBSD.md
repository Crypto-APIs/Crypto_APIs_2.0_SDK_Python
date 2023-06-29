# GetWalletTransactionDetailsByTransactionIDRIBSD

Dogecoin

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locktime** | **int** | Represents the time at which a particular transaction can be added to the blockchain. | 
**size** | **int** | Represents the total size of this transaction. | 
**version** | **int** | Represents the transaction version number. | 
**vin** | [**List[GetWalletTransactionDetailsByTransactionIDRIBSDVinInner]**](GetWalletTransactionDetailsByTransactionIDRIBSDVinInner.md) | Object Array representation of transaction inputs | 
**vout** | [**List[GetTransactionDetailsByTransactionIDRIBSDVoutInner]**](GetTransactionDetailsByTransactionIDRIBSDVoutInner.md) | Object Array representation of transaction outputs | 

## Example

```python
from cryptoapis.models.get_wallet_transaction_details_by_transaction_idribsd import GetWalletTransactionDetailsByTransactionIDRIBSD

# TODO update the JSON string below
json = "{}"
# create an instance of GetWalletTransactionDetailsByTransactionIDRIBSD from a JSON string
get_wallet_transaction_details_by_transaction_idribsd_instance = GetWalletTransactionDetailsByTransactionIDRIBSD.from_json(json)
# print the JSON string representation of the object
print GetWalletTransactionDetailsByTransactionIDRIBSD.to_json()

# convert the object into a dict
get_wallet_transaction_details_by_transaction_idribsd_dict = get_wallet_transaction_details_by_transaction_idribsd_instance.to_dict()
# create an instance of GetWalletTransactionDetailsByTransactionIDRIBSD from a dict
get_wallet_transaction_details_by_transaction_idribsd_form_dict = get_wallet_transaction_details_by_transaction_idribsd.from_dict(get_wallet_transaction_details_by_transaction_idribsd_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


