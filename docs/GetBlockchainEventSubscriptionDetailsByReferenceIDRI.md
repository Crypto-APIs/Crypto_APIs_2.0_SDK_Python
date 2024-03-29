# GetBlockchainEventSubscriptionDetailsByReferenceIDRI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Represents the address of the transaction. | [optional] 
**blockchain** | **str** | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. | 
**callback_secret_key** | **str** | Represents the Secret Key value provided by the customer. This field is used for security purposes during the callback notification, in order to prove the sender of the callback as Crypto APIs. For more information please see our [Documentation](https://developers.cryptoapis.io/technical-documentation/general-information/callbacks#callback-security). | [optional] 
**callback_url** | **str** | Represents the URL that is set by the customer where the callback will be received at. The callback notification will be received only if and when the event occurs. | 
**confirmations_count** | **int** | Represents the number of confirmations, i.e. the amount of blocks that have been built on top of this block. | [optional] 
**created_timestamp** | **int** | Defines the specific time/date when the subscription was created in Unix Timestamp. | 
**deactivation_reasons** | [**List[ListBlockchainEventsSubscriptionsRIDeactivationReasonsInner]**](ListBlockchainEventsSubscriptionsRIDeactivationReasonsInner.md) | Represents the deactivation reason details, available when a blockchain event subscription has status isActive - false. | [optional] 
**event_type** | **str** | Defines the type of the specific event available for the customer to subscribe to for callback notification. | 
**is_active** | **bool** | Defines whether the subscription is active or not. Set as boolean. | 
**network** | **str** | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot; are test networks. | 
**reference_id** | **str** | Represents a unique ID used to reference the specific callback subscription. | 
**transaction_id** | **str** | Represents the unique identification string that defines the transaction. | [optional] 

## Example

```python
from cryptoapis.models.get_blockchain_event_subscription_details_by_reference_idri import GetBlockchainEventSubscriptionDetailsByReferenceIDRI

# TODO update the JSON string below
json = "{}"
# create an instance of GetBlockchainEventSubscriptionDetailsByReferenceIDRI from a JSON string
get_blockchain_event_subscription_details_by_reference_idri_instance = GetBlockchainEventSubscriptionDetailsByReferenceIDRI.from_json(json)
# print the JSON string representation of the object
print GetBlockchainEventSubscriptionDetailsByReferenceIDRI.to_json()

# convert the object into a dict
get_blockchain_event_subscription_details_by_reference_idri_dict = get_blockchain_event_subscription_details_by_reference_idri_instance.to_dict()
# create an instance of GetBlockchainEventSubscriptionDetailsByReferenceIDRI from a dict
get_blockchain_event_subscription_details_by_reference_idri_form_dict = get_blockchain_event_subscription_details_by_reference_idri.from_dict(get_blockchain_event_subscription_details_by_reference_idri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


