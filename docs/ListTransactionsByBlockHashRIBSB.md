# ListTransactionsByBlockHashRIBSB

Bitcoin

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locktime** | **int** | Represents the locktime on the transaction on the specific blockchain, i.e. the blockheight at which the transaction is valid. | 
**size** | **int** | Represents the total size of this transaction. | 
**v_size** | **int** | Represents the virtual size of this transaction. | 
**version** | **int** | Represents the transaction version number. | 
**vin** | [**List[ListTransactionsByBlockHashRIBSBVinInner]**](ListTransactionsByBlockHashRIBSBVinInner.md) | Represents the transaction inputs. | 
**vout** | [**List[ListTransactionsByBlockHashRIBSBVoutInner]**](ListTransactionsByBlockHashRIBSBVoutInner.md) | Represents the transaction outputs. | 

## Example

```python
from cryptoapis.models.list_transactions_by_block_hash_ribsb import ListTransactionsByBlockHashRIBSB

# TODO update the JSON string below
json = "{}"
# create an instance of ListTransactionsByBlockHashRIBSB from a JSON string
list_transactions_by_block_hash_ribsb_instance = ListTransactionsByBlockHashRIBSB.from_json(json)
# print the JSON string representation of the object
print ListTransactionsByBlockHashRIBSB.to_json()

# convert the object into a dict
list_transactions_by_block_hash_ribsb_dict = list_transactions_by_block_hash_ribsb_instance.to_dict()
# create an instance of ListTransactionsByBlockHashRIBSB from a dict
list_transactions_by_block_hash_ribsb_form_dict = list_transactions_by_block_hash_ribsb.from_dict(list_transactions_by_block_hash_ribsb_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


