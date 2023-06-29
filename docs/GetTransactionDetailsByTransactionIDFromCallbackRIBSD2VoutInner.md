# GetTransactionDetailsByTransactionIDFromCallbackRIBSD2VoutInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_spent** | **bool** | Defines whether the output is spent or not. | 
**script_pub_key** | [**GetTransactionDetailsByTransactionIDFromCallbackRIBSD2VoutInnerScriptPubKey**](GetTransactionDetailsByTransactionIDFromCallbackRIBSD2VoutInnerScriptPubKey.md) |  | 
**value** | **str** | String representation of the amount | 

## Example

```python
from cryptoapis.models.get_transaction_details_by_transaction_id_from_callback_ribsd2_vout_inner import GetTransactionDetailsByTransactionIDFromCallbackRIBSD2VoutInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetTransactionDetailsByTransactionIDFromCallbackRIBSD2VoutInner from a JSON string
get_transaction_details_by_transaction_id_from_callback_ribsd2_vout_inner_instance = GetTransactionDetailsByTransactionIDFromCallbackRIBSD2VoutInner.from_json(json)
# print the JSON string representation of the object
print GetTransactionDetailsByTransactionIDFromCallbackRIBSD2VoutInner.to_json()

# convert the object into a dict
get_transaction_details_by_transaction_id_from_callback_ribsd2_vout_inner_dict = get_transaction_details_by_transaction_id_from_callback_ribsd2_vout_inner_instance.to_dict()
# create an instance of GetTransactionDetailsByTransactionIDFromCallbackRIBSD2VoutInner from a dict
get_transaction_details_by_transaction_id_from_callback_ribsd2_vout_inner_form_dict = get_transaction_details_by_transaction_id_from_callback_ribsd2_vout_inner.from_dict(get_transaction_details_by_transaction_id_from_callback_ribsd2_vout_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


