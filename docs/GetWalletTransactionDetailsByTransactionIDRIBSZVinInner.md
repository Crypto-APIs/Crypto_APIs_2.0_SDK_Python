# GetWalletTransactionDetailsByTransactionIDRIBSZVinInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | **List[str]** |  | 
**script_sig** | [**GetTransactionDetailsByTransactionIDRIBSZVinInnerScriptSig**](GetTransactionDetailsByTransactionIDRIBSZVinInnerScriptSig.md) |  | 
**sequence** | **int** | Represents the script sequence number. | 
**txid** | **str** | Represents the reference transaction identifier. | 
**txinwitness** | **List[str]** |  | [optional] 
**value** | **str** | Defines the specific amount. | 
**vout** | **int** | It refers to the index of the output address of this transaction. The index starts from 0. | 

## Example

```python
from cryptoapis.models.get_wallet_transaction_details_by_transaction_idribsz_vin_inner import GetWalletTransactionDetailsByTransactionIDRIBSZVinInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetWalletTransactionDetailsByTransactionIDRIBSZVinInner from a JSON string
get_wallet_transaction_details_by_transaction_idribsz_vin_inner_instance = GetWalletTransactionDetailsByTransactionIDRIBSZVinInner.from_json(json)
# print the JSON string representation of the object
print GetWalletTransactionDetailsByTransactionIDRIBSZVinInner.to_json()

# convert the object into a dict
get_wallet_transaction_details_by_transaction_idribsz_vin_inner_dict = get_wallet_transaction_details_by_transaction_idribsz_vin_inner_instance.to_dict()
# create an instance of GetWalletTransactionDetailsByTransactionIDRIBSZVinInner from a dict
get_wallet_transaction_details_by_transaction_idribsz_vin_inner_form_dict = get_wallet_transaction_details_by_transaction_idribsz_vin_inner.from_dict(get_wallet_transaction_details_by_transaction_idribsz_vin_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


