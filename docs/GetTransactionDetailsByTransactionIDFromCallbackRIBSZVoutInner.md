# GetTransactionDetailsByTransactionIDFromCallbackRIBSZVoutInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_spent** | **bool** | Defines whether the transaction output has been spent or not. | 
**script_pub_key** | [**GetTransactionDetailsByTransactionIDFromCallbackRIBSZVoutInnerScriptPubKey**](GetTransactionDetailsByTransactionIDFromCallbackRIBSZVoutInnerScriptPubKey.md) |  | 
**value** | **str** | Represents the specific amount. | 

## Example

```python
from cryptoapis.models.get_transaction_details_by_transaction_id_from_callback_ribsz_vout_inner import GetTransactionDetailsByTransactionIDFromCallbackRIBSZVoutInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetTransactionDetailsByTransactionIDFromCallbackRIBSZVoutInner from a JSON string
get_transaction_details_by_transaction_id_from_callback_ribsz_vout_inner_instance = GetTransactionDetailsByTransactionIDFromCallbackRIBSZVoutInner.from_json(json)
# print the JSON string representation of the object
print GetTransactionDetailsByTransactionIDFromCallbackRIBSZVoutInner.to_json()

# convert the object into a dict
get_transaction_details_by_transaction_id_from_callback_ribsz_vout_inner_dict = get_transaction_details_by_transaction_id_from_callback_ribsz_vout_inner_instance.to_dict()
# create an instance of GetTransactionDetailsByTransactionIDFromCallbackRIBSZVoutInner from a dict
get_transaction_details_by_transaction_id_from_callback_ribsz_vout_inner_form_dict = get_transaction_details_by_transaction_id_from_callback_ribsz_vout_inner.from_dict(get_transaction_details_by_transaction_id_from_callback_ribsz_vout_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


