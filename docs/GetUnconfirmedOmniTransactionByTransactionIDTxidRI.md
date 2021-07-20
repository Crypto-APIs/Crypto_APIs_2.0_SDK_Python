# GetUnconfirmedOmniTransactionByTransactionIDTxidRI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Defines the amount of the sent tokens. | 
**divisible** | **bool** | Defines whether the attribute can be divisible or not, as boolean. E.g., if it is \&quot;true\&quot;, the attribute is divisible. | 
**mined** | **bool** | Defines whether the transaction has been mined or not, as boolean. E.g. if set to \&quot;true\&quot;, it means the transaction is mined. | 
**property_id** | **int** | Represents the identifier of the tokens to send. | 
**recipients** | [**[GetUnconfirmedOmniTransactionByTransactionIDTxidRIRecipients]**](GetUnconfirmedOmniTransactionByTransactionIDTxidRIRecipients.md) | Represents an object of addresses that receive the transactions. | 
**senders** | [**[GetUnconfirmedOmniTransactionByTransactionIDTxidRISenders]**](GetUnconfirmedOmniTransactionByTransactionIDTxidRISenders.md) | Represents an object of addresses that provide the funds. | 
**sent** | **bool** | Defines whether the transaction has been sent or not, as boolean. E.g. if set to \&quot;true\&quot;, it means the transaction is sent. | 
**timestamp** | **int** | Defines the exact date/time in Unix Timestamp when this transaction was mined, confirmed or first seen in Mempool, if it is unconfirmed. | 
**transaction_id** | **str** | String representation of the transaction identifier (txid) | 
**type** | **str** | Defines the type of the transaction as a string. | 
**type_int** | **int** | Defines the type of the transaction as a number. | 
**version** | **int** | Defines the specific version. | 
**fee** | [**ListUnconfirmedOmniTransactionsByAddressRIFee**](ListUnconfirmedOmniTransactionsByAddressRIFee.md) |  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


