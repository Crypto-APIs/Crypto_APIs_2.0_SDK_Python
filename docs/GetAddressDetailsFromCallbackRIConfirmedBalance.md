# GetAddressDetailsFromCallbackRIConfirmedBalance


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Defines the total balance of the address that is confirmed. It doesn&#39;t include unconfirmed transactions. | 
**unit** | **str** | Represents the unit of the confirmed balance. | 

## Example

```python
from cryptoapis.models.get_address_details_from_callback_ri_confirmed_balance import GetAddressDetailsFromCallbackRIConfirmedBalance

# TODO update the JSON string below
json = "{}"
# create an instance of GetAddressDetailsFromCallbackRIConfirmedBalance from a JSON string
get_address_details_from_callback_ri_confirmed_balance_instance = GetAddressDetailsFromCallbackRIConfirmedBalance.from_json(json)
# print the JSON string representation of the object
print GetAddressDetailsFromCallbackRIConfirmedBalance.to_json()

# convert the object into a dict
get_address_details_from_callback_ri_confirmed_balance_dict = get_address_details_from_callback_ri_confirmed_balance_instance.to_dict()
# create an instance of GetAddressDetailsFromCallbackRIConfirmedBalance from a dict
get_address_details_from_callback_ri_confirmed_balance_form_dict = get_address_details_from_callback_ri_confirmed_balance.from_dict(get_address_details_from_callback_ri_confirmed_balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


