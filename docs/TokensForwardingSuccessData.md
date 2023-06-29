# TokensForwardingSuccessData

Specifies all data, as attributes, included into the callback notification, which depends on the `event`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product** | **str** | Represents the Crypto APIs 2.0 product which sends the callback. | 
**event** | **str** | Defines the specific event, for which a callback subscription is set. | 
**item** | [**TokensForwardingSuccessDataItem**](TokensForwardingSuccessDataItem.md) |  | 

## Example

```python
from cryptoapis.models.tokens_forwarding_success_data import TokensForwardingSuccessData

# TODO update the JSON string below
json = "{}"
# create an instance of TokensForwardingSuccessData from a JSON string
tokens_forwarding_success_data_instance = TokensForwardingSuccessData.from_json(json)
# print the JSON string representation of the object
print TokensForwardingSuccessData.to_json()

# convert the object into a dict
tokens_forwarding_success_data_dict = tokens_forwarding_success_data_instance.to_dict()
# create an instance of TokensForwardingSuccessData from a dict
tokens_forwarding_success_data_form_dict = tokens_forwarding_success_data.from_dict(tokens_forwarding_success_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


