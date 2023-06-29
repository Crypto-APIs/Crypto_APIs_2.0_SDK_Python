# ListTransactionsByBlockHeightRIBSBSCGasPrice


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Represents the price offered to the miner to purchase this amount of gas. | 
**unit** | **str** | Defines the unit of the gas price amount, e.g. BTC, ETH, XRP. | 

## Example

```python
from cryptoapis.models.list_transactions_by_block_height_ribsbsc_gas_price import ListTransactionsByBlockHeightRIBSBSCGasPrice

# TODO update the JSON string below
json = "{}"
# create an instance of ListTransactionsByBlockHeightRIBSBSCGasPrice from a JSON string
list_transactions_by_block_height_ribsbsc_gas_price_instance = ListTransactionsByBlockHeightRIBSBSCGasPrice.from_json(json)
# print the JSON string representation of the object
print ListTransactionsByBlockHeightRIBSBSCGasPrice.to_json()

# convert the object into a dict
list_transactions_by_block_height_ribsbsc_gas_price_dict = list_transactions_by_block_height_ribsbsc_gas_price_instance.to_dict()
# create an instance of ListTransactionsByBlockHeightRIBSBSCGasPrice from a dict
list_transactions_by_block_height_ribsbsc_gas_price_form_dict = list_transactions_by_block_height_ribsbsc_gas_price.from_dict(list_transactions_by_block_height_ribsbsc_gas_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


