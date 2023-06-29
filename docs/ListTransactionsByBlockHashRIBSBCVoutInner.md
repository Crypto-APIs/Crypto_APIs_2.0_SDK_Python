# ListTransactionsByBlockHashRIBSBCVoutInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_spent** | **bool** | Defines whether the output is spent or not. | 
**script_pub_key** | [**ListTransactionsByBlockHashRIBSBCVoutInnerScriptPubKey**](ListTransactionsByBlockHashRIBSBCVoutInnerScriptPubKey.md) |  | 
**value** | **str** | Represents the sent/received amount. | 

## Example

```python
from cryptoapis.models.list_transactions_by_block_hash_ribsbc_vout_inner import ListTransactionsByBlockHashRIBSBCVoutInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListTransactionsByBlockHashRIBSBCVoutInner from a JSON string
list_transactions_by_block_hash_ribsbc_vout_inner_instance = ListTransactionsByBlockHashRIBSBCVoutInner.from_json(json)
# print the JSON string representation of the object
print ListTransactionsByBlockHashRIBSBCVoutInner.to_json()

# convert the object into a dict
list_transactions_by_block_hash_ribsbc_vout_inner_dict = list_transactions_by_block_hash_ribsbc_vout_inner_instance.to_dict()
# create an instance of ListTransactionsByBlockHashRIBSBCVoutInner from a dict
list_transactions_by_block_hash_ribsbc_vout_inner_form_dict = list_transactions_by_block_hash_ribsbc_vout_inner.from_dict(list_transactions_by_block_hash_ribsbc_vout_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


