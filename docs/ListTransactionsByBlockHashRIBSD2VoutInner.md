# ListTransactionsByBlockHashRIBSD2VoutInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_spent** | **bool** | Defines whether the output is spent or not. | 
**script_pub_key** | [**ListTransactionsByBlockHashRIBSD2VoutInnerScriptPubKey**](ListTransactionsByBlockHashRIBSD2VoutInnerScriptPubKey.md) |  | 
**value** | **str** | Represents the sent/received amount. | 

## Example

```python
from cryptoapis.models.list_transactions_by_block_hash_ribsd2_vout_inner import ListTransactionsByBlockHashRIBSD2VoutInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListTransactionsByBlockHashRIBSD2VoutInner from a JSON string
list_transactions_by_block_hash_ribsd2_vout_inner_instance = ListTransactionsByBlockHashRIBSD2VoutInner.from_json(json)
# print the JSON string representation of the object
print ListTransactionsByBlockHashRIBSD2VoutInner.to_json()

# convert the object into a dict
list_transactions_by_block_hash_ribsd2_vout_inner_dict = list_transactions_by_block_hash_ribsd2_vout_inner_instance.to_dict()
# create an instance of ListTransactionsByBlockHashRIBSD2VoutInner from a dict
list_transactions_by_block_hash_ribsd2_vout_inner_form_dict = list_transactions_by_block_hash_ribsd2_vout_inner.from_dict(list_transactions_by_block_hash_ribsd2_vout_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


