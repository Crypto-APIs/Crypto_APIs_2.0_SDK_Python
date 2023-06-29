# ListTransactionsByBlockHashRIBSL

Litecoin

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locktime** | **int** | Represents the time at which a particular transaction can be added to the blockchain. | 
**size** | **int** | Represents the total size of this transaction. | 
**v_size** | **int** | Represents the virtual size of this transaction. | 
**version** | **int** | Represents transaction version number. | 
**vin** | [**List[ListTransactionsByBlockHashRIBSLVinInner]**](ListTransactionsByBlockHashRIBSLVinInner.md) | Represents the transaction inputs. | 
**vout** | [**List[ListTransactionsByBlockHashRIBSLVoutInner]**](ListTransactionsByBlockHashRIBSLVoutInner.md) | Represents the transaction outputs. | 

## Example

```python
from cryptoapis.models.list_transactions_by_block_hash_ribsl import ListTransactionsByBlockHashRIBSL

# TODO update the JSON string below
json = "{}"
# create an instance of ListTransactionsByBlockHashRIBSL from a JSON string
list_transactions_by_block_hash_ribsl_instance = ListTransactionsByBlockHashRIBSL.from_json(json)
# print the JSON string representation of the object
print ListTransactionsByBlockHashRIBSL.to_json()

# convert the object into a dict
list_transactions_by_block_hash_ribsl_dict = list_transactions_by_block_hash_ribsl_instance.to_dict()
# create an instance of ListTransactionsByBlockHashRIBSL from a dict
list_transactions_by_block_hash_ribsl_form_dict = list_transactions_by_block_hash_ribsl.from_dict(list_transactions_by_block_hash_ribsl_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


