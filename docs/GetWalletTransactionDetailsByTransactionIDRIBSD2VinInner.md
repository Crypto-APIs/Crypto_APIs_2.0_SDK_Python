# GetWalletTransactionDetailsByTransactionIDRIBSD2VinInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | **List[str]** |  | 
**coinbase** | **str** | Represents the coinbase hex. | [optional] 
**script_sig** | [**GetTransactionDetailsByTransactionIDRIBSD2VinInnerScriptSig**](GetTransactionDetailsByTransactionIDRIBSD2VinInnerScriptSig.md) |  | 
**sequence** | **int** | Represents the script sequence number. | 
**txid** | **str** | Represents the reference transaction identifier. | [optional] 
**txinwitness** | **List[str]** |  | [optional] 
**value** | **str** | Represents the sent/received amount. | [optional] 
**vout** | **int** | It refers to the index of the output address of this transaction. The index starts from 0. | [optional] 

## Example

```python
from cryptoapis.models.get_wallet_transaction_details_by_transaction_idribsd2_vin_inner import GetWalletTransactionDetailsByTransactionIDRIBSD2VinInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetWalletTransactionDetailsByTransactionIDRIBSD2VinInner from a JSON string
get_wallet_transaction_details_by_transaction_idribsd2_vin_inner_instance = GetWalletTransactionDetailsByTransactionIDRIBSD2VinInner.from_json(json)
# print the JSON string representation of the object
print GetWalletTransactionDetailsByTransactionIDRIBSD2VinInner.to_json()

# convert the object into a dict
get_wallet_transaction_details_by_transaction_idribsd2_vin_inner_dict = get_wallet_transaction_details_by_transaction_idribsd2_vin_inner_instance.to_dict()
# create an instance of GetWalletTransactionDetailsByTransactionIDRIBSD2VinInner from a dict
get_wallet_transaction_details_by_transaction_idribsd2_vin_inner_form_dict = get_wallet_transaction_details_by_transaction_idribsd2_vin_inner.from_dict(get_wallet_transaction_details_by_transaction_idribsd2_vin_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


