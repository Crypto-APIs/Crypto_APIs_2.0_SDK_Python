# DeleteBlockchainEventSubscriptionE400


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Specifies an error code, e.g. error 404. | 
**message** | **str** | Specifies the message of the error, i.e. why the error was returned, e.g. error 404 stands for “not found”. | 
**details** | [**List[BannedIpAddressDetailsInner]**](BannedIpAddressDetailsInner.md) |  | [optional] 

## Example

```python
from cryptoapis.models.delete_blockchain_event_subscription_e400 import DeleteBlockchainEventSubscriptionE400

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteBlockchainEventSubscriptionE400 from a JSON string
delete_blockchain_event_subscription_e400_instance = DeleteBlockchainEventSubscriptionE400.from_json(json)
# print the JSON string representation of the object
print DeleteBlockchainEventSubscriptionE400.to_json()

# convert the object into a dict
delete_blockchain_event_subscription_e400_dict = delete_blockchain_event_subscription_e400_instance.to_dict()
# create an instance of DeleteBlockchainEventSubscriptionE400 from a dict
delete_blockchain_event_subscription_e400_form_dict = delete_blockchain_event_subscription_e400.from_dict(delete_blockchain_event_subscription_e400_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


