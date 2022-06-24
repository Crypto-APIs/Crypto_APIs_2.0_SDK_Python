# DecodeRawTransactionHexRISD

Dash

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locktime** | **int** | Represents the time at which a particular transaction can be added to the blockchain. | 
**transaction_hash** | **str** | Represents the same as transactionId for account-based protocols like Ethereum, while it could be different in UTXO-based protocols like Bitcoin. E.g., in UTXO-based protocols hash is different from transactionId for SegWit transactions. | 
**v_size** | **int** | Represents the virtual size of this transaction. | 
**version** | **int** | Represents transaction version number. | 
**vin** | [**[DecodeRawTransactionHexRISDVinInner]**](DecodeRawTransactionHexRISDVinInner.md) | Represents the transaction inputs. | 
**vout** | [**[DecodeRawTransactionHexRISDVoutInner]**](DecodeRawTransactionHexRISDVoutInner.md) | Represents the transaction outputs. | 
**weight** | **int** | Represents the size of a block, measured in weight units and including the segwit discount. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


