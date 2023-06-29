# ListZilliqaTransactionsByAddressRI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee** | [**GetZilliqaTransactionDetailsByTransactionIDRIFee**](GetZilliqaTransactionDetailsByTransactionIDRIFee.md) |  | 
**gas_limit** | **int** | Represents the maximum amount of gas allowed in the block in order to determine how many transactions it can fit. | 
**gas_price** | **int** | Defines the price of the gas. | 
**gas_used** | **int** | Defines how much of the gas for the block has been used. | 
**mined_in_block_hash** | **str** | Represents the hash of the block where this transaction was mined/confirmed for first time. The hash is defined as a cryptographic digital fingerprint made by hashing the block header twice through the SHA256 algorithm. | 
**mined_in_block_height** | **int** | Represents the number of blocks in the blockchain preceding this specific block. Block numbers have no gaps. A blockchain usually starts with block 0 called the \&quot;Genesis block\&quot;. | 
**nonce** | **int** | Represents a random value that can be adjusted to satisfy the Proof of Work. | 
**recipients** | [**List[ListZilliqaTransactionsByAddressRIRecipientsInner]**](ListZilliqaTransactionsByAddressRIRecipientsInner.md) | Defines an object array of the transaction recipients. | 
**senders** | [**List[ListZilliqaTransactionsByAddressRISendersInner]**](ListZilliqaTransactionsByAddressRISendersInner.md) | Represents an object of addresses that provide the funds. | 
**timestamp** | **int** | Defines the exact date/time when this block was mined in Unix Timestamp. | 
**transaction_hash** | **str** | Represents the hash of the transaction, which is its unique identifier. | 
**transaction_index** | **int** | Defines the numeric representation of the transaction index. | 
**transaction_status** | **str** | Defines the status of the transaction, whether it is e.g. pending or complete. | 

## Example

```python
from cryptoapis.models.list_zilliqa_transactions_by_address_ri import ListZilliqaTransactionsByAddressRI

# TODO update the JSON string below
json = "{}"
# create an instance of ListZilliqaTransactionsByAddressRI from a JSON string
list_zilliqa_transactions_by_address_ri_instance = ListZilliqaTransactionsByAddressRI.from_json(json)
# print the JSON string representation of the object
print ListZilliqaTransactionsByAddressRI.to_json()

# convert the object into a dict
list_zilliqa_transactions_by_address_ri_dict = list_zilliqa_transactions_by_address_ri_instance.to_dict()
# create an instance of ListZilliqaTransactionsByAddressRI from a dict
list_zilliqa_transactions_by_address_ri_form_dict = list_zilliqa_transactions_by_address_ri.from_dict(list_zilliqa_transactions_by_address_ri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


