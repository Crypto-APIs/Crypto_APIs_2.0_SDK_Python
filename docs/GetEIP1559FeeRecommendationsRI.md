# GetEIP1559FeeRecommendationsRI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_fee_per_gas** | [**GetEIP1559FeeRecommendationsRIBaseFeePerGas**](GetEIP1559FeeRecommendationsRIBaseFeePerGas.md) |  | 
**max_fee_per_gas** | [**GetEIP1559FeeRecommendationsRIMaxFeePerGas**](GetEIP1559FeeRecommendationsRIMaxFeePerGas.md) |  | 
**max_priority_fee_per_gas** | [**GetEIP1559FeeRecommendationsRIMaxPriorityFeePerGas**](GetEIP1559FeeRecommendationsRIMaxPriorityFeePerGas.md) |  | 

## Example

```python
from cryptoapis.models.get_eip1559_fee_recommendations_ri import GetEIP1559FeeRecommendationsRI

# TODO update the JSON string below
json = "{}"
# create an instance of GetEIP1559FeeRecommendationsRI from a JSON string
get_eip1559_fee_recommendations_ri_instance = GetEIP1559FeeRecommendationsRI.from_json(json)
# print the JSON string representation of the object
print GetEIP1559FeeRecommendationsRI.to_json()

# convert the object into a dict
get_eip1559_fee_recommendations_ri_dict = get_eip1559_fee_recommendations_ri_instance.to_dict()
# create an instance of GetEIP1559FeeRecommendationsRI from a dict
get_eip1559_fee_recommendations_ri_form_dict = get_eip1559_fee_recommendations_ri.from_dict(get_eip1559_fee_recommendations_ri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


