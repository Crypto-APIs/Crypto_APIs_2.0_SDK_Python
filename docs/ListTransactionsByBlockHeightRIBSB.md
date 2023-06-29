# ListTransactionsByBlockHeightRIBSB

Bitcoin

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locktime** | **int** | Represents the time at which a particular transaction can be added to the blockchain. | 
**size** | **int** | Represents the total size of this transaction. | 
**v_size** | **int** | Represents the virtual size of this transaction. | 
**version** | **int** | Represents the transaction version number. | 
**vin** | [**List[ListTransactionsByBlockHashRIBSBVinInner]**](ListTransactionsByBlockHashRIBSBVinInner.md) | Represents the transaction inputs. | 
**vout** | [**List[ListTransactionsByBlockHeightRIBSBVoutInner]**](ListTransactionsByBlockHeightRIBSBVoutInner.md) | Represents the transaction outputs. | 

## Example

```python
from cryptoapis.models.list_transactions_by_block_height_ribsb import ListTransactionsByBlockHeightRIBSB

# TODO update the JSON string below
json = "{}"
# create an instance of ListTransactionsByBlockHeightRIBSB from a JSON string
list_transactions_by_block_height_ribsb_instance = ListTransactionsByBlockHeightRIBSB.from_json(json)
# print the JSON string representation of the object
print ListTransactionsByBlockHeightRIBSB.to_json()

# convert the object into a dict
list_transactions_by_block_height_ribsb_dict = list_transactions_by_block_height_ribsb_instance.to_dict()
# create an instance of ListTransactionsByBlockHeightRIBSB from a dict
list_transactions_by_block_height_ribsb_form_dict = list_transactions_by_block_height_ribsb.from_dict(list_transactions_by_block_height_ribsb_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


