# GetAddressBalanceRI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confirmed_balance** | [**GetAddressBalanceRIConfirmedBalance**](GetAddressBalanceRIConfirmedBalance.md) |  | 

## Example

```python
from cryptoapis.models.get_address_balance_ri import GetAddressBalanceRI

# TODO update the JSON string below
json = "{}"
# create an instance of GetAddressBalanceRI from a JSON string
get_address_balance_ri_instance = GetAddressBalanceRI.from_json(json)
# print the JSON string representation of the object
print GetAddressBalanceRI.to_json()

# convert the object into a dict
get_address_balance_ri_dict = get_address_balance_ri_instance.to_dict()
# create an instance of GetAddressBalanceRI from a dict
get_address_balance_ri_form_dict = get_address_balance_ri.from_dict(get_address_balance_ri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


