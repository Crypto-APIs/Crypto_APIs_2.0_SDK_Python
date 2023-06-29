# CoinsForwardingSuccessData

Specifies all data, as attributes, included into the callback notification, which depends on the `event`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product** | **str** | Represents the Crypto APIs 2.0 product which sends the callback. | 
**event** | **str** | Defines the specific event, for which a callback subscription is set. | 
**item** | [**CoinsForwardingSuccessDataItem**](CoinsForwardingSuccessDataItem.md) |  | 

## Example

```python
from cryptoapis.models.coins_forwarding_success_data import CoinsForwardingSuccessData

# TODO update the JSON string below
json = "{}"
# create an instance of CoinsForwardingSuccessData from a JSON string
coins_forwarding_success_data_instance = CoinsForwardingSuccessData.from_json(json)
# print the JSON string representation of the object
print CoinsForwardingSuccessData.to_json()

# convert the object into a dict
coins_forwarding_success_data_dict = coins_forwarding_success_data_instance.to_dict()
# create an instance of CoinsForwardingSuccessData from a dict
coins_forwarding_success_data_form_dict = coins_forwarding_success_data.from_dict(coins_forwarding_success_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


