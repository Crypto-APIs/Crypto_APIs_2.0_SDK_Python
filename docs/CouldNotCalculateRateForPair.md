# CouldNotCalculateRateForPair

could_not_calculate_rate_for_pair

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Specifies an error code, e.g. error 404. | 
**message** | **str** | Specifies the message of the error, i.e. why the error was returned, e.g. error 404 stands for “not found”. | 
**details** | [**List[BannedIpAddressDetailsInner]**](BannedIpAddressDetailsInner.md) |  | [optional] 

## Example

```python
from cryptoapis.models.could_not_calculate_rate_for_pair import CouldNotCalculateRateForPair

# TODO update the JSON string below
json = "{}"
# create an instance of CouldNotCalculateRateForPair from a JSON string
could_not_calculate_rate_for_pair_instance = CouldNotCalculateRateForPair.from_json(json)
# print the JSON string representation of the object
print CouldNotCalculateRateForPair.to_json()

# convert the object into a dict
could_not_calculate_rate_for_pair_dict = could_not_calculate_rate_for_pair_instance.to_dict()
# create an instance of CouldNotCalculateRateForPair from a dict
could_not_calculate_rate_for_pair_form_dict = could_not_calculate_rate_for_pair.from_dict(could_not_calculate_rate_for_pair_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


