# BlockchainDataAddressEventSubscriptionNotFound

blockchain_data_address_event_subscription_not_found

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Specifies an error code, e.g. error 404. | 
**message** | **str** | Specifies the message of the error, i.e. why the error was returned, e.g. error 404 stands for “not found”. | 
**details** | [**List[BannedIpAddressDetailsInner]**](BannedIpAddressDetailsInner.md) |  | [optional] 

## Example

```python
from cryptoapis.models.blockchain_data_address_event_subscription_not_found import BlockchainDataAddressEventSubscriptionNotFound

# TODO update the JSON string below
json = "{}"
# create an instance of BlockchainDataAddressEventSubscriptionNotFound from a JSON string
blockchain_data_address_event_subscription_not_found_instance = BlockchainDataAddressEventSubscriptionNotFound.from_json(json)
# print the JSON string representation of the object
print BlockchainDataAddressEventSubscriptionNotFound.to_json()

# convert the object into a dict
blockchain_data_address_event_subscription_not_found_dict = blockchain_data_address_event_subscription_not_found_instance.to_dict()
# create an instance of BlockchainDataAddressEventSubscriptionNotFound from a dict
blockchain_data_address_event_subscription_not_found_form_dict = blockchain_data_address_event_subscription_not_found.from_dict(blockchain_data_address_event_subscription_not_found_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


