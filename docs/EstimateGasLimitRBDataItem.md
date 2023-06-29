# EstimateGasLimitRBDataItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_data** | **str** | Represents an optional field to add additonal data. | [optional] 
**amount** | **str** | Represents transactions&#39; amount. | 
**recipient** | **str** | The address which receives this transaction. In UTXO-based protocols like Bitcoin there could be several senders while in account-based protocols like Ethereum there is always only one recipient. | 
**sender** | **str** | Represents the address which sends this transaction. In UTXO-based protocols like Bitcoin there could be several senders while in account-based protocols like Ethereum there is always only one sender. | 

## Example

```python
from cryptoapis.models.estimate_gas_limit_rb_data_item import EstimateGasLimitRBDataItem

# TODO update the JSON string below
json = "{}"
# create an instance of EstimateGasLimitRBDataItem from a JSON string
estimate_gas_limit_rb_data_item_instance = EstimateGasLimitRBDataItem.from_json(json)
# print the JSON string representation of the object
print EstimateGasLimitRBDataItem.to_json()

# convert the object into a dict
estimate_gas_limit_rb_data_item_dict = estimate_gas_limit_rb_data_item_instance.to_dict()
# create an instance of EstimateGasLimitRBDataItem from a dict
estimate_gas_limit_rb_data_item_form_dict = estimate_gas_limit_rb_data_item.from_dict(estimate_gas_limit_rb_data_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


