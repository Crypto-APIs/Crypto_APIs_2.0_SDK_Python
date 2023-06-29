# EstimateTokenGasLimitRB


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **str** | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional] 
**data** | [**EstimateTokenGasLimitRBData**](EstimateTokenGasLimitRBData.md) |  | 

## Example

```python
from cryptoapis.models.estimate_token_gas_limit_rb import EstimateTokenGasLimitRB

# TODO update the JSON string below
json = "{}"
# create an instance of EstimateTokenGasLimitRB from a JSON string
estimate_token_gas_limit_rb_instance = EstimateTokenGasLimitRB.from_json(json)
# print the JSON string representation of the object
print EstimateTokenGasLimitRB.to_json()

# convert the object into a dict
estimate_token_gas_limit_rb_dict = estimate_token_gas_limit_rb_instance.to_dict()
# create an instance of EstimateTokenGasLimitRB from a dict
estimate_token_gas_limit_rb_form_dict = estimate_token_gas_limit_rb.from_dict(estimate_token_gas_limit_rb_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


