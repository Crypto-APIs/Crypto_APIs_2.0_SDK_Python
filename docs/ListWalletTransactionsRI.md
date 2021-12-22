# ListWalletTransactionsRI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | **str** | Defines the direction of the transaction, e.g. incoming. | 
**fee** | [**ListWalletTransactionsRIFee**](ListWalletTransactionsRIFee.md) |  | 
**recipients** | [**[ListWalletTransactionsRIRecipients]**](ListWalletTransactionsRIRecipients.md) | Represents a list of recipient addresses with the respective amounts. In account-based protocols like Ethereum there is only one address in this list. | 
**senders** | [**[ListWalletTransactionsRISenders]**](ListWalletTransactionsRISenders.md) | Represents a list of sender addresses with the respective amounts. In account-based protocols like Ethereum there is only one address in this list. | 
**status** | **str** | Defines the status of the transaction, if it is confirmed or unconfirmed. | 
**timestamp** | **int** | Defines the exact date/time in Unix Timestamp when this transaction was mined, confirmed or first seen in Mempool, if it is unconfirmed. | 
**transaction_id** | **str** | Represents the unique TD of the transaction. | 
**value** | [**ListWalletTransactionsRIValue**](ListWalletTransactionsRIValue.md) |  | 
**fungible_tokens** | [**[ListWalletTransactionsRIFungibleTokens]**](ListWalletTransactionsRIFungibleTokens.md) | Represents fungible tokens&#39;es detailed information | [optional] 
**internal_transactions** | [**[ListWalletTransactionsRIInternalTransactions]**](ListWalletTransactionsRIInternalTransactions.md) |  | [optional] 
**non_fungible_tokens** | [**[ListWalletTransactionsRINonFungibleTokens]**](ListWalletTransactionsRINonFungibleTokens.md) | Represents non-fungible tokens&#39;es detailed information. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


