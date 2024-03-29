# ActivateBlockchainEventSubscriptionRI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Represents the address of the transaction, per which the result is returned. | 
**blockchain** | **str** | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. | 
**callback_secret_key** | **str** | Represents the Secret Key value provided by the customer. This field is used for security purposes during the callback notification, in order to prove the sender of the callback as Crypto APIs. For more information please see our Documentation. | 
**callback_url** | **str** | Represents the URL that is set by the customer where the callback will be received at. The callback notification will be received only if and when the event occurs. &#x60;We support ONLY httpS type of protocol&#x60;. | 
**confirmations_count** | **int** | Represents the number of confirmations, i.e. the amount of blocks that have been built on top of this block. | 
**created_timestamp** | **int** | Defines the specific time/date when the subscription was created in Unix Timestamp. | 
**event_type** | **str** | Defines the type of the specific event available for the customer to subscribe to for callback notification. | 
**is_active** | **bool** | Defines whether the subscription is active or not. Set as boolean. | 
**network** | **str** | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. | 
**reference_id** | **str** | Represents a unique ID used to reference the specific callback subscription. | 
**transaction_id** | **str** | Represents the unique identification string that defines the transaction. | 

## Example

```python
from cryptoapis.models.activate_blockchain_event_subscription_ri import ActivateBlockchainEventSubscriptionRI

# TODO update the JSON string below
json = "{}"
# create an instance of ActivateBlockchainEventSubscriptionRI from a JSON string
activate_blockchain_event_subscription_ri_instance = ActivateBlockchainEventSubscriptionRI.from_json(json)
# print the JSON string representation of the object
print ActivateBlockchainEventSubscriptionRI.to_json()

# convert the object into a dict
activate_blockchain_event_subscription_ri_dict = activate_blockchain_event_subscription_ri_instance.to_dict()
# create an instance of ActivateBlockchainEventSubscriptionRI from a dict
activate_blockchain_event_subscription_ri_form_dict = activate_blockchain_event_subscription_ri.from_dict(activate_blockchain_event_subscription_ri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


