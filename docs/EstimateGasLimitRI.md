# EstimateGasLimitRI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gas_limit** | **str** | Represents the amount of gas used by this specific transaction alone. | 

## Example

```python
from cryptoapis.models.estimate_gas_limit_ri import EstimateGasLimitRI

# TODO update the JSON string below
json = "{}"
# create an instance of EstimateGasLimitRI from a JSON string
estimate_gas_limit_ri_instance = EstimateGasLimitRI.from_json(json)
# print the JSON string representation of the object
print EstimateGasLimitRI.to_json()

# convert the object into a dict
estimate_gas_limit_ri_dict = estimate_gas_limit_ri_instance.to_dict()
# create an instance of EstimateGasLimitRI from a dict
estimate_gas_limit_ri_form_dict = estimate_gas_limit_ri.from_dict(estimate_gas_limit_ri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


