# GetZilliqaAddressDetailsRIBalance

Represents the total balance of the address as an object.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Represents the amount of the address&#39;s balance. | 
**unit** | **str** | Represents the unit of the address&#39;s balance. | 

## Example

```python
from cryptoapis.models.get_zilliqa_address_details_ri_balance import GetZilliqaAddressDetailsRIBalance

# TODO update the JSON string below
json = "{}"
# create an instance of GetZilliqaAddressDetailsRIBalance from a JSON string
get_zilliqa_address_details_ri_balance_instance = GetZilliqaAddressDetailsRIBalance.from_json(json)
# print the JSON string representation of the object
print GetZilliqaAddressDetailsRIBalance.to_json()

# convert the object into a dict
get_zilliqa_address_details_ri_balance_dict = get_zilliqa_address_details_ri_balance_instance.to_dict()
# create an instance of GetZilliqaAddressDetailsRIBalance from a dict
get_zilliqa_address_details_ri_balance_form_dict = get_zilliqa_address_details_ri_balance.from_dict(get_zilliqa_address_details_ri_balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


