# GetEIP1559FeeRecommendationsRIMaxPriorityFeePerGas


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fast** | **str** | Represents the fast maximum priority fee per gas, calculated from unconfirmed transactions. | 
**slow** | **str** | Represents the slow maximum priority fee per gas, calculated from unconfirmed transactions. | 
**standard** | **str** | Represents the standard maximum priority fee per gas, calculated from unconfirmed transactions. | 
**unit** | **str** | Represents the unit of the maximum priority fee per gas. | 

## Example

```python
from cryptoapis.models.get_eip1559_fee_recommendations_ri_max_priority_fee_per_gas import GetEIP1559FeeRecommendationsRIMaxPriorityFeePerGas

# TODO update the JSON string below
json = "{}"
# create an instance of GetEIP1559FeeRecommendationsRIMaxPriorityFeePerGas from a JSON string
get_eip1559_fee_recommendations_ri_max_priority_fee_per_gas_instance = GetEIP1559FeeRecommendationsRIMaxPriorityFeePerGas.from_json(json)
# print the JSON string representation of the object
print GetEIP1559FeeRecommendationsRIMaxPriorityFeePerGas.to_json()

# convert the object into a dict
get_eip1559_fee_recommendations_ri_max_priority_fee_per_gas_dict = get_eip1559_fee_recommendations_ri_max_priority_fee_per_gas_instance.to_dict()
# create an instance of GetEIP1559FeeRecommendationsRIMaxPriorityFeePerGas from a dict
get_eip1559_fee_recommendations_ri_max_priority_fee_per_gas_form_dict = get_eip1559_fee_recommendations_ri_max_priority_fee_per_gas.from_dict(get_eip1559_fee_recommendations_ri_max_priority_fee_per_gas_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


