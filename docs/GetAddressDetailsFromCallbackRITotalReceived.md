# GetAddressDetailsFromCallbackRITotalReceived


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Defines the total amount of all coins received to the address, based on confirmed transactions. | 
**unit** | **str** | Represents the unit of the total received amount. | 

## Example

```python
from cryptoapis.models.get_address_details_from_callback_ri_total_received import GetAddressDetailsFromCallbackRITotalReceived

# TODO update the JSON string below
json = "{}"
# create an instance of GetAddressDetailsFromCallbackRITotalReceived from a JSON string
get_address_details_from_callback_ri_total_received_instance = GetAddressDetailsFromCallbackRITotalReceived.from_json(json)
# print the JSON string representation of the object
print GetAddressDetailsFromCallbackRITotalReceived.to_json()

# convert the object into a dict
get_address_details_from_callback_ri_total_received_dict = get_address_details_from_callback_ri_total_received_instance.to_dict()
# create an instance of GetAddressDetailsFromCallbackRITotalReceived from a dict
get_address_details_from_callback_ri_total_received_form_dict = get_address_details_from_callback_ri_total_received.from_dict(get_address_details_from_callback_ri_total_received_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


