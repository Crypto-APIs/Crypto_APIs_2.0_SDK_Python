# GetWalletTransactionDetailsByTransactionIDRIBSBCVinInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | **List[str]** |  | 
**coinbase** | **str** | Represents the coinbase hex. | [optional] 
**script_sig** | [**GetWalletTransactionDetailsByTransactionIDRIBSBCVinInnerScriptSig**](GetWalletTransactionDetailsByTransactionIDRIBSBCVinInnerScriptSig.md) |  | 
**sequence** | **int** | Represents the script sequence number. | 
**txid** | **str** | Represents the reference transaction identifier. | 
**txinwitness** | **List[str]** |  | [optional] 
**value** | **str** | Represents the sent/received amount. | [optional] 
**vout** | **int** | It refers to the index of the output address of this transaction. The index starts from 0. | [optional] 

## Example

```python
from cryptoapis.models.get_wallet_transaction_details_by_transaction_idribsbc_vin_inner import GetWalletTransactionDetailsByTransactionIDRIBSBCVinInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetWalletTransactionDetailsByTransactionIDRIBSBCVinInner from a JSON string
get_wallet_transaction_details_by_transaction_idribsbc_vin_inner_instance = GetWalletTransactionDetailsByTransactionIDRIBSBCVinInner.from_json(json)
# print the JSON string representation of the object
print GetWalletTransactionDetailsByTransactionIDRIBSBCVinInner.to_json()

# convert the object into a dict
get_wallet_transaction_details_by_transaction_idribsbc_vin_inner_dict = get_wallet_transaction_details_by_transaction_idribsbc_vin_inner_instance.to_dict()
# create an instance of GetWalletTransactionDetailsByTransactionIDRIBSBCVinInner from a dict
get_wallet_transaction_details_by_transaction_idribsbc_vin_inner_form_dict = get_wallet_transaction_details_by_transaction_idribsbc_vin_inner.from_dict(get_wallet_transaction_details_by_transaction_idribsbc_vin_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


