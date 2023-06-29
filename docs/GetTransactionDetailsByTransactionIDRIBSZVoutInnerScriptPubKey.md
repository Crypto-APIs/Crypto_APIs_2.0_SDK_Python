# GetTransactionDetailsByTransactionIDRIBSZVoutInnerScriptPubKey

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
from cryptoapis.models.get_transaction_details_by_transaction_idribsz_vout_inner_script_pub_key import GetTransactionDetailsByTransactionIDRIBSZVoutInnerScriptPubKey

# TODO update the JSON string below
json = "{}"
# create an instance of GetTransactionDetailsByTransactionIDRIBSZVoutInnerScriptPubKey from a JSON string
get_transaction_details_by_transaction_idribsz_vout_inner_script_pub_key_instance = GetTransactionDetailsByTransactionIDRIBSZVoutInnerScriptPubKey.from_json(json)
# print the JSON string representation of the object
print GetTransactionDetailsByTransactionIDRIBSZVoutInnerScriptPubKey.to_json()

# convert the object into a dict
get_transaction_details_by_transaction_idribsz_vout_inner_script_pub_key_dict = get_transaction_details_by_transaction_idribsz_vout_inner_script_pub_key_instance.to_dict()
# create an instance of GetTransactionDetailsByTransactionIDRIBSZVoutInnerScriptPubKey from a dict
get_transaction_details_by_transaction_idribsz_vout_inner_script_pub_key_form_dict = get_transaction_details_by_transaction_idribsz_vout_inner_script_pub_key.from_dict(get_transaction_details_by_transaction_idribsz_vout_inner_script_pub_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


