# AddTokensToExistingFromAddressRI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callback_url** | **str** | Represents the URL that is set by the customer where the callback will be received at. The callback notification will be received only if and when the event occurs. &#x60;We support ONLY httpS type of protocol&#x60;. | 
**confirmations_count** | **int** | Represents the number of confirmations, i.e. the amount of blocks that have been built on top of this block. | 
**created_timestamp** | **int** | Defines the specific time/date when the automatic forwarding was created in Unix Timestamp. | 
**fee_address** | **str** | Represents the specific fee address, which is always automatically generated. Users must fund it. | 
**fee_priority** | **str** | Represents the fee priority of the automation, whether it is \&quot;SLOW\&quot;, \&quot;STANDARD\&quot; or \&quot;FAST\&quot;. | 
**from_address** | **str** | Represents the hash of the address that forwards the tokens. | 
**minimum_transfer_amount** | **str** | Represents the minimum transfer amount of the tokens in the &#x60;fromAddress&#x60; that can be allowed for an automatic forwarding. | 
**reference_id** | **str** | Represents a unique ID used to reference the specific callback subscription. | 
**to_address** | **str** | Represents the hash of the address the tokens are forwarded to. | 
**token_data** | [**AddTokensToExistingFromAddressRITS**](AddTokensToExistingFromAddressRITS.md) |  | 

## Example

```python
from cryptoapis.models.add_tokens_to_existing_from_address_ri import AddTokensToExistingFromAddressRI

# TODO update the JSON string below
json = "{}"
# create an instance of AddTokensToExistingFromAddressRI from a JSON string
add_tokens_to_existing_from_address_ri_instance = AddTokensToExistingFromAddressRI.from_json(json)
# print the JSON string representation of the object
print AddTokensToExistingFromAddressRI.to_json()

# convert the object into a dict
add_tokens_to_existing_from_address_ri_dict = add_tokens_to_existing_from_address_ri_instance.to_dict()
# create an instance of AddTokensToExistingFromAddressRI from a dict
add_tokens_to_existing_from_address_ri_form_dict = add_tokens_to_existing_from_address_ri.from_dict(add_tokens_to_existing_from_address_ri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


