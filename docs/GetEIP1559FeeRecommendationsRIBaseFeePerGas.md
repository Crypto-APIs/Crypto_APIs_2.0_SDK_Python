# GetEIP1559FeeRecommendationsRIBaseFeePerGas


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unit** | **str** | Represents the unit of the base fee per gas. | 
**value** | **str** | Represents the expected base fee per gas of the upcoming block, calculated from the previous block data. | 

## Example

```python
from cryptoapis.models.get_eip1559_fee_recommendations_ri_base_fee_per_gas import GetEIP1559FeeRecommendationsRIBaseFeePerGas

# TODO update the JSON string below
json = "{}"
# create an instance of GetEIP1559FeeRecommendationsRIBaseFeePerGas from a JSON string
get_eip1559_fee_recommendations_ri_base_fee_per_gas_instance = GetEIP1559FeeRecommendationsRIBaseFeePerGas.from_json(json)
# print the JSON string representation of the object
print GetEIP1559FeeRecommendationsRIBaseFeePerGas.to_json()

# convert the object into a dict
get_eip1559_fee_recommendations_ri_base_fee_per_gas_dict = get_eip1559_fee_recommendations_ri_base_fee_per_gas_instance.to_dict()
# create an instance of GetEIP1559FeeRecommendationsRIBaseFeePerGas from a dict
get_eip1559_fee_recommendations_ri_base_fee_per_gas_form_dict = get_eip1559_fee_recommendations_ri_base_fee_per_gas.from_dict(get_eip1559_fee_recommendations_ri_base_fee_per_gas_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


