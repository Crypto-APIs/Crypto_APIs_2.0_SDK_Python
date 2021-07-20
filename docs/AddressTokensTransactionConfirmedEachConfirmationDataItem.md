# AddressTokensTransactionConfirmedEachConfirmationDataItem

Defines an `item` as one result.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blockchain** | **str** | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. | 
**network** | **str** | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot;, \&quot;rinkeby\&quot; are test networks. | 
**address** | **str** | Defines the specific address to which the transaction has been sent. | 
**mined_in_block** | [**AddressTokensTransactionConfirmedEachConfirmationDataItemMinedInBlock**](AddressTokensTransactionConfirmedEachConfirmationDataItemMinedInBlock.md) |  | 
**transaction_id** | **str** | Defines the unique ID of the specific transaction, i.e. its identification number. | 
**current_confirmations** | **int** | Defines the number of currently received confirmations for the transaction. | 
**target_confirmations** | **int** | Defines the number of confirmation transactions requested as callbacks, i.e. the system can notify till the n-th confirmation. | 
**token_type** | **str** | Defines the type of token sent with the transaction, e.g. ERC 20. | 
**token** | [**AddressTokensTransactionConfirmedEachConfirmationToken**](AddressTokensTransactionConfirmedEachConfirmationToken.md) |  | 
**direction** | **str** | Defines whether the transaction is \&quot;incoming\&quot; or \&quot;outgoing\&quot;. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


