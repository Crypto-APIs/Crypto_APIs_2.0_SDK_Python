# DeleteAutomaticCoinsForwardingRI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callback_url** | **str** | Represents the URL that is set by the customer where the callback will be received at. The callback notification will be received only if and when the event occurs. &#x60;We support ONLY httpS type of protocol&#x60;. | 
**confirmations_count** | **int** | Represents the number of confirmations, i.e. the amount of blocks that have been built on top of this block. | 
**created_timestamp** | **int** | Defines the specific time/date when the automatic forwarding was created in Unix Timestamp. | 
**fee_priority** | **str** | Represents the fee priority of the automation, whether it is \&quot;SLOW\&quot;, \&quot;STANDARD\&quot; or \&quot;FAST\&quot;. | 
**from_address** | **str** | Represents the hash of the address that forwards the currency. | 
**minimum_transfer_amount** | **str** | Represents the minimum transfer amount of the currency in the &#x60;fromAddress&#x60; that can be allowed for an automatic forwarding. | 
**reference_id** | **str** | Represents a unique ID used to reference the specific callback subscription. | 
**to_address** | **str** | Represents the hash of the address the currency is forwarded to. | 

## Example

```python
from cryptoapis.models.delete_automatic_coins_forwarding_ri import DeleteAutomaticCoinsForwardingRI

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteAutomaticCoinsForwardingRI from a JSON string
delete_automatic_coins_forwarding_ri_instance = DeleteAutomaticCoinsForwardingRI.from_json(json)
# print the JSON string representation of the object
print DeleteAutomaticCoinsForwardingRI.to_json()

# convert the object into a dict
delete_automatic_coins_forwarding_ri_dict = delete_automatic_coins_forwarding_ri_instance.to_dict()
# create an instance of DeleteAutomaticCoinsForwardingRI from a dict
delete_automatic_coins_forwarding_ri_form_dict = delete_automatic_coins_forwarding_ri.from_dict(delete_automatic_coins_forwarding_ri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


