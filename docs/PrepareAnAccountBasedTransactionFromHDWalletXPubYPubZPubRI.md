# PrepareAnAccountBasedTransactionFromHDWalletXPubYPubZPubRI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Representation of the amount of the transaction | 
**data_hex** | **str** | Representation of the data in hex value | 
**derivation_index** | **int** | Representation of the derivation index of the xpub address | 
**fee** | [**PrepareAnAccountBasedTransactionFromHDWalletXPubYPubZPubRIFee**](PrepareAnAccountBasedTransactionFromHDWalletXPubYPubZPubRIFee.md) |  | 
**nonce** | **str** | Represents the sequential running number for an address, starting from 0 for the first transaction. E.g., if the nonce of a transaction is 10, it would be the 11th transaction sent from the sender&#39;s address. | 
**recipient** | **str** | Represents a recipient addresses. In account-based protocols like Ethereum there is only one address in this list. | 
**sender** | **str** | Represents a sender address. In account-based protocols like Ethereum there is only one address in this list. | 
**sig_hash** | **str** | Representation of the hash that should be signed. | 
**transaction_type** | **str** | Representation of the transaction type | defaults to "legacy-transaction"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


