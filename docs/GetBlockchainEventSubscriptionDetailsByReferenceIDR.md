# GetBlockchainEventSubscriptionDetailsByReferenceIDR


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | Specifies the version of the API that incorporates this endpoint. | 
**request_id** | **str** | Defines the ID of the request. The &#x60;requestId&#x60; is generated by Crypto APIs and it&#39;s unique for every request. | 
**context** | **str** | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional] 
**data** | [**GetBlockchainEventSubscriptionDetailsByReferenceIDRData**](GetBlockchainEventSubscriptionDetailsByReferenceIDRData.md) |  | 

## Example

```python
from cryptoapis.models.get_blockchain_event_subscription_details_by_reference_idr import GetBlockchainEventSubscriptionDetailsByReferenceIDR

# TODO update the JSON string below
json = "{}"
# create an instance of GetBlockchainEventSubscriptionDetailsByReferenceIDR from a JSON string
get_blockchain_event_subscription_details_by_reference_idr_instance = GetBlockchainEventSubscriptionDetailsByReferenceIDR.from_json(json)
# print the JSON string representation of the object
print GetBlockchainEventSubscriptionDetailsByReferenceIDR.to_json()

# convert the object into a dict
get_blockchain_event_subscription_details_by_reference_idr_dict = get_blockchain_event_subscription_details_by_reference_idr_instance.to_dict()
# create an instance of GetBlockchainEventSubscriptionDetailsByReferenceIDR from a dict
get_blockchain_event_subscription_details_by_reference_idr_form_dict = get_blockchain_event_subscription_details_by_reference_idr.from_dict(get_blockchain_event_subscription_details_by_reference_idr_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


