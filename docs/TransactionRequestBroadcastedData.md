# TransactionRequestBroadcastedData

Specifies all data, as attributes, included into the callback notification, which depends on the `event`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product** | **str** | Represents the Crypto APIs 2.0 product which sends the callback. | 
**event** | **str** | Defines the specific event, for which a callback subscription is set. | 
**item** | [**TransactionRequestBroadcastedDataItem**](TransactionRequestBroadcastedDataItem.md) |  | 

## Example

```python
from cryptoapis.models.transaction_request_broadcasted_data import TransactionRequestBroadcastedData

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionRequestBroadcastedData from a JSON string
transaction_request_broadcasted_data_instance = TransactionRequestBroadcastedData.from_json(json)
# print the JSON string representation of the object
print TransactionRequestBroadcastedData.to_json()

# convert the object into a dict
transaction_request_broadcasted_data_dict = transaction_request_broadcasted_data_instance.to_dict()
# create an instance of TransactionRequestBroadcastedData from a dict
transaction_request_broadcasted_data_form_dict = transaction_request_broadcasted_data.from_dict(transaction_request_broadcasted_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


