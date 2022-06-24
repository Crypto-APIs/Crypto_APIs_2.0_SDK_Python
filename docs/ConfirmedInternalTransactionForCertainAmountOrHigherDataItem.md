# ConfirmedInternalTransactionForCertainAmountOrHigherDataItem

Defines an `item` as one result.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blockchain** | **str** | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. | 
**network** | **str** | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot;,\&quot;mordor\&quot; are test networks. | 
**address** | **str** | Defines the specific address of the internal transaction. | 
**mined_in_block** | [**AddressInternalTransactionConfirmedDataItemMinedInBlock**](AddressInternalTransactionConfirmedDataItemMinedInBlock.md) |  | 
**parent_transaction_id** | **str** | Defines the Parent Transaction&#39;s unique ID. | 
**operation_id** | **str** | Defines the specific operation&#39;s unique ID. | 
**amount** | **str** | Defines the amount of coins sent with the confirmed transaction. | 
**unit** | **str** | Defines the unit of the transaction, e.g. Gwei. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


