# ListTransactionsByBlockHashRI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | Represents the unique identifier of a transaction, i.e. it could be &#x60;transactionId&#x60; in UTXO-based protocols like Bitcoin, and transaction &#x60;hash&#x60; in Ethereum blockchain. | 
**index** | **int** | Represents the index position of the transaction in the specific block. | 
**mined_in_block_hash** | **str** | Represents the hash of the block where this transaction was mined/confirmed for first time. The hash is defined as a cryptographic digital fingerprint made by hashing the block header twice through the SHA256 algorithm. | 
**mined_in_block_height** | **int** | Represents the hight of the block where this transaction was mined/confirmed for first time. The height is defined as the number of blocks in the blockchain preceding this specific block. | 
**recipients** | [**List[ListTransactionsByBlockHashRIRecipientsInner]**](ListTransactionsByBlockHashRIRecipientsInner.md) | Represents a list of recipient addresses with the respective amounts. In account-based protocols like Ethereum there is only one address in this list. | 
**senders** | [**List[ListTransactionsByBlockHashRISendersInner]**](ListTransactionsByBlockHashRISendersInner.md) | Represents a list of sender addresses with the respective amounts. In account-based protocols like Ethereum there is only one address in this list. | 
**timestamp** | **int** | Defines the exact date/time in Unix Timestamp when this transaction was mined, confirmed or first seen in Mempool, if it is unconfirmed. | 
**transaction_hash** | **str** | Represents the same as &#x60;transactionId&#x60; for account-based protocols like Ethereum, while it could be different in UTXO-based protocols like Bitcoin. E.g., in UTXO-based protocols &#x60;hash&#x60; is different from &#x60;transactionId&#x60; for SegWit transactions. | 
**fee** | [**ListTransactionsByBlockHashRIFee**](ListTransactionsByBlockHashRIFee.md) |  | 
**blockchain_specific** | [**ListTransactionsByBlockHashRIBS**](ListTransactionsByBlockHashRIBS.md) |  | 

## Example

```python
from cryptoapis.models.list_transactions_by_block_hash_ri import ListTransactionsByBlockHashRI

# TODO update the JSON string below
json = "{}"
# create an instance of ListTransactionsByBlockHashRI from a JSON string
list_transactions_by_block_hash_ri_instance = ListTransactionsByBlockHashRI.from_json(json)
# print the JSON string representation of the object
print ListTransactionsByBlockHashRI.to_json()

# convert the object into a dict
list_transactions_by_block_hash_ri_dict = list_transactions_by_block_hash_ri_instance.to_dict()
# create an instance of ListTransactionsByBlockHashRI from a dict
list_transactions_by_block_hash_ri_form_dict = list_transactions_by_block_hash_ri.from_dict(list_transactions_by_block_hash_ri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


