# GetWalletTransactionDetailsByTransactionIDRIBSD2

Dash

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locktime** | **int** | Represents the time at which a particular transaction can be added to the blockchain. | 
**size** | **int** | Represents the total size of this transaction. | 
**version** | **int** | Represents the transaction version number. | 
**vin** | [**List[GetWalletTransactionDetailsByTransactionIDRIBSD2VinInner]**](GetWalletTransactionDetailsByTransactionIDRIBSD2VinInner.md) | Object Array representation of transaction inputs | 
**vout** | [**List[GetTransactionDetailsByTransactionIDRIBSD2VoutInner]**](GetTransactionDetailsByTransactionIDRIBSD2VoutInner.md) | Object Array representation of transaction outputs | 

## Example

```python
from cryptoapis.models.get_wallet_transaction_details_by_transaction_idribsd2 import GetWalletTransactionDetailsByTransactionIDRIBSD2

# TODO update the JSON string below
json = "{}"
# create an instance of GetWalletTransactionDetailsByTransactionIDRIBSD2 from a JSON string
get_wallet_transaction_details_by_transaction_idribsd2_instance = GetWalletTransactionDetailsByTransactionIDRIBSD2.from_json(json)
# print the JSON string representation of the object
print GetWalletTransactionDetailsByTransactionIDRIBSD2.to_json()

# convert the object into a dict
get_wallet_transaction_details_by_transaction_idribsd2_dict = get_wallet_transaction_details_by_transaction_idribsd2_instance.to_dict()
# create an instance of GetWalletTransactionDetailsByTransactionIDRIBSD2 from a dict
get_wallet_transaction_details_by_transaction_idribsd2_form_dict = get_wallet_transaction_details_by_transaction_idribsd2.from_dict(get_wallet_transaction_details_by_transaction_idribsd2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


