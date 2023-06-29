# ListDepositAddressesRIConfirmedBalance


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Defines the total balance of the address that is confirmed. It doesn&#39;t include unconfirmed transactions. | 
**unit** | **str** | Represents the unit of the confirmed balance. | 

## Example

```python
from cryptoapis.models.list_deposit_addresses_ri_confirmed_balance import ListDepositAddressesRIConfirmedBalance

# TODO update the JSON string below
json = "{}"
# create an instance of ListDepositAddressesRIConfirmedBalance from a JSON string
list_deposit_addresses_ri_confirmed_balance_instance = ListDepositAddressesRIConfirmedBalance.from_json(json)
# print the JSON string representation of the object
print ListDepositAddressesRIConfirmedBalance.to_json()

# convert the object into a dict
list_deposit_addresses_ri_confirmed_balance_dict = list_deposit_addresses_ri_confirmed_balance_instance.to_dict()
# create an instance of ListDepositAddressesRIConfirmedBalance from a dict
list_deposit_addresses_ri_confirmed_balance_form_dict = list_deposit_addresses_ri_confirmed_balance.from_dict(list_deposit_addresses_ri_confirmed_balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


