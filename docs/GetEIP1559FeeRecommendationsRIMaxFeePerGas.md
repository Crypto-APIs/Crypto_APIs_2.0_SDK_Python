# GetEIP1559FeeRecommendationsRIMaxFeePerGas


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fast** | **str** | Represents the fast maximum fee per gas, calculated from unconfirmed transactions. | 
**slow** | **str** | Represents the slow maximum fee per gas, calculated from unconfirmed transactions. | 
**standard** | **str** | Represents the standard maximum fee per gas, calculated from unconfirmed transactions. | 
**unit** | **str** | Represents the unit of the maximum fee per gas. | 

## Example

```python
from cryptoapis.models.get_eip1559_fee_recommendations_ri_max_fee_per_gas import GetEIP1559FeeRecommendationsRIMaxFeePerGas

# TODO update the JSON string below
json = "{}"
# create an instance of GetEIP1559FeeRecommendationsRIMaxFeePerGas from a JSON string
get_eip1559_fee_recommendations_ri_max_fee_per_gas_instance = GetEIP1559FeeRecommendationsRIMaxFeePerGas.from_json(json)
# print the JSON string representation of the object
print GetEIP1559FeeRecommendationsRIMaxFeePerGas.to_json()

# convert the object into a dict
get_eip1559_fee_recommendations_ri_max_fee_per_gas_dict = get_eip1559_fee_recommendations_ri_max_fee_per_gas_instance.to_dict()
# create an instance of GetEIP1559FeeRecommendationsRIMaxFeePerGas from a dict
get_eip1559_fee_recommendations_ri_max_fee_per_gas_form_dict = get_eip1559_fee_recommendations_ri_max_fee_per_gas.from_dict(get_eip1559_fee_recommendations_ri_max_fee_per_gas_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


