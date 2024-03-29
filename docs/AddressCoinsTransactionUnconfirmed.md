# AddressCoinsTransactionUnconfirmed


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | Specifies the version of the API that incorporates this endpoint. | 
**reference_id** | **str** | Represents a unique identifier that serves as reference to the specific request which prompts a callback, e.g. Blockchain Events Subscription, Blockchain Automation, etc. | 
**idempotency_key** | **str** | Specifies a unique ID generated by the system and attached to each callback. It is used by the server to recognize consecutive requests with the same data with the purpose not to perform the same operation twice. | 
**data** | [**AddressCoinsTransactionUnconfirmedData**](AddressCoinsTransactionUnconfirmedData.md) |  | 

## Example

```python
from cryptoapis.models.address_coins_transaction_unconfirmed import AddressCoinsTransactionUnconfirmed

# TODO update the JSON string below
json = "{}"
# create an instance of AddressCoinsTransactionUnconfirmed from a JSON string
address_coins_transaction_unconfirmed_instance = AddressCoinsTransactionUnconfirmed.from_json(json)
# print the JSON string representation of the object
print AddressCoinsTransactionUnconfirmed.to_json()

# convert the object into a dict
address_coins_transaction_unconfirmed_dict = address_coins_transaction_unconfirmed_instance.to_dict()
# create an instance of AddressCoinsTransactionUnconfirmed from a dict
address_coins_transaction_unconfirmed_form_dict = address_coins_transaction_unconfirmed.from_dict(address_coins_transaction_unconfirmed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


