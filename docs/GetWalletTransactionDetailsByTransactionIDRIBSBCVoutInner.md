# GetWalletTransactionDetailsByTransactionIDRIBSBCVoutInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_spent** | **bool** | Defines whether the output is spent or not. | 
**script_pub_key** | [**GetWalletTransactionDetailsByTransactionIDRIBSBCVoutInnerScriptPubKey**](GetWalletTransactionDetailsByTransactionIDRIBSBCVoutInnerScriptPubKey.md) |  | 
**value** | **str** | Represents the sent/received amount. | 

## Example

```python
from cryptoapis.models.get_wallet_transaction_details_by_transaction_idribsbc_vout_inner import GetWalletTransactionDetailsByTransactionIDRIBSBCVoutInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetWalletTransactionDetailsByTransactionIDRIBSBCVoutInner from a JSON string
get_wallet_transaction_details_by_transaction_idribsbc_vout_inner_instance = GetWalletTransactionDetailsByTransactionIDRIBSBCVoutInner.from_json(json)
# print the JSON string representation of the object
print GetWalletTransactionDetailsByTransactionIDRIBSBCVoutInner.to_json()

# convert the object into a dict
get_wallet_transaction_details_by_transaction_idribsbc_vout_inner_dict = get_wallet_transaction_details_by_transaction_idribsbc_vout_inner_instance.to_dict()
# create an instance of GetWalletTransactionDetailsByTransactionIDRIBSBCVoutInner from a dict
get_wallet_transaction_details_by_transaction_idribsbc_vout_inner_form_dict = get_wallet_transaction_details_by_transaction_idribsbc_vout_inner.from_dict(get_wallet_transaction_details_by_transaction_idribsbc_vout_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


