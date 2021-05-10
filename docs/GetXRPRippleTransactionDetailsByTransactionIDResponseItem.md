# GetXRPRippleTransactionDetailsByTransactionIDResponseItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_data** | **str** | Represents additional data that may be needed. | 
**index** | **str** | Defines the index of the transaction, i.e. the consecutive place it takes in the blockchain. | 
**mined_in_block_hash** | **str** | Represents the hash of the block where this transaction was mined/confirmed for first time. The hash is defined as a cryptographic digital fingerprint made by hashing the block header twice through the SHA256 algorithm. | 
**mined_in_block_height** | **str** | Represents the hight of the block where this transaction was mined/confirmed for first time. The height is defined as the number of blocks in the blockchain preceding this specific block. | 
**offer** | [**GetXRPRippleTransactionDetailsByTransactionIDResponseItemOffer**](GetXRPRippleTransactionDetailsByTransactionIDResponseItemOffer.md) |  | 
**receive** | [**GetXRPRippleTransactionDetailsByTransactionIDResponseItemReceive**](GetXRPRippleTransactionDetailsByTransactionIDResponseItemReceive.md) |  | 
**recipients** | [**[GetXRPRippleTransactionDetailsByTransactionIDResponseItemRecipients]**](GetXRPRippleTransactionDetailsByTransactionIDResponseItemRecipients.md) | Represents an object of addresses that receive the transactions. | 
**senders** | [**[GetXRPRippleTransactionDetailsByTransactionIDResponseItemSenders]**](GetXRPRippleTransactionDetailsByTransactionIDResponseItemSenders.md) | Represents an object of addresses that provide the funds. | 
**sequence** | **int** | Defines the transaction input&#39;s sequence as an integer, which is is used when transactions are replaced with newer versions before LockTime. | 
**timestamp** | **int** | Defines the exact date/time in Unix Timestamp when this transaction was mined, confirmed or first seen in Mempool, if it is unconfirmed. | 
**transaction_hash** | **str** | Represents the same as &#x60;transactionId&#x60; for account-based protocols like Ethereum, while it could be different in UTXO-based protocols like Bitcoin. E.g., in UTXO-based protocols &#x60;hash&#x60; is different from &#x60;transactionId&#x60; for SegWit transactions. | 
**type** | **str** | Defines the type of the transaction. | 
**fee** | [**GetXRPRippleTransactionDetailsByTransactionIDResponseItemFee**](GetXRPRippleTransactionDetailsByTransactionIDResponseItemFee.md) |  | 
**value** | [**GetXRPRippleTransactionDetailsByTransactionIDResponseItemValue**](GetXRPRippleTransactionDetailsByTransactionIDResponseItemValue.md) |  | 
**status** | **str** | Defines the status of the transaction. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


