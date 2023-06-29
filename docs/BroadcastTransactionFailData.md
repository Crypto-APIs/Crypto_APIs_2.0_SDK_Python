# BroadcastTransactionFailData

Specifies all data, as attributes, included into the callback notification, which depends on the `event`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product** | **str** | Represents the Crypto APIs 2.0 product which sends the callback. | 
**event** | **str** | Defines the specific event, for which a callback subscription is set. | 
**item** | [**BroadcastTransactionFailDataItem**](BroadcastTransactionFailDataItem.md) |  | 

## Example

```python
from cryptoapis.models.broadcast_transaction_fail_data import BroadcastTransactionFailData

# TODO update the JSON string below
json = "{}"
# create an instance of BroadcastTransactionFailData from a JSON string
broadcast_transaction_fail_data_instance = BroadcastTransactionFailData.from_json(json)
# print the JSON string representation of the object
print BroadcastTransactionFailData.to_json()

# convert the object into a dict
broadcast_transaction_fail_data_dict = broadcast_transaction_fail_data_instance.to_dict()
# create an instance of BroadcastTransactionFailData from a dict
broadcast_transaction_fail_data_form_dict = broadcast_transaction_fail_data.from_dict(broadcast_transaction_fail_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


