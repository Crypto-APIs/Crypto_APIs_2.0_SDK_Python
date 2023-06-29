# GetWalletTransactionDetailsByTransactionIDRI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_confirmed** | **bool** | Represents the state of the transaction whether it is confirmed or not confirmed. | 
**transaction_id** | **str** | Represents the unique identifier of a transaction, i.e. it could be &#x60;transactionId&#x60; in UTXO-based protocols like Bitcoin, and transaction &#x60;hash&#x60; in Ethereum blockchain. | 
**index** | **int** | Represents the index position of the transaction in the specific block. | 
**mined_in_block_hash** | **str** | Represents the hash of the block where this transaction was mined/confirmed for first time. The hash is defined as a cryptographic digital fingerprint made by hashing the block header twice through the SHA256 algorithm. | [optional] 
**mined_in_block_height** | **int** | Represents the hight of the block where this transaction was mined/confirmed for first time. The height is defined as the number of blocks in the blockchain preceding this specific block. | [optional] 
**recipients** | [**List[GetWalletTransactionDetailsByTransactionIDRIRecipientsInner]**](GetWalletTransactionDetailsByTransactionIDRIRecipientsInner.md) | Object Array representation of transaction receivers | 
**senders** | [**List[GetWalletTransactionDetailsByTransactionIDRISendersInner]**](GetWalletTransactionDetailsByTransactionIDRISendersInner.md) | String representation of the transaction from address | 
**timestamp** | **int** | Defines the exact date/time in Unix Timestamp when this transaction was mined, confirmed or first seen in Mempool, if it is unconfirmed. | 
**transaction_hash** | **str** | Represents the same as &#x60;transactionId&#x60; for account-based protocols like Ethereum, while it could be different in UTXO-based protocols like Bitcoin. E.g., in UTXO-based protocols &#x60;hash&#x60; is different from &#x60;transactionId&#x60; for SegWit transactions. | 
**fee** | [**GetWalletTransactionDetailsByTransactionIDRIFee**](GetWalletTransactionDetailsByTransactionIDRIFee.md) |  | 
**blockchain_specific** | [**GetWalletTransactionDetailsByTransactionIDRIBS**](GetWalletTransactionDetailsByTransactionIDRIBS.md) |  | 

## Example

```python
from cryptoapis.models.get_wallet_transaction_details_by_transaction_idri import GetWalletTransactionDetailsByTransactionIDRI

# TODO update the JSON string below
json = "{}"
# create an instance of GetWalletTransactionDetailsByTransactionIDRI from a JSON string
get_wallet_transaction_details_by_transaction_idri_instance = GetWalletTransactionDetailsByTransactionIDRI.from_json(json)
# print the JSON string representation of the object
print GetWalletTransactionDetailsByTransactionIDRI.to_json()

# convert the object into a dict
get_wallet_transaction_details_by_transaction_idri_dict = get_wallet_transaction_details_by_transaction_idri_instance.to_dict()
# create an instance of GetWalletTransactionDetailsByTransactionIDRI from a dict
get_wallet_transaction_details_by_transaction_idri_form_dict = get_wallet_transaction_details_by_transaction_idri.from_dict(get_wallet_transaction_details_by_transaction_idri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


