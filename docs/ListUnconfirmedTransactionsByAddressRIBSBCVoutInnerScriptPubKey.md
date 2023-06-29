# ListUnconfirmedTransactionsByAddressRIBSBCVoutInnerScriptPubKey

Represents the script public key.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | **List[str]** |  | 
**asm** | **str** | Represents the assembly of the script public key of the address. | 
**hex** | **str** | Represents the hex of the script public key of the address. | 
**req_sigs** | **int** | Represents the required signatures. | [optional] 
**type** | **str** | String representation of the type | 

## Example

```python
from cryptoapis.models.list_unconfirmed_transactions_by_address_ribsbc_vout_inner_script_pub_key import ListUnconfirmedTransactionsByAddressRIBSBCVoutInnerScriptPubKey

# TODO update the JSON string below
json = "{}"
# create an instance of ListUnconfirmedTransactionsByAddressRIBSBCVoutInnerScriptPubKey from a JSON string
list_unconfirmed_transactions_by_address_ribsbc_vout_inner_script_pub_key_instance = ListUnconfirmedTransactionsByAddressRIBSBCVoutInnerScriptPubKey.from_json(json)
# print the JSON string representation of the object
print ListUnconfirmedTransactionsByAddressRIBSBCVoutInnerScriptPubKey.to_json()

# convert the object into a dict
list_unconfirmed_transactions_by_address_ribsbc_vout_inner_script_pub_key_dict = list_unconfirmed_transactions_by_address_ribsbc_vout_inner_script_pub_key_instance.to_dict()
# create an instance of ListUnconfirmedTransactionsByAddressRIBSBCVoutInnerScriptPubKey from a dict
list_unconfirmed_transactions_by_address_ribsbc_vout_inner_script_pub_key_form_dict = list_unconfirmed_transactions_by_address_ribsbc_vout_inner_script_pub_key.from_dict(list_unconfirmed_transactions_by_address_ribsbc_vout_inner_script_pub_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


