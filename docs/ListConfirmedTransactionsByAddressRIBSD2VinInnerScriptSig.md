# ListConfirmedTransactionsByAddressRIBSD2VinInnerScriptSig

Specifies the required signatures.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asm** | **str** | The asm strands for assembly, which is the symbolic representation of the Bitcoin&#39;s Script language op-codes. | 
**hex** | **str** | Represents the hex of the public key of the address. | 
**type** | **str** | Represents the script type of the reference transaction identifier. | 

## Example

```python
from cryptoapis.models.list_confirmed_transactions_by_address_ribsd2_vin_inner_script_sig import ListConfirmedTransactionsByAddressRIBSD2VinInnerScriptSig

# TODO update the JSON string below
json = "{}"
# create an instance of ListConfirmedTransactionsByAddressRIBSD2VinInnerScriptSig from a JSON string
list_confirmed_transactions_by_address_ribsd2_vin_inner_script_sig_instance = ListConfirmedTransactionsByAddressRIBSD2VinInnerScriptSig.from_json(json)
# print the JSON string representation of the object
print ListConfirmedTransactionsByAddressRIBSD2VinInnerScriptSig.to_json()

# convert the object into a dict
list_confirmed_transactions_by_address_ribsd2_vin_inner_script_sig_dict = list_confirmed_transactions_by_address_ribsd2_vin_inner_script_sig_instance.to_dict()
# create an instance of ListConfirmedTransactionsByAddressRIBSD2VinInnerScriptSig from a dict
list_confirmed_transactions_by_address_ribsd2_vin_inner_script_sig_form_dict = list_confirmed_transactions_by_address_ribsd2_vin_inner_script_sig.from_dict(list_confirmed_transactions_by_address_ribsd2_vin_inner_script_sig_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


