# TokensForwardingSuccessDataItem

Defines an `item` as one result.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blockchain** | **str** | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. | 
**network** | **str** | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. | 
**from_address** | **str** | Represents the hash of the address that provides the tokens. | 
**to_address** | **str** | Represents the hash of the address to forward the tokens to. | 
**spent_fees_amount** | **str** | Represents the amount of the fee spent for the tokens to be forwarded. | 
**spent_fees_unit** | **str** | Represents the unit of the fee spent for the tokens to be forwarded, e.g. BTC. | 
**trigger_transaction_id** | **str** | Defines the unique Transaction ID that triggered the token forwarding. | 
**forwarding_transaction_id** | **str** | Defines the unique Transaction ID that forwarded the tokens. | 
**token_type** | **str** | Defines the type of token sent with the transaction, e.g. ERC 20. | 
**token** | [**TokensForwardingSuccessToken**](TokensForwardingSuccessToken.md) |  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


