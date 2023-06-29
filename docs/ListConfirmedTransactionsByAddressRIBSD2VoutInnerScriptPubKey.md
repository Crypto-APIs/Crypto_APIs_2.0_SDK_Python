# ListConfirmedTransactionsByAddressRIBSD2VoutInnerScriptPubKey

Represents the script public key.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | **List[str]** |  | 
**asm** | **str** | Represents the assembly of the script public key of the address. | 
**hex** | **str** | Represents the hex of the script public key of the address. | 
**req_sigs** | **int** | Represents the required signatures. | [optional] 
**type** | **str** | Represents the script type. | 

## Example

```python
from cryptoapis.models.list_confirmed_transactions_by_address_ribsd2_vout_inner_script_pub_key import ListConfirmedTransactionsByAddressRIBSD2VoutInnerScriptPubKey

# TODO update the JSON string below
json = "{}"
# create an instance of ListConfirmedTransactionsByAddressRIBSD2VoutInnerScriptPubKey from a JSON string
list_confirmed_transactions_by_address_ribsd2_vout_inner_script_pub_key_instance = ListConfirmedTransactionsByAddressRIBSD2VoutInnerScriptPubKey.from_json(json)
# print the JSON string representation of the object
print ListConfirmedTransactionsByAddressRIBSD2VoutInnerScriptPubKey.to_json()

# convert the object into a dict
list_confirmed_transactions_by_address_ribsd2_vout_inner_script_pub_key_dict = list_confirmed_transactions_by_address_ribsd2_vout_inner_script_pub_key_instance.to_dict()
# create an instance of ListConfirmedTransactionsByAddressRIBSD2VoutInnerScriptPubKey from a dict
list_confirmed_transactions_by_address_ribsd2_vout_inner_script_pub_key_form_dict = list_confirmed_transactions_by_address_ribsd2_vout_inner_script_pub_key.from_dict(list_confirmed_transactions_by_address_ribsd2_vout_inner_script_pub_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

