# ListXRPRippleTransactionsByBlockHashRI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_data** | **str** | Represents any additional data that may be needed. | [optional] 
**destination_tag** | **int** |  | [optional] 
**index** | **int** | Represents the index position of the transaction in the specific block. | 
**mined_in_block_height** | **int** | Represents the hight of the block where this transaction was mined/confirmed for first time. The height is defined as the number of blocks in the blockchain preceding this specific block. | 
**offer** | [**ListXRPRippleTransactionsByBlockHashRIOffer**](ListXRPRippleTransactionsByBlockHashRIOffer.md) |  | 
**recipients** | [**List[ListXRPRippleTransactionsByBlockHashRIRecipientsInner]**](ListXRPRippleTransactionsByBlockHashRIRecipientsInner.md) | Represents an object of addresses that receive the transactions. | 
**senders** | [**List[ListXRPRippleTransactionsByBlockHashRISendersInner]**](ListXRPRippleTransactionsByBlockHashRISendersInner.md) | Represents an object of addresses that provide the funds. | 
**sequence** | **int** | Defines the transaction input&#39;s sequence as an integer, which is is used when transactions are replaced with newer versions before LockTime. | 
**status** | **str** | Defines the status of the transaction. | 
**timestamp** | **int** | Defines the exact date/time in Unix Timestamp when this transaction was mined, confirmed or first seen in Mempool, if it is unconfirmed. | 
**transaction_hash** | **str** | Represents the same as &#x60;transactionId&#x60; for account-based protocols like Ethereum, while it could be different in UTXO-based protocols like Bitcoin. E.g., in UTXO-based protocols &#x60;hash&#x60; is different from &#x60;transactionId&#x60; for SegWit transactions. | 
**type** | **str** | Defines the type of the transaction. | 
**fee** | [**ListXRPRippleTransactionsByBlockHashRIFee**](ListXRPRippleTransactionsByBlockHashRIFee.md) |  | 
**receive** | [**ListXRPRippleTransactionsByBlockHashRIReceive**](ListXRPRippleTransactionsByBlockHashRIReceive.md) |  | 
**value** | [**ListXRPRippleTransactionsByBlockHashRIValue**](ListXRPRippleTransactionsByBlockHashRIValue.md) |  | 

## Example

```python
from cryptoapis.models.list_xrp_ripple_transactions_by_block_hash_ri import ListXRPRippleTransactionsByBlockHashRI

# TODO update the JSON string below
json = "{}"
# create an instance of ListXRPRippleTransactionsByBlockHashRI from a JSON string
list_xrp_ripple_transactions_by_block_hash_ri_instance = ListXRPRippleTransactionsByBlockHashRI.from_json(json)
# print the JSON string representation of the object
print ListXRPRippleTransactionsByBlockHashRI.to_json()

# convert the object into a dict
list_xrp_ripple_transactions_by_block_hash_ri_dict = list_xrp_ripple_transactions_by_block_hash_ri_instance.to_dict()
# create an instance of ListXRPRippleTransactionsByBlockHashRI from a dict
list_xrp_ripple_transactions_by_block_hash_ri_form_dict = list_xrp_ripple_transactions_by_block_hash_ri.from_dict(list_xrp_ripple_transactions_by_block_hash_ri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


