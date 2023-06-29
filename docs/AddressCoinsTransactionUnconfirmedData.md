# AddressCoinsTransactionUnconfirmedData

Specifies all data, as attributes, included into the callback notification, which depends on the `event`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product** | **str** | Represents the Crypto APIs 2.0 product which sends the callback. | 
**event** | **str** | Defines the specific event, for which a callback subscription is set. | 
**item** | [**AddressCoinsTransactionUnconfirmedDataItem**](AddressCoinsTransactionUnconfirmedDataItem.md) |  | 

## Example

```python
from cryptoapis.models.address_coins_transaction_unconfirmed_data import AddressCoinsTransactionUnconfirmedData

# TODO update the JSON string below
json = "{}"
# create an instance of AddressCoinsTransactionUnconfirmedData from a JSON string
address_coins_transaction_unconfirmed_data_instance = AddressCoinsTransactionUnconfirmedData.from_json(json)
# print the JSON string representation of the object
print AddressCoinsTransactionUnconfirmedData.to_json()

# convert the object into a dict
address_coins_transaction_unconfirmed_data_dict = address_coins_transaction_unconfirmed_data_instance.to_dict()
# create an instance of AddressCoinsTransactionUnconfirmedData from a dict
address_coins_transaction_unconfirmed_data_form_dict = address_coins_transaction_unconfirmed_data.from_dict(address_coins_transaction_unconfirmed_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


