# PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRBDataItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee** | [**PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRBDataItemFee**](PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRBDataItemFee.md) |  | 
**recipients** | [**[PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRBDataItemRecipientsInner]**](PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRBDataItemRecipientsInner.md) | Represents a list of recipient addresses with the respective amounts. In account-based protocols like Ethereum there is only one address in this list. | 
**xpub** | **str** | Defines the account extended publicly known key which is used to derive all child public keys. | 
**additional_data** | **str** | Representation of the additional data. | [optional] 
**locktime** | **int** | Represents the time at which a particular transaction can be added to the blockchain. | [optional] 
**prepare_strategy** | **str** | Representation of the transaction&#39;s strategy type | [optional] 
**replaceable** | **bool** | Representation of whether the transaction is replaceable | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


