# ListTransactionsByBlockHeightRIFee


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Defines the amount of the fee. | 
**unit** | **str** | Defines the specific unit of the fee. | 

## Example

```python
from cryptoapis.models.list_transactions_by_block_height_ri_fee import ListTransactionsByBlockHeightRIFee

# TODO update the JSON string below
json = "{}"
# create an instance of ListTransactionsByBlockHeightRIFee from a JSON string
list_transactions_by_block_height_ri_fee_instance = ListTransactionsByBlockHeightRIFee.from_json(json)
# print the JSON string representation of the object
print ListTransactionsByBlockHeightRIFee.to_json()

# convert the object into a dict
list_transactions_by_block_height_ri_fee_dict = list_transactions_by_block_height_ri_fee_instance.to_dict()
# create an instance of ListTransactionsByBlockHeightRIFee from a dict
list_transactions_by_block_height_ri_fee_form_dict = list_transactions_by_block_height_ri_fee.from_dict(list_transactions_by_block_height_ri_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


