# ListTransactionsByBlockHashRIBSBSCGasPrice


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Represents the price offered to the miner to purchase this amount of gas. | 
**unit** | **str** | Defines the specific unit of the fee. | 

## Example

```python
from cryptoapis.models.list_transactions_by_block_hash_ribsbsc_gas_price import ListTransactionsByBlockHashRIBSBSCGasPrice

# TODO update the JSON string below
json = "{}"
# create an instance of ListTransactionsByBlockHashRIBSBSCGasPrice from a JSON string
list_transactions_by_block_hash_ribsbsc_gas_price_instance = ListTransactionsByBlockHashRIBSBSCGasPrice.from_json(json)
# print the JSON string representation of the object
print ListTransactionsByBlockHashRIBSBSCGasPrice.to_json()

# convert the object into a dict
list_transactions_by_block_hash_ribsbsc_gas_price_dict = list_transactions_by_block_hash_ribsbsc_gas_price_instance.to_dict()
# create an instance of ListTransactionsByBlockHashRIBSBSCGasPrice from a dict
list_transactions_by_block_hash_ribsbsc_gas_price_form_dict = list_transactions_by_block_hash_ribsbsc_gas_price.from_dict(list_transactions_by_block_hash_ribsbsc_gas_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


