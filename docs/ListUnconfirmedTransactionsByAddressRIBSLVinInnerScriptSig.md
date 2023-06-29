# ListUnconfirmedTransactionsByAddressRIBSLVinInnerScriptSig

Specifies the required signatures.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asm** | **str** | The asm strands for assembly, which is the symbolic representation of the Bitcoin&#39;s Script language op-codes. | 
**hex** | **str** | String array representation of the hex | 
**type** | **str** | Represents the script type of the reference transaction identifier. | 

## Example

```python
from cryptoapis.models.list_unconfirmed_transactions_by_address_ribsl_vin_inner_script_sig import ListUnconfirmedTransactionsByAddressRIBSLVinInnerScriptSig

# TODO update the JSON string below
json = "{}"
# create an instance of ListUnconfirmedTransactionsByAddressRIBSLVinInnerScriptSig from a JSON string
list_unconfirmed_transactions_by_address_ribsl_vin_inner_script_sig_instance = ListUnconfirmedTransactionsByAddressRIBSLVinInnerScriptSig.from_json(json)
# print the JSON string representation of the object
print ListUnconfirmedTransactionsByAddressRIBSLVinInnerScriptSig.to_json()

# convert the object into a dict
list_unconfirmed_transactions_by_address_ribsl_vin_inner_script_sig_dict = list_unconfirmed_transactions_by_address_ribsl_vin_inner_script_sig_instance.to_dict()
# create an instance of ListUnconfirmedTransactionsByAddressRIBSLVinInnerScriptSig from a dict
list_unconfirmed_transactions_by_address_ribsl_vin_inner_script_sig_form_dict = list_unconfirmed_transactions_by_address_ribsl_vin_inner_script_sig.from_dict(list_unconfirmed_transactions_by_address_ribsl_vin_inner_script_sig_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


