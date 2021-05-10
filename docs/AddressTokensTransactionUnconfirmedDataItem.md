# AddressTokensTransactionUnconfirmedDataItem

Defines an `item` as one result.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blockchain** | **str** | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. | 
**network** | **str** | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot;, \&quot;rinkeby\&quot; are test networks. | 
**address** | **str** | Defines the specific address to which the token transaction has been sent and is pending confirmation. | 
**transaction_id** | **str** | Defines the unique ID of the specific transaction, i.e. its identification number. | 
**token_type** | **str** | Defines the type of token sent with the transaction, e.g. ERC 20. | 
**token** | [**AddressTokensTransactionUnconfirmedToken**](AddressTokensTransactionUnconfirmedToken.md) |  | 
**direction** | **str** | Defines whether the transaction is \&quot;incoming\&quot; or \&quot;outgoing\&quot;. | 
**first_seen_in_mempool_timestamp** | **int** | Defines the exact time the transaction has been first accepted into the mempool to await confirmation as timestamp. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


