# ListInternalTransactionDetailsByTransactionHashRI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Defines the specific amount of the transaction. | 
**block_hash** | **str** | Represents the hash of the block, which is its unique identifier. It represents a cryptographic digital fingerprint made by hashing the block header twice through the SHA256 algorithm. | 
**block_height** | **int** | Represents the number of blocks in the blockchain preceding this specific block. Block numbers have no gaps. A blockchain usually starts with block 0 called the \&quot;Genesis block\&quot;. | 
**operation_id** | **str** | Represents the unique internal transaction ID in regards to the parent transaction (type trace address). | 
**operation_type** | **str** | Defines the call type of the internal transaction. | 
**parent_hash** | **str** | Defines the specific hash of the parent transaction. | 
**recipient** | **str** | Represents the recipient address with the respective amount. | 
**sender** | **str** | Represents the sender address with the respective amount. | 
**timestamp** | **int** | Defines the exact date/time in Unix Timestamp when this transaction was mined, confirmed or first seen in Mempool, if it is unconfirmed. | 

## Example

```python
from cryptoapis.models.list_internal_transaction_details_by_transaction_hash_ri import ListInternalTransactionDetailsByTransactionHashRI

# TODO update the JSON string below
json = "{}"
# create an instance of ListInternalTransactionDetailsByTransactionHashRI from a JSON string
list_internal_transaction_details_by_transaction_hash_ri_instance = ListInternalTransactionDetailsByTransactionHashRI.from_json(json)
# print the JSON string representation of the object
print ListInternalTransactionDetailsByTransactionHashRI.to_json()

# convert the object into a dict
list_internal_transaction_details_by_transaction_hash_ri_dict = list_internal_transaction_details_by_transaction_hash_ri_instance.to_dict()
# create an instance of ListInternalTransactionDetailsByTransactionHashRI from a dict
list_internal_transaction_details_by_transaction_hash_ri_form_dict = list_internal_transaction_details_by_transaction_hash_ri.from_dict(list_internal_transaction_details_by_transaction_hash_ri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


