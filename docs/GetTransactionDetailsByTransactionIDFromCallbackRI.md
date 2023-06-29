# GetTransactionDetailsByTransactionIDFromCallbackRI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** | Represents the index position of the transaction in the specific block. | 
**is_confirmed** | **bool** | Represents the state of the transaction whether it is confirmed or not confirmed. | 
**mined_in_block_hash** | **str** | Represents the hash of the block where this transaction was mined/confirmed for first time. The hash is defined as a cryptographic digital fingerprint made by hashing the block header twice through the SHA256 algorithm. | 
**mined_in_block_height** | **int** | Represents the hight of the block where this transaction was mined/confirmed for first time. The height is defined as the number of blocks in the blockchain preceding this specific block. | 
**recipients** | [**List[GetTransactionDetailsByTransactionIDRIRecipientsInner]**](GetTransactionDetailsByTransactionIDRIRecipientsInner.md) | Represents a list of recipient addresses with the respective amounts. In account-based protocols like Ethereum there is only one address in this list. | 
**senders** | [**List[GetTransactionDetailsByTransactionIDRISendersInner]**](GetTransactionDetailsByTransactionIDRISendersInner.md) | Represents a list of sender addresses with the respective amounts. In account-based protocols like Ethereum there is only one address in this list. | 
**timestamp** | **int** | Defines the exact date/time in Unix Timestamp when this transaction was mined, confirmed or first seen in Mempool, if it is unconfirmed. | 
**transaction_hash** | **str** | Represents the same as transactionId for account-based protocols like Ethereum, while it could be different in UTXO-based protocols like Bitcoin. E.g., in UTXO-based protocols hash is different from transactionId for SegWit transactions. | 
**fee** | [**GetTransactionDetailsByTransactionIDFromCallbackRIFee**](GetTransactionDetailsByTransactionIDFromCallbackRIFee.md) |  | 
**transaction_id** | **str** | String representation of the transaction hash | 
**blockchain_specific** | [**GetTransactionDetailsByTransactionIDFromCallbackRIBS**](GetTransactionDetailsByTransactionIDFromCallbackRIBS.md) |  | 

## Example

```python
from cryptoapis.models.get_transaction_details_by_transaction_id_from_callback_ri import GetTransactionDetailsByTransactionIDFromCallbackRI

# TODO update the JSON string below
json = "{}"
# create an instance of GetTransactionDetailsByTransactionIDFromCallbackRI from a JSON string
get_transaction_details_by_transaction_id_from_callback_ri_instance = GetTransactionDetailsByTransactionIDFromCallbackRI.from_json(json)
# print the JSON string representation of the object
print GetTransactionDetailsByTransactionIDFromCallbackRI.to_json()

# convert the object into a dict
get_transaction_details_by_transaction_id_from_callback_ri_dict = get_transaction_details_by_transaction_id_from_callback_ri_instance.to_dict()
# create an instance of GetTransactionDetailsByTransactionIDFromCallbackRI from a dict
get_transaction_details_by_transaction_id_from_callback_ri_form_dict = get_transaction_details_by_transaction_id_from_callback_ri.from_dict(get_transaction_details_by_transaction_id_from_callback_ri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


