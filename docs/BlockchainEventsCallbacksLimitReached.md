# BlockchainEventsCallbacksLimitReached

blockchain_events_callbacks_limit_reached

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Specifies an error code, e.g. error 404. | 
**message** | **str** | Specifies the message of the error, i.e. why the error was returned, e.g. error 404 stands for “not found”. | 
**details** | [**List[BannedIpAddressDetailsInner]**](BannedIpAddressDetailsInner.md) |  | [optional] 

## Example

```python
from cryptoapis.models.blockchain_events_callbacks_limit_reached import BlockchainEventsCallbacksLimitReached

# TODO update the JSON string below
json = "{}"
# create an instance of BlockchainEventsCallbacksLimitReached from a JSON string
blockchain_events_callbacks_limit_reached_instance = BlockchainEventsCallbacksLimitReached.from_json(json)
# print the JSON string representation of the object
print BlockchainEventsCallbacksLimitReached.to_json()

# convert the object into a dict
blockchain_events_callbacks_limit_reached_dict = blockchain_events_callbacks_limit_reached_instance.to_dict()
# create an instance of BlockchainEventsCallbacksLimitReached from a dict
blockchain_events_callbacks_limit_reached_form_dict = blockchain_events_callbacks_limit_reached.from_dict(blockchain_events_callbacks_limit_reached_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


