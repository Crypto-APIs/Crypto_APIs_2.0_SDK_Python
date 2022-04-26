# GetTransactionRequestDetailsRI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_details** | **str** | Defines an optional note for additional details. | 
**blockchain** | **str** | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. | 
**fee_priority** | **str** | Defines the priority for the fee, if it is \&quot;slow\&quot;, \&quot;standard\&quot; or \&quot;fast\&quot;. | 
**network** | **str** | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. | 
**recipients** | [**[GetTransactionRequestDetailsRIRecipients]**](GetTransactionRequestDetailsRIRecipients.md) | Represents a list of recipient addresses with the respective amounts. In account-based protocols like Ethereum there is only one address in this list. | 
**total_transaction_amount** | **str** | Defines the total transaction amount. | 
**transaction_request_status** | **str** | Defines the status of the transaction request, e.g. pending. | 
**transaction_type** | **str** | Defines the transaction type, if it is for coins or tokens. | 
**unit** | **str** | Defines the unit of the amount. | 
**wallet_id** | **str** | Defines the unique ID of the Wallet. | 
**transaction_id** | **str** | Represents the unique identifier of a transaction, i.e. it could be transactionId in UTXO-based protocols like Bitcoin, and transaction hash in Ethereum blockchain. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


