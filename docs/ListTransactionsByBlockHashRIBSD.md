# ListTransactionsByBlockHashRIBSD

Dogecoin

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locktime** | **int** | Represents the time at which a particular transaction can be added to the blockchain. | 
**size** | **int** | Represents the total size of this transaction. | 
**version** | **int** | Represents transaction version number. | 
**vin** | [**List[ListTransactionsByBlockHashRIBSDVinInner]**](ListTransactionsByBlockHashRIBSDVinInner.md) | Represents the transaction inputs. | 
**vout** | [**List[ListTransactionsByBlockHashRIBSDVoutInner]**](ListTransactionsByBlockHashRIBSDVoutInner.md) | Represents the transaction outputs. | 

## Example

```python
from cryptoapis.models.list_transactions_by_block_hash_ribsd import ListTransactionsByBlockHashRIBSD

# TODO update the JSON string below
json = "{}"
# create an instance of ListTransactionsByBlockHashRIBSD from a JSON string
list_transactions_by_block_hash_ribsd_instance = ListTransactionsByBlockHashRIBSD.from_json(json)
# print the JSON string representation of the object
print ListTransactionsByBlockHashRIBSD.to_json()

# convert the object into a dict
list_transactions_by_block_hash_ribsd_dict = list_transactions_by_block_hash_ribsd_instance.to_dict()
# create an instance of ListTransactionsByBlockHashRIBSD from a dict
list_transactions_by_block_hash_ribsd_form_dict = list_transactions_by_block_hash_ribsd.from_dict(list_transactions_by_block_hash_ribsd_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


