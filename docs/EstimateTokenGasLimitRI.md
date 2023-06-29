# EstimateTokenGasLimitRI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gas_limit** | **str** | Represents the amount of gas used by this specific transaction alone. | 

## Example

```python
from cryptoapis.models.estimate_token_gas_limit_ri import EstimateTokenGasLimitRI

# TODO update the JSON string below
json = "{}"
# create an instance of EstimateTokenGasLimitRI from a JSON string
estimate_token_gas_limit_ri_instance = EstimateTokenGasLimitRI.from_json(json)
# print the JSON string representation of the object
print EstimateTokenGasLimitRI.to_json()

# convert the object into a dict
estimate_token_gas_limit_ri_dict = estimate_token_gas_limit_ri_instance.to_dict()
# create an instance of EstimateTokenGasLimitRI from a dict
estimate_token_gas_limit_ri_form_dict = estimate_token_gas_limit_ri.from_dict(estimate_token_gas_limit_ri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


