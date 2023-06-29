# CreateAutomaticTokensForwardingRBDataItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callback_secret_key** | **str** | Represents the Secret Key value provided by the customer. This field is used for security purposes during the callback notification, in order to prove the sender of the callback as Crypto APIs. For more information please see our [Documentation](https://developers.cryptoapis.io/technical-documentation/general-information/callbacks#callback-security). | [optional] 
**callback_url** | **str** | Represents the URL that is set by the customer where the callback will be received at. The callback notification will be received only if and when the event occurs. &#x60;We support ONLY httpS type of protocol&#x60;. | 
**confirmations_count** | **str** | Represents the number of confirmations, i.e. the amount of blocks that have been built on top of this block. | 
**fee_priority** | **str** | Represents the fee priority of the automation, whether it is \&quot;SLOW\&quot;, \&quot;STANDARD\&quot; or \&quot;FAST\&quot;. | 
**minimum_transfer_amount** | **str** | Represents the minimum transfer amount of the currency in the &#x60;fromAddress&#x60; that can be allowed for an automatic forwarding. | 
**to_address** | **str** | Represents the hash of the address the currency is forwarded to. | 
**token_data** | [**CreateAutomaticTokensForwardingRBTokenData**](CreateAutomaticTokensForwardingRBTokenData.md) |  | 

## Example

```python
from cryptoapis.models.create_automatic_tokens_forwarding_rb_data_item import CreateAutomaticTokensForwardingRBDataItem

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAutomaticTokensForwardingRBDataItem from a JSON string
create_automatic_tokens_forwarding_rb_data_item_instance = CreateAutomaticTokensForwardingRBDataItem.from_json(json)
# print the JSON string representation of the object
print CreateAutomaticTokensForwardingRBDataItem.to_json()

# convert the object into a dict
create_automatic_tokens_forwarding_rb_data_item_dict = create_automatic_tokens_forwarding_rb_data_item_instance.to_dict()
# create an instance of CreateAutomaticTokensForwardingRBDataItem from a dict
create_automatic_tokens_forwarding_rb_data_item_form_dict = create_automatic_tokens_forwarding_rb_data_item.from_dict(create_automatic_tokens_forwarding_rb_data_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


