# ListTransactionsByBlockHeightRIBSD2

Dogecoin

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locktime** | **int** | Represents the time at which a particular transaction can be added to the blockchain. | 
**size** | **int** | Represents the total size of this transaction. | 
**version** | **int** | Represents transaction version number. | 
**vin** | [**List[ListTransactionsByBlockHeightRIBSD2VinInner]**](ListTransactionsByBlockHeightRIBSD2VinInner.md) | Represents the transaction inputs. | 
**vout** | [**List[ListTransactionsByBlockHeightRIBSD2VoutInner]**](ListTransactionsByBlockHeightRIBSD2VoutInner.md) | Represents the transaction outputs. | 

## Example

```python
from cryptoapis.models.list_transactions_by_block_height_ribsd2 import ListTransactionsByBlockHeightRIBSD2

# TODO update the JSON string below
json = "{}"
# create an instance of ListTransactionsByBlockHeightRIBSD2 from a JSON string
list_transactions_by_block_height_ribsd2_instance = ListTransactionsByBlockHeightRIBSD2.from_json(json)
# print the JSON string representation of the object
print ListTransactionsByBlockHeightRIBSD2.to_json()

# convert the object into a dict
list_transactions_by_block_height_ribsd2_dict = list_transactions_by_block_height_ribsd2_instance.to_dict()
# create an instance of ListTransactionsByBlockHeightRIBSD2 from a dict
list_transactions_by_block_height_ribsd2_form_dict = list_transactions_by_block_height_ribsd2.from_dict(list_transactions_by_block_height_ribsd2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


