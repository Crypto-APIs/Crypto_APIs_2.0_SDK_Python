# EstimateTransactionSmartFeeRI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confirmation_target** | **int** | Represents the confirmation target in blocks | 
**fee_rate** | **str** | Represents the Fee Rate value. | 
**unit** | **str** | Defines the fee unit. | 

## Example

```python
from cryptoapis.models.estimate_transaction_smart_fee_ri import EstimateTransactionSmartFeeRI

# TODO update the JSON string below
json = "{}"
# create an instance of EstimateTransactionSmartFeeRI from a JSON string
estimate_transaction_smart_fee_ri_instance = EstimateTransactionSmartFeeRI.from_json(json)
# print the JSON string representation of the object
print EstimateTransactionSmartFeeRI.to_json()

# convert the object into a dict
estimate_transaction_smart_fee_ri_dict = estimate_transaction_smart_fee_ri_instance.to_dict()
# create an instance of EstimateTransactionSmartFeeRI from a dict
estimate_transaction_smart_fee_ri_form_dict = estimate_transaction_smart_fee_ri.from_dict(estimate_transaction_smart_fee_ri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


