# ListTransactionsByBlockHashRIBS


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locktime** | **int** | Represents the time at which a particular transaction can be added to the blockchain. | [optional] 
**size** | **int** | Represents the total size of this transaction. | [optional] 
**v_size** | **int** | Represents the virtual size of this transaction. | [optional] 
**version** | **int** | Represents transaction version number. | [optional] 
**vin** | [**[ListTransactionsByBlockHashRIBSD2Vin]**](ListTransactionsByBlockHashRIBSD2Vin.md) | Represents the transaction inputs. | [optional] 
**vout** | [**[ListTransactionsByBlockHashRIBSD2Vout]**](ListTransactionsByBlockHashRIBSD2Vout.md) | Represents the transaction outputs. | [optional] 
**vsize** | **int** | Represents the virtual size of this transaction. | [optional] 
**contract** | **str** | Represents the specific transaction contract. | [optional] 
**gas_limit** | **str** | Represents the amount of gas used by this specific transaction alone. | [optional] 
**gas_price** | [**ListTransactionsByBlockHashRIBSEGasPrice**](ListTransactionsByBlockHashRIBSEGasPrice.md) |  | [optional] 
**gas_used** | **str** | Represents the exact unit of gas that was used for the transaction. | [optional] 
**input_data** | **str** | Represents additional information that is required for the transaction. | [optional] 
**nonce** | **str** | Represents the sequential running number for an address, starting from 0 for the first transaction. E.g., if the nonce of a transaction is 10, it would be the 11th transaction sent from the sender&#39;s address. | [optional] 
**transaction_status** | **str** | String representation of the transaction status | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


