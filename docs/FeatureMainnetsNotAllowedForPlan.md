# FeatureMainnetsNotAllowedForPlan

feature_mainnets_not_allowed_for_plan

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Specifies an error code, e.g. error 404. | 
**message** | **str** | Specifies the message of the error, i.e. why the error was returned, e.g. error 404 stands for “not found”. | 
**details** | [**List[BannedIpAddressDetailsInner]**](BannedIpAddressDetailsInner.md) |  | [optional] 

## Example

```python
from cryptoapis.models.feature_mainnets_not_allowed_for_plan import FeatureMainnetsNotAllowedForPlan

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureMainnetsNotAllowedForPlan from a JSON string
feature_mainnets_not_allowed_for_plan_instance = FeatureMainnetsNotAllowedForPlan.from_json(json)
# print the JSON string representation of the object
print FeatureMainnetsNotAllowedForPlan.to_json()

# convert the object into a dict
feature_mainnets_not_allowed_for_plan_dict = feature_mainnets_not_allowed_for_plan_instance.to_dict()
# create an instance of FeatureMainnetsNotAllowedForPlan from a dict
feature_mainnets_not_allowed_for_plan_form_dict = feature_mainnets_not_allowed_for_plan.from_dict(feature_mainnets_not_allowed_for_plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


