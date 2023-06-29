# GetWalletTransactionDetailsByTransactionIDRIBSB

Bitcoin

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locktime** | **int** | Represents the time at which a particular transaction can be added to the blockchain. | 
**size** | **int** | Represents the total size of this transaction. | 
**v_size** | **int** | Represents the virtual size of this transaction. | 
**version** | **int** | Represents the transaction version number. | 
**vin** | [**List[GetWalletTransactionDetailsByTransactionIDRIBSBVinInner]**](GetWalletTransactionDetailsByTransactionIDRIBSBVinInner.md) | Object Array representation of transaction inputs | 
**vout** | [**List[GetWalletTransactionDetailsByTransactionIDRIBSBVoutInner]**](GetWalletTransactionDetailsByTransactionIDRIBSBVoutInner.md) | Represents the transaction outputs. | 

## Example

```python
from cryptoapis.models.get_wallet_transaction_details_by_transaction_idribsb import GetWalletTransactionDetailsByTransactionIDRIBSB

# TODO update the JSON string below
json = "{}"
# create an instance of GetWalletTransactionDetailsByTransactionIDRIBSB from a JSON string
get_wallet_transaction_details_by_transaction_idribsb_instance = GetWalletTransactionDetailsByTransactionIDRIBSB.from_json(json)
# print the JSON string representation of the object
print GetWalletTransactionDetailsByTransactionIDRIBSB.to_json()

# convert the object into a dict
get_wallet_transaction_details_by_transaction_idribsb_dict = get_wallet_transaction_details_by_transaction_idribsb_instance.to_dict()
# create an instance of GetWalletTransactionDetailsByTransactionIDRIBSB from a dict
get_wallet_transaction_details_by_transaction_idribsb_form_dict = get_wallet_transaction_details_by_transaction_idribsb.from_dict(get_wallet_transaction_details_by_transaction_idribsb_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


