# TokensForwardingAutomationsLimitReached

tokens_forwarding_automations_limit_reached

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Specifies an error code, e.g. error 404. | 
**message** | **str** | Specifies the message of the error, i.e. why the error was returned, e.g. error 404 stands for “not found”. | 
**details** | [**List[BannedIpAddressDetailsInner]**](BannedIpAddressDetailsInner.md) |  | [optional] 

## Example

```python
from cryptoapis.models.tokens_forwarding_automations_limit_reached import TokensForwardingAutomationsLimitReached

# TODO update the JSON string below
json = "{}"
# create an instance of TokensForwardingAutomationsLimitReached from a JSON string
tokens_forwarding_automations_limit_reached_instance = TokensForwardingAutomationsLimitReached.from_json(json)
# print the JSON string representation of the object
print TokensForwardingAutomationsLimitReached.to_json()

# convert the object into a dict
tokens_forwarding_automations_limit_reached_dict = tokens_forwarding_automations_limit_reached_instance.to_dict()
# create an instance of TokensForwardingAutomationsLimitReached from a dict
tokens_forwarding_automations_limit_reached_form_dict = tokens_forwarding_automations_limit_reached.from_dict(tokens_forwarding_automations_limit_reached_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


