# ListTransactionsByBlockHeightRIBSZVoutInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_spent** | **bool** | Defines whether the transaction output has been spent or not. | 
**script_pub_key** | [**ListTransactionsByBlockHeightRIBSZVoutInnerScriptPubKey**](ListTransactionsByBlockHeightRIBSZVoutInnerScriptPubKey.md) |  | 
**value** | **str** | Represents the specific amount. | 

## Example

```python
from cryptoapis.models.list_transactions_by_block_height_ribsz_vout_inner import ListTransactionsByBlockHeightRIBSZVoutInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListTransactionsByBlockHeightRIBSZVoutInner from a JSON string
list_transactions_by_block_height_ribsz_vout_inner_instance = ListTransactionsByBlockHeightRIBSZVoutInner.from_json(json)
# print the JSON string representation of the object
print ListTransactionsByBlockHeightRIBSZVoutInner.to_json()

# convert the object into a dict
list_transactions_by_block_height_ribsz_vout_inner_dict = list_transactions_by_block_height_ribsz_vout_inner_instance.to_dict()
# create an instance of ListTransactionsByBlockHeightRIBSZVoutInner from a dict
list_transactions_by_block_height_ribsz_vout_inner_form_dict = list_transactions_by_block_height_ribsz_vout_inner.from_dict(list_transactions_by_block_height_ribsz_vout_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


