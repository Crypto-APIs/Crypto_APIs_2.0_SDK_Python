# ListTransactionsByBlockHeightRIBSBC

Bitcoin Cash

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locktime** | **int** | Represents the time at which a particular transaction can be added to the blockchain. | 
**size** | **int** | Represents the total size of this transaction. | 
**version** | **int** | Represents the total size of this transaction. | 
**vin** | [**List[ListTransactionsByBlockHashRIBSBCVinInner]**](ListTransactionsByBlockHashRIBSBCVinInner.md) | Represents the transaction inputs. | 
**vout** | [**List[ListTransactionsByBlockHashRIBSBCVoutInner]**](ListTransactionsByBlockHashRIBSBCVoutInner.md) | Represents the transaction outputs. | 

## Example

```python
from cryptoapis.models.list_transactions_by_block_height_ribsbc import ListTransactionsByBlockHeightRIBSBC

# TODO update the JSON string below
json = "{}"
# create an instance of ListTransactionsByBlockHeightRIBSBC from a JSON string
list_transactions_by_block_height_ribsbc_instance = ListTransactionsByBlockHeightRIBSBC.from_json(json)
# print the JSON string representation of the object
print ListTransactionsByBlockHeightRIBSBC.to_json()

# convert the object into a dict
list_transactions_by_block_height_ribsbc_dict = list_transactions_by_block_height_ribsbc_instance.to_dict()
# create an instance of ListTransactionsByBlockHeightRIBSBC from a dict
list_transactions_by_block_height_ribsbc_form_dict = list_transactions_by_block_height_ribsbc.from_dict(list_transactions_by_block_height_ribsbc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


