# DeleteBlockchainEventSubscriptionR


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | Specifies the version of the API that incorporates this endpoint. | 
**request_id** | **str** | Defines the ID of the request. The &#x60;requestId&#x60; is generated by Crypto APIs and it&#39;s unique for every request. | 
**context** | **str** | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional] 
**data** | [**DeleteBlockchainEventSubscriptionRData**](DeleteBlockchainEventSubscriptionRData.md) |  | 

## Example

```python
from cryptoapis.models.delete_blockchain_event_subscription_r import DeleteBlockchainEventSubscriptionR

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteBlockchainEventSubscriptionR from a JSON string
delete_blockchain_event_subscription_r_instance = DeleteBlockchainEventSubscriptionR.from_json(json)
# print the JSON string representation of the object
print DeleteBlockchainEventSubscriptionR.to_json()

# convert the object into a dict
delete_blockchain_event_subscription_r_dict = delete_blockchain_event_subscription_r_instance.to_dict()
# create an instance of DeleteBlockchainEventSubscriptionR from a dict
delete_blockchain_event_subscription_r_form_dict = delete_blockchain_event_subscription_r.from_dict(delete_blockchain_event_subscription_r_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


