# ListAllUnconfirmedTransactionsRI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipients** | [**[ListUnconfirmedTransactionsByAddressRIRecipients]**](ListUnconfirmedTransactionsByAddressRIRecipients.md) | Represents a list of recipient addresses with the respective amounts. In account-based protocols like Ethereum there is only one address in this list. | 
**senders** | [**[ListUnconfirmedTransactionsByAddressRISenders]**](ListUnconfirmedTransactionsByAddressRISenders.md) | Represents a list of sender addresses with the respective amounts. In account-based protocols like Ethereum there is only one address in this list. | 
**timestamp** | **int** | Defines the exact date/time in Unix Timestamp when this transaction was mined, confirmed or first seen in Mempool, if it is unconfirmed. | 
**transaction_id** | **str** | Represents the unique identifier of a transaction, i.e. it could be &#x60;transactionId&#x60; in UTXO-based protocols like Bitcoin, and transaction &#x60;hash&#x60; in Ethereum blockchain. | 
**blockchain_specific** | [**ListAllUnconfirmedTransactionsRIBS**](ListAllUnconfirmedTransactionsRIBS.md) |  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


