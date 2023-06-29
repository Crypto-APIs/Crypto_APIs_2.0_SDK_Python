# GetTransactionDetailsByTransactionIDRIBSD2VoutInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_spent** | **bool** | Defines whether the output is spent or not. | 
**script_pub_key** | [**GetTransactionDetailsByTransactionIDRIBSD2VoutInnerScriptPubKey**](GetTransactionDetailsByTransactionIDRIBSD2VoutInnerScriptPubKey.md) |  | 
**value** | **str** | Represents the sent/received amount. | 

## Example

```python
from cryptoapis.models.get_transaction_details_by_transaction_idribsd2_vout_inner import GetTransactionDetailsByTransactionIDRIBSD2VoutInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetTransactionDetailsByTransactionIDRIBSD2VoutInner from a JSON string
get_transaction_details_by_transaction_idribsd2_vout_inner_instance = GetTransactionDetailsByTransactionIDRIBSD2VoutInner.from_json(json)
# print the JSON string representation of the object
print GetTransactionDetailsByTransactionIDRIBSD2VoutInner.to_json()

# convert the object into a dict
get_transaction_details_by_transaction_idribsd2_vout_inner_dict = get_transaction_details_by_transaction_idribsd2_vout_inner_instance.to_dict()
# create an instance of GetTransactionDetailsByTransactionIDRIBSD2VoutInner from a dict
get_transaction_details_by_transaction_idribsd2_vout_inner_form_dict = get_transaction_details_by_transaction_idribsd2_vout_inner.from_dict(get_transaction_details_by_transaction_idribsd2_vout_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


