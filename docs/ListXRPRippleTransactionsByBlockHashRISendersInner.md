# ListXRPRippleTransactionsByBlockHashRISendersInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Represents the hash of the address that provides the funds. | 
**amount** | **str** | Represents the total amount sent by this address including the fee. | 

## Example

```python
from cryptoapis.models.list_xrp_ripple_transactions_by_block_hash_ri_senders_inner import ListXRPRippleTransactionsByBlockHashRISendersInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListXRPRippleTransactionsByBlockHashRISendersInner from a JSON string
list_xrp_ripple_transactions_by_block_hash_ri_senders_inner_instance = ListXRPRippleTransactionsByBlockHashRISendersInner.from_json(json)
# print the JSON string representation of the object
print ListXRPRippleTransactionsByBlockHashRISendersInner.to_json()

# convert the object into a dict
list_xrp_ripple_transactions_by_block_hash_ri_senders_inner_dict = list_xrp_ripple_transactions_by_block_hash_ri_senders_inner_instance.to_dict()
# create an instance of ListXRPRippleTransactionsByBlockHashRISendersInner from a dict
list_xrp_ripple_transactions_by_block_hash_ri_senders_inner_form_dict = list_xrp_ripple_transactions_by_block_hash_ri_senders_inner.from_dict(list_xrp_ripple_transactions_by_block_hash_ri_senders_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


