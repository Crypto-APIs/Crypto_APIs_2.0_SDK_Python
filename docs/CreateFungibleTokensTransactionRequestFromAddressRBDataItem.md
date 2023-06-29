# CreateFungibleTokensTransactionRequestFromAddressRBDataItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Represents the specific amount of the transaction. | 
**callback_secret_key** | **str** | Represents the Secret Key value provided by the customer. This field is used for security purposes during the callback notification, in order to prove the sender of the callback as Crypto APIs. For more information please see our [Documentation](https://developers.cryptoapis.io/technical-documentation/general-information/callbacks#callback-security). | [optional] 
**callback_url** | **str** | Represents the URL that is set by the customer where the callback will be received at. The callback notification will be received only if and when the event occurs. &#x60;We support ONLY httpS type of protocol&#x60;. | [optional] 
**fee_priority** | **str** | Represents the fee priority of the automation, whether it is \&quot;slow\&quot;, \&quot;standard\&quot; or \&quot;fast\&quot;. | 
**note** | **str** | Represents an optional note to add a free text in, explaining or providing additional detail on the transaction request. | [optional] 
**recipient_address** | **str** | Defines the specific recipient address for the transaction. | 
**token_identifier** | **str** | Defines the specific token identifier. For Bitcoin-based transactions it should be the &#x60;propertyId&#x60; and for Ethereum-based transactions - the &#x60;contract&#x60;. | 

## Example

```python
from cryptoapis.models.create_fungible_tokens_transaction_request_from_address_rb_data_item import CreateFungibleTokensTransactionRequestFromAddressRBDataItem

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFungibleTokensTransactionRequestFromAddressRBDataItem from a JSON string
create_fungible_tokens_transaction_request_from_address_rb_data_item_instance = CreateFungibleTokensTransactionRequestFromAddressRBDataItem.from_json(json)
# print the JSON string representation of the object
print CreateFungibleTokensTransactionRequestFromAddressRBDataItem.to_json()

# convert the object into a dict
create_fungible_tokens_transaction_request_from_address_rb_data_item_dict = create_fungible_tokens_transaction_request_from_address_rb_data_item_instance.to_dict()
# create an instance of CreateFungibleTokensTransactionRequestFromAddressRBDataItem from a dict
create_fungible_tokens_transaction_request_from_address_rb_data_item_form_dict = create_fungible_tokens_transaction_request_from_address_rb_data_item.from_dict(create_fungible_tokens_transaction_request_from_address_rb_data_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


