# CreateCoinsTransactionRequestFromWalletRBDataItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee_priority** | **str** | Represents the fee priority of the automation, whether it is \&quot;slow\&quot;, \&quot;standard\&quot; or \&quot;fast\&quot;. | 
**recipients** | [**[CreateCoinsTransactionRequestFromWalletRBDataItemRecipients]**](CreateCoinsTransactionRequestFromWalletRBDataItemRecipients.md) | Defines the destination of the transaction, whether it is incoming or outgoing. | 
**callback_secret_key** | **str** | Represents the Secret Key value provided by the customer. This field is used for security purposes during the callback notification, in order to prove the sender of the callback as Crypto APIs. For more information please see our [Documentation](https://developers.cryptoapis.io/technical-documentation/general-information/callbacks#callback-security). | [optional] 
**callback_url** | **str** | Represents the URL that is set by the customer where the callback will be received at. The callback notification will be received only if and when the event occurs. | [optional] 
**note** | **str** | Represents an optional note to add a free text in, explaining or providing additional detail on the transaction request. | [optional] 
**prepare_strategy** | **str** | Refers to a model of a UTXO spending strategy, where customers can choose how to spend their transaction outputs from multiple Bitcoin addresses. Two options available - \&quot;minimize-dust\&quot; (select lower amounts from multiple addresses) or \&quot;optimize-size\&quot; (select higher amounts from less addresses). | [optional]  if omitted the server will use the default value of "minimize-dust"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


