# ActivateBlockchainEventSubscriptionRB


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **str** | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional] 
**data** | [**ActivateBlockchainEventSubscriptionRBData**](ActivateBlockchainEventSubscriptionRBData.md) |  | 

## Example

```python
from cryptoapis.models.activate_blockchain_event_subscription_rb import ActivateBlockchainEventSubscriptionRB

# TODO update the JSON string below
json = "{}"
# create an instance of ActivateBlockchainEventSubscriptionRB from a JSON string
activate_blockchain_event_subscription_rb_instance = ActivateBlockchainEventSubscriptionRB.from_json(json)
# print the JSON string representation of the object
print ActivateBlockchainEventSubscriptionRB.to_json()

# convert the object into a dict
activate_blockchain_event_subscription_rb_dict = activate_blockchain_event_subscription_rb_instance.to_dict()
# create an instance of ActivateBlockchainEventSubscriptionRB from a dict
activate_blockchain_event_subscription_rb_form_dict = activate_blockchain_event_subscription_rb.from_dict(activate_blockchain_event_subscription_rb_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


