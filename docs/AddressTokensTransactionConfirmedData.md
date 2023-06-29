# AddressTokensTransactionConfirmedData

Specifies all data, as attributes, included into the callback notification, which depends on the `event`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product** | **str** | Represents the Crypto APIs 2.0 product which sends the callback. | 
**event** | **str** | Defines the specific event, for which a callback subscription is set. | 
**item** | [**AddressTokensTransactionConfirmedDataItem**](AddressTokensTransactionConfirmedDataItem.md) |  | 

## Example

```python
from cryptoapis.models.address_tokens_transaction_confirmed_data import AddressTokensTransactionConfirmedData

# TODO update the JSON string below
json = "{}"
# create an instance of AddressTokensTransactionConfirmedData from a JSON string
address_tokens_transaction_confirmed_data_instance = AddressTokensTransactionConfirmedData.from_json(json)
# print the JSON string representation of the object
print AddressTokensTransactionConfirmedData.to_json()

# convert the object into a dict
address_tokens_transaction_confirmed_data_dict = address_tokens_transaction_confirmed_data_instance.to_dict()
# create an instance of AddressTokensTransactionConfirmedData from a dict
address_tokens_transaction_confirmed_data_form_dict = address_tokens_transaction_confirmed_data.from_dict(address_tokens_transaction_confirmed_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


