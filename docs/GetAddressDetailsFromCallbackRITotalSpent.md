# GetAddressDetailsFromCallbackRITotalSpent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Defines the total amount of all spent by this address coins, based on confirmed transactions. | 
**unit** | **str** | Represents the unit of the total spent amount. | 

## Example

```python
from cryptoapis.models.get_address_details_from_callback_ri_total_spent import GetAddressDetailsFromCallbackRITotalSpent

# TODO update the JSON string below
json = "{}"
# create an instance of GetAddressDetailsFromCallbackRITotalSpent from a JSON string
get_address_details_from_callback_ri_total_spent_instance = GetAddressDetailsFromCallbackRITotalSpent.from_json(json)
# print the JSON string representation of the object
print GetAddressDetailsFromCallbackRITotalSpent.to_json()

# convert the object into a dict
get_address_details_from_callback_ri_total_spent_dict = get_address_details_from_callback_ri_total_spent_instance.to_dict()
# create an instance of GetAddressDetailsFromCallbackRITotalSpent from a dict
get_address_details_from_callback_ri_total_spent_form_dict = get_address_details_from_callback_ri_total_spent.from_dict(get_address_details_from_callback_ri_total_spent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


