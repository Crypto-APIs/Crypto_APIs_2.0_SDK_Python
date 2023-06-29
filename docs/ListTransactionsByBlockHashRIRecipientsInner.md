# ListTransactionsByBlockHashRIRecipientsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The address which receives this transaction. In UTXO-based protocols like Bitcoin there could be several senders while in account-based protocols like Ethereum there is always only one recipient. | 
**amount** | **str** | Represents the amount received to this address. | 

## Example

```python
from cryptoapis.models.list_transactions_by_block_hash_ri_recipients_inner import ListTransactionsByBlockHashRIRecipientsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListTransactionsByBlockHashRIRecipientsInner from a JSON string
list_transactions_by_block_hash_ri_recipients_inner_instance = ListTransactionsByBlockHashRIRecipientsInner.from_json(json)
# print the JSON string representation of the object
print ListTransactionsByBlockHashRIRecipientsInner.to_json()

# convert the object into a dict
list_transactions_by_block_hash_ri_recipients_inner_dict = list_transactions_by_block_hash_ri_recipients_inner_instance.to_dict()
# create an instance of ListTransactionsByBlockHashRIRecipientsInner from a dict
list_transactions_by_block_hash_ri_recipients_inner_form_dict = list_transactions_by_block_hash_ri_recipients_inner.from_dict(list_transactions_by_block_hash_ri_recipients_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


