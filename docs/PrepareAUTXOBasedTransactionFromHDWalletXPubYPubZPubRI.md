# PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee** | **str** | When isConfirmed is True - Defines the amount of the transaction fee When isConfirmed is False - For ETH-based blockchains this attribute represents the max fee value. | 
**locktime** | **int** | Represents the time at which a particular transaction can be added to the blockchain. | 
**replaceable** | **bool** | Representation of whether the transaction is replaceable | 
**size** | **int** | Represents the total size of this transaction. | 
**vin** | [**[PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIVinInner]**](PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIVinInner.md) | Represents the transaction inputs. | 
**vout** | [**[PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIVoutInner]**](PrepareAUTXOBasedTransactionFromHDWalletXPubYPubZPubRIVoutInner.md) | Represents the transaction outputs. | 
**additional_data** | **str** | Representation of the additional data | [optional] 
**fee_per_byte** | **str** | Defines the fee per byte value | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


