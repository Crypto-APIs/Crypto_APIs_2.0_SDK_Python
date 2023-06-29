# ListTransactionsByBlockHeightRIBSLVinInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | **List[str]** |  | 
**coinbase** | **str** | Represents the coinbase hex. | [optional] 
**script_sig** | [**ListTransactionsByBlockHeightRIBSLVinInnerScriptSig**](ListTransactionsByBlockHeightRIBSLVinInnerScriptSig.md) |  | 
**sequence** | **str** | Represents the script sequence number. | 
**txid** | **str** | Represents the reference transaction identifier. | 
**txinwitness** | **List[str]** |  | 
**value** | **str** | Represents the sent/received amount. | 
**vout** | **int** | It refers to the index of the output address of this transaction. The index starts from 0. | 

## Example

```python
from cryptoapis.models.list_transactions_by_block_height_ribsl_vin_inner import ListTransactionsByBlockHeightRIBSLVinInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListTransactionsByBlockHeightRIBSLVinInner from a JSON string
list_transactions_by_block_height_ribsl_vin_inner_instance = ListTransactionsByBlockHeightRIBSLVinInner.from_json(json)
# print the JSON string representation of the object
print ListTransactionsByBlockHeightRIBSLVinInner.to_json()

# convert the object into a dict
list_transactions_by_block_height_ribsl_vin_inner_dict = list_transactions_by_block_height_ribsl_vin_inner_instance.to_dict()
# create an instance of ListTransactionsByBlockHeightRIBSLVinInner from a dict
list_transactions_by_block_height_ribsl_vin_inner_form_dict = list_transactions_by_block_height_ribsl_vin_inner.from_dict(list_transactions_by_block_height_ribsl_vin_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


