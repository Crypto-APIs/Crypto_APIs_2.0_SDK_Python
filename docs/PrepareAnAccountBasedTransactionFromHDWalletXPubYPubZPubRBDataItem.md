# PrepareAnAccountBasedTransactionFromHDWalletXPubYPubZPubRBDataItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Representation of the amount of the transaction | 
**fee** | [**PrepareAnAccountBasedTransactionFromHDWalletXPubYPubZPubRBDataItemFee**](PrepareAnAccountBasedTransactionFromHDWalletXPubYPubZPubRBDataItemFee.md) |  | 
**recipient** | **str** | Represents a list of recipient addresses with the respective amounts. In account-based protocols like Ethereum there is only one address in this list. | 
**sender** | **str** | Represents a  sender address with the respective amount. In account-based protocols like Ethereum there is only one address in this list. | 
**xpub** | **str** | Defines the account extended publicly known key which is used to derive all child public keys. | 
**additional_data** | **str** | Representation of the additional data. | [optional] 
**nonce** | **str** | Representation of the nonce value | [optional] 
**transaction_type** | **str** | Representation of the transaction type | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


