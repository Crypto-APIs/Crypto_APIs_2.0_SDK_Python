# GetTransactionDetailsByTransactionIDFromCallbackRIBSP

Polygon

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Representation of the amount value. | 
**contract** | **str** | Represents the specific transaction contract. | 
**gas** | **str** | Represents the price offered to the miner to purchase this amount of gas. | 
**gas_price** | **str** | Represents the price offered to the miner to purchase this amount of gas. | 
**gas_used** | **str** | Represents the exact unit of gas that was used for the transaction. | 
**input** | **str** | Represents additional information that is required for the transaction. | 
**nonce** | **int** | Represents the sequential running number for an address, starting from 0 for the first transaction. E.g., if the nonce of a transaction is 10, it would be the 11th transaction sent from the sender&#39;s address. | 
**recipients** | **str** | Represents a list of recipient addresses with the respective amounts. In account-based protocols like Ethereum there is only one address in this list. | 
**senders** | **str** | Represents a list of sender addresses with the respective amounts. In account-based protocols like Ethereum there is only one address in this list. | 
**transaction_status** | **str** | Represents the status of this transaction. | 
**txid** | **str** | Represents the unique identifier of a transaction, i.e. it could be transactionId in UTXO-based protocols like Bitcoin, and transaction hash in Ethereum blockchain. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


