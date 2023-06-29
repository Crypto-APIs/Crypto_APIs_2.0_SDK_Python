# GetBlockchainEventSubscriptionDetailsByReferenceIDE403


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Specifies an error code, e.g. error 404. | 
**message** | **str** | Specifies the message of the error, i.e. why the error was returned, e.g. error 404 stands for “not found”. | 
**details** | [**List[BannedIpAddressDetailsInner]**](BannedIpAddressDetailsInner.md) |  | [optional] 

## Example

```python
from cryptoapis.models.get_blockchain_event_subscription_details_by_reference_ide403 import GetBlockchainEventSubscriptionDetailsByReferenceIDE403

# TODO update the JSON string below
json = "{}"
# create an instance of GetBlockchainEventSubscriptionDetailsByReferenceIDE403 from a JSON string
get_blockchain_event_subscription_details_by_reference_ide403_instance = GetBlockchainEventSubscriptionDetailsByReferenceIDE403.from_json(json)
# print the JSON string representation of the object
print GetBlockchainEventSubscriptionDetailsByReferenceIDE403.to_json()

# convert the object into a dict
get_blockchain_event_subscription_details_by_reference_ide403_dict = get_blockchain_event_subscription_details_by_reference_ide403_instance.to_dict()
# create an instance of GetBlockchainEventSubscriptionDetailsByReferenceIDE403 from a dict
get_blockchain_event_subscription_details_by_reference_ide403_form_dict = get_blockchain_event_subscription_details_by_reference_ide403.from_dict(get_blockchain_event_subscription_details_by_reference_ide403_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


