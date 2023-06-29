# ListBlockchainEventsSubscriptionsRI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Represents the address of the transaction. | 
**callback_secret_key** | **str** | Represents the Secret Key value provided by the customer. This field is used for security purposes during the callback notification, in order to prove the sender of the callback as Crypto APIs. For more information please see our [Documentation](https://developers.cryptoapis.io/technical-documentation/general-information/callbacks#callback-security). | [optional] 
**callback_url** | **str** | Represents the URL that is set by the customer where the callback will be received at. The callback notification will be received only if and when the event occurs. &#x60;We support ONLY httpS type of protocol&#x60;. | 
**confirmations_count** | **int** | Represents the number of confirmations, i.e. the amount of blocks that have been built on top of this block. | 
**created_timestamp** | **int** | Defines the specific time/date when the subscription was created in Unix Timestamp. | 
**deactivation_reasons** | [**List[ListBlockchainEventsSubscriptionsRIDeactivationReasonsInner]**](ListBlockchainEventsSubscriptionsRIDeactivationReasonsInner.md) | Represents the deactivation reason details, available when a blockchain event subscription has status isActive - false. | [optional] 
**event_type** | **str** | Defines the type of the specific event available for the customer to subscribe to for callback notification. | 
**is_active** | **bool** | Defines whether the subscription is active or not. Set as boolean. | 
**reference_id** | **str** | Represents a unique ID used to reference the specific callback subscription. | 
**transaction_id** | **str** | Represents the unique identification string that defines the transaction. | [optional] 

## Example

```python
from cryptoapis.models.list_blockchain_events_subscriptions_ri import ListBlockchainEventsSubscriptionsRI

# TODO update the JSON string below
json = "{}"
# create an instance of ListBlockchainEventsSubscriptionsRI from a JSON string
list_blockchain_events_subscriptions_ri_instance = ListBlockchainEventsSubscriptionsRI.from_json(json)
# print the JSON string representation of the object
print ListBlockchainEventsSubscriptionsRI.to_json()

# convert the object into a dict
list_blockchain_events_subscriptions_ri_dict = list_blockchain_events_subscriptions_ri_instance.to_dict()
# create an instance of ListBlockchainEventsSubscriptionsRI from a dict
list_blockchain_events_subscriptions_ri_form_dict = list_blockchain_events_subscriptions_ri.from_dict(list_blockchain_events_subscriptions_ri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


