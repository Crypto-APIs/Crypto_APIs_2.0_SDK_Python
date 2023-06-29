# CoinsForwardingAutomationsLimitReached

coins_forwarding_automations_limit_reached

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Specifies an error code, e.g. error 404. | 
**message** | **str** | Specifies the message of the error, i.e. why the error was returned, e.g. error 404 stands for “not found”. | 
**details** | [**List[BannedIpAddressDetailsInner]**](BannedIpAddressDetailsInner.md) |  | [optional] 

## Example

```python
from cryptoapis.models.coins_forwarding_automations_limit_reached import CoinsForwardingAutomationsLimitReached

# TODO update the JSON string below
json = "{}"
# create an instance of CoinsForwardingAutomationsLimitReached from a JSON string
coins_forwarding_automations_limit_reached_instance = CoinsForwardingAutomationsLimitReached.from_json(json)
# print the JSON string representation of the object
print CoinsForwardingAutomationsLimitReached.to_json()

# convert the object into a dict
coins_forwarding_automations_limit_reached_dict = coins_forwarding_automations_limit_reached_instance.to_dict()
# create an instance of CoinsForwardingAutomationsLimitReached from a dict
coins_forwarding_automations_limit_reached_form_dict = coins_forwarding_automations_limit_reached.from_dict(coins_forwarding_automations_limit_reached_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


