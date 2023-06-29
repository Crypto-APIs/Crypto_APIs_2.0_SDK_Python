# GetWalletTransactionDetailsByTransactionIDRIBSDVinInnerScriptSig

Object representation of the script

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asm** | **str** | The asm strands for assembly, which is the symbolic representation of the Bitcoin&#39;s Script language op-codes. | 
**hex** | **str** | Represents the hex of the public key of the address. | 
**type** | **str** | Represents the script type of the reference transaction identifier. | 

## Example

```python
from cryptoapis.models.get_wallet_transaction_details_by_transaction_idribsd_vin_inner_script_sig import GetWalletTransactionDetailsByTransactionIDRIBSDVinInnerScriptSig

# TODO update the JSON string below
json = "{}"
# create an instance of GetWalletTransactionDetailsByTransactionIDRIBSDVinInnerScriptSig from a JSON string
get_wallet_transaction_details_by_transaction_idribsd_vin_inner_script_sig_instance = GetWalletTransactionDetailsByTransactionIDRIBSDVinInnerScriptSig.from_json(json)
# print the JSON string representation of the object
print GetWalletTransactionDetailsByTransactionIDRIBSDVinInnerScriptSig.to_json()

# convert the object into a dict
get_wallet_transaction_details_by_transaction_idribsd_vin_inner_script_sig_dict = get_wallet_transaction_details_by_transaction_idribsd_vin_inner_script_sig_instance.to_dict()
# create an instance of GetWalletTransactionDetailsByTransactionIDRIBSDVinInnerScriptSig from a dict
get_wallet_transaction_details_by_transaction_idribsd_vin_inner_script_sig_form_dict = get_wallet_transaction_details_by_transaction_idribsd_vin_inner_script_sig.from_dict(get_wallet_transaction_details_by_transaction_idribsd_vin_inner_script_sig_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


