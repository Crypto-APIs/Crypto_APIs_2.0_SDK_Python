# ListTransactionsByBlockHeightRIBSZVinInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | **List[str]** |  | 
**coinbase** | **str** | Represents the coinbase hex. | 
**script_sig** | [**ListTransactionsByBlockHeightRIBSZVinInnerScriptSig**](ListTransactionsByBlockHeightRIBSZVinInnerScriptSig.md) |  | 
**sequence** | **int** | Represents the script sequence number. | 
**txid** | **str** | Represents the reference transaction identifier. | 
**txinwitness** | **List[str]** |  | 
**value** | **str** | Defines the specific amount. | 
**vout** | **int** | It refers to the index of the output address of this transaction. The index starts from 0. | 

## Example

```python
from cryptoapis.models.list_transactions_by_block_height_ribsz_vin_inner import ListTransactionsByBlockHeightRIBSZVinInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListTransactionsByBlockHeightRIBSZVinInner from a JSON string
list_transactions_by_block_height_ribsz_vin_inner_instance = ListTransactionsByBlockHeightRIBSZVinInner.from_json(json)
# print the JSON string representation of the object
print ListTransactionsByBlockHeightRIBSZVinInner.to_json()

# convert the object into a dict
list_transactions_by_block_height_ribsz_vin_inner_dict = list_transactions_by_block_height_ribsz_vin_inner_instance.to_dict()
# create an instance of ListTransactionsByBlockHeightRIBSZVinInner from a dict
list_transactions_by_block_height_ribsz_vin_inner_form_dict = list_transactions_by_block_height_ribsz_vin_inner.from_dict(list_transactions_by_block_height_ribsz_vin_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


