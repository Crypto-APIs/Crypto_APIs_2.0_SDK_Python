# GetFeeRecommendationsRI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unit** | **str** | Currency unit | 
**fast** | **str** | Fast fee per byte calculated from unconfirmed transactions | 
**slow** | **str** | Slow fee per byte calculated from unconfirmed transactions | 
**standard** | **str** | Standard fee per byte calculated from unconfirmed transactions | 
**fee_cushion_multiplier** | **str** | Fee cushion multiplier used to multiply the base fee | 

## Example

```python
from cryptoapis.models.get_fee_recommendations_ri import GetFeeRecommendationsRI

# TODO update the JSON string below
json = "{}"
# create an instance of GetFeeRecommendationsRI from a JSON string
get_fee_recommendations_ri_instance = GetFeeRecommendationsRI.from_json(json)
# print the JSON string representation of the object
print GetFeeRecommendationsRI.to_json()

# convert the object into a dict
get_fee_recommendations_ri_dict = get_fee_recommendations_ri_instance.to_dict()
# create an instance of GetFeeRecommendationsRI from a dict
get_fee_recommendations_ri_form_dict = get_fee_recommendations_ri.from_dict(get_fee_recommendations_ri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


