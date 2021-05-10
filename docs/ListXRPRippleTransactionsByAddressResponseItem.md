# ListXRPRippleTransactionsByAddressResponseItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_data** | **str** | Represents any additional data that may be needed. | 
**index** | **int** | Represents the index position of the transaction in the block. | 
**mined_in_block_hash** | **str** | Represents the hash of the block where this transaction was mined/confirmed for first time. The hash is defined as a cryptographic digital fingerprint made by hashing the block header twice through the SHA256 algorithm. | 
**mined_in_block_height** | **int** | Represents the hight of the block where this transaction was mined/confirmed for first time. The height is defined as the number of blocks in the blockchain preceding this specific block. | 
**recipients** | [**[GetXRPRippleTransactionDetailsByTransactionIDResponseItemRecipients]**](GetXRPRippleTransactionDetailsByTransactionIDResponseItemRecipients.md) | Represents an object of addresses that receive the transactions. | 
**senders** | [**[GetXRPRippleTransactionDetailsByTransactionIDResponseItemSenders]**](GetXRPRippleTransactionDetailsByTransactionIDResponseItemSenders.md) | Represents an object of addresses that provide the funds. | 
**sequence** | **int** | Defines the transaction input&#39;s sequence as an integer, which is is used when transactions are replaced with newer versions before LockTime. | 
**status** | **str** | Defines the status of the transaction. | 
**timestamp** | **int** | Defines the exact date/time in Unix Timestamp when this transaction was mined, confirmed or first seen in Mempool, if it is unconfirmed. | 
**transaction_hash** | **str** | Represents the hash of the XRP transaction. | 
**type** | **str** | Specifies the type of the transaction. | 
**fee** | [**ListXRPRippleTransactionsByAddressResponseItemFee**](ListXRPRippleTransactionsByAddressResponseItemFee.md) |  | 
**offer** | [**ListXRPRippleTransactionsByAddressResponseItemOffer**](ListXRPRippleTransactionsByAddressResponseItemOffer.md) |  | 
**receive** | [**ListXRPRippleTransactionsByAddressResponseItemReceive**](ListXRPRippleTransactionsByAddressResponseItemReceive.md) |  | 
**value** | [**ListXRPRippleTransactionsByAddressResponseItemValue**](ListXRPRippleTransactionsByAddressResponseItemValue.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


