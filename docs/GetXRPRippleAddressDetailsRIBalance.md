# GetXRPRippleAddressDetailsRIBalance

Defines the balance of the account.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Represents the total amount of the balance. | 
**unit** | **str** | Represents the unit used for the balance. | 

## Example

```python
from cryptoapis.models.get_xrp_ripple_address_details_ri_balance import GetXRPRippleAddressDetailsRIBalance

# TODO update the JSON string below
json = "{}"
# create an instance of GetXRPRippleAddressDetailsRIBalance from a JSON string
get_xrp_ripple_address_details_ri_balance_instance = GetXRPRippleAddressDetailsRIBalance.from_json(json)
# print the JSON string representation of the object
print GetXRPRippleAddressDetailsRIBalance.to_json()

# convert the object into a dict
get_xrp_ripple_address_details_ri_balance_dict = get_xrp_ripple_address_details_ri_balance_instance.to_dict()
# create an instance of GetXRPRippleAddressDetailsRIBalance from a dict
get_xrp_ripple_address_details_ri_balance_form_dict = get_xrp_ripple_address_details_ri_balance.from_dict(get_xrp_ripple_address_details_ri_balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


