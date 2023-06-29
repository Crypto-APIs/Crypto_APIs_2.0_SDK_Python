# GetTransactionDetailsByTransactionIDRIBSLVoutInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_spent** | **bool** | Defines whether the output is spent or not. | 
**script_pub_key** | [**GetTransactionDetailsByTransactionIDRIBSLVoutInnerScriptPubKey**](GetTransactionDetailsByTransactionIDRIBSLVoutInnerScriptPubKey.md) |  | 
**value** | **str** | Represents the sent/received amount. | 

## Example

```python
from cryptoapis.models.get_transaction_details_by_transaction_idribsl_vout_inner import GetTransactionDetailsByTransactionIDRIBSLVoutInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetTransactionDetailsByTransactionIDRIBSLVoutInner from a JSON string
get_transaction_details_by_transaction_idribsl_vout_inner_instance = GetTransactionDetailsByTransactionIDRIBSLVoutInner.from_json(json)
# print the JSON string representation of the object
print GetTransactionDetailsByTransactionIDRIBSLVoutInner.to_json()

# convert the object into a dict
get_transaction_details_by_transaction_idribsl_vout_inner_dict = get_transaction_details_by_transaction_idribsl_vout_inner_instance.to_dict()
# create an instance of GetTransactionDetailsByTransactionIDRIBSLVoutInner from a dict
get_transaction_details_by_transaction_idribsl_vout_inner_form_dict = get_transaction_details_by_transaction_idribsl_vout_inner.from_dict(get_transaction_details_by_transaction_idribsl_vout_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


