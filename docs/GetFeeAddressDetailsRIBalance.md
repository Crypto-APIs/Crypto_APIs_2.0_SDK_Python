# GetFeeAddressDetailsRIBalance

Specifies the balance of the fee address.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Represents the amount of the units in fee address. | 
**unit** | **str** | Represents the unit of the fee spent for the forwarded tokens, e.g. BTC. | 

## Example

```python
from cryptoapis.models.get_fee_address_details_ri_balance import GetFeeAddressDetailsRIBalance

# TODO update the JSON string below
json = "{}"
# create an instance of GetFeeAddressDetailsRIBalance from a JSON string
get_fee_address_details_ri_balance_instance = GetFeeAddressDetailsRIBalance.from_json(json)
# print the JSON string representation of the object
print GetFeeAddressDetailsRIBalance.to_json()

# convert the object into a dict
get_fee_address_details_ri_balance_dict = get_fee_address_details_ri_balance_instance.to_dict()
# create an instance of GetFeeAddressDetailsRIBalance from a dict
get_fee_address_details_ri_balance_form_dict = get_fee_address_details_ri_balance.from_dict(get_fee_address_details_ri_balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


