# AddressInternalTransactionConfirmedData

Specifies all data, as attributes, included into the callback notification, which depends on the `event`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product** | **str** | Represents the Crypto APIs 2.0 product which sends the callback. | 
**event** | **str** | Defines the specific event, for which a callback subscription is set. | 
**item** | [**AddressInternalTransactionConfirmedDataItem**](AddressInternalTransactionConfirmedDataItem.md) |  | 

## Example

```python
from cryptoapis.models.address_internal_transaction_confirmed_data import AddressInternalTransactionConfirmedData

# TODO update the JSON string below
json = "{}"
# create an instance of AddressInternalTransactionConfirmedData from a JSON string
address_internal_transaction_confirmed_data_instance = AddressInternalTransactionConfirmedData.from_json(json)
# print the JSON string representation of the object
print AddressInternalTransactionConfirmedData.to_json()

# convert the object into a dict
address_internal_transaction_confirmed_data_dict = address_internal_transaction_confirmed_data_instance.to_dict()
# create an instance of AddressInternalTransactionConfirmedData from a dict
address_internal_transaction_confirmed_data_form_dict = address_internal_transaction_confirmed_data.from_dict(address_internal_transaction_confirmed_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


