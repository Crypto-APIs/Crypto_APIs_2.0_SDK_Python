# GetZilliqaTransactionDetailsByTransactionIDRI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee** | [**GetZilliqaTransactionDetailsByTransactionIDRIFee**](GetZilliqaTransactionDetailsByTransactionIDRIFee.md) |  | 
**gas_limit** | **int** | Represents the maximum amount of gas allowed in the block in order to determine how many transactions it can fit. | 
**gas_price** | **int** | Defines the price of the gas. | 
**gas_used** | **int** | Defines how much of the gas for the block has been used. | 
**mined_in_block_hash** | **str** | Represents the hash of the block, which is its unique identifier. It represents a cryptographic digital fingerprint made by hashing the block header twice through the SHA256 algorithm. | 
**mined_in_block_height** | **int** | Represents the number of blocks in the blockchain preceding this specific block. Block numbers have no gaps. A blockchain usually starts with block 0 called the \&quot;Genesis block\&quot;. | 
**nonce** | **int** | Represents the sequential running number for an address, starting from 0 for the first transaction. E.g., if the nonce of a transaction is 10, it would be the 11th transaction sent from the sender&#39;s address. | 
**recipients** | [**List[GetZilliqaTransactionDetailsByTransactionIDRIRecipientsInner]**](GetZilliqaTransactionDetailsByTransactionIDRIRecipientsInner.md) | Represents an object of addresses that receive the transactions. | 
**senders** | [**List[GetZilliqaTransactionDetailsByTransactionIDRISendersInner]**](GetZilliqaTransactionDetailsByTransactionIDRISendersInner.md) | Represents an object of addresses that provide the funds. | 
**timestamp** | **int** | Defines the exact date/time when this block was mined in Unix Timestamp. | 
**transaction_index** | **int** | Defines the numeric representation of the transaction index. | 
**transaction_status** | **str** | Defines the status of the transaction, whether it is e.g. pending or complete. | 

## Example

```python
from cryptoapis.models.get_zilliqa_transaction_details_by_transaction_idri import GetZilliqaTransactionDetailsByTransactionIDRI

# TODO update the JSON string below
json = "{}"
# create an instance of GetZilliqaTransactionDetailsByTransactionIDRI from a JSON string
get_zilliqa_transaction_details_by_transaction_idri_instance = GetZilliqaTransactionDetailsByTransactionIDRI.from_json(json)
# print the JSON string representation of the object
print GetZilliqaTransactionDetailsByTransactionIDRI.to_json()

# convert the object into a dict
get_zilliqa_transaction_details_by_transaction_idri_dict = get_zilliqa_transaction_details_by_transaction_idri_instance.to_dict()
# create an instance of GetZilliqaTransactionDetailsByTransactionIDRI from a dict
get_zilliqa_transaction_details_by_transaction_idri_form_dict = get_zilliqa_transaction_details_by_transaction_idri.from_dict(get_zilliqa_transaction_details_by_transaction_idri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


