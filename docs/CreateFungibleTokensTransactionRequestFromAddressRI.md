# CreateFungibleTokensTransactionRequestFromAddressRI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callback_secret_key** | **str** | Represents the Secret Key value provided by the customer. This field is used for security purposes during the callback notification, in order to prove the sender of the callback as Crypto APIs. For more information please see our [Documentation](https://developers.cryptoapis.io/technical-documentation/general-information/callbacks#callback-security). | 
**callback_url** | **str** | Represents the URL that is set by the customer where the callback will be received at. The callback notification will be received only if and when the event occurs. &#x60;We support ONLY httpS type of protocol&#x60;. | 
**fee_priority** | **str** | Represents the fee priority of the automation, whether it is \&quot;slow\&quot;, \&quot;standard\&quot; or \&quot;fast\&quot;. | 
**note** | **str** | Represents an optional note to add a free text in, explaining or providing additional detail on the transaction request. | [optional] 
**recipients** | [**List[CreateFungibleTokensTransactionRequestFromAddressRIRecipientsInner]**](CreateFungibleTokensTransactionRequestFromAddressRIRecipientsInner.md) | Defines the destination for the transaction, i.e. the recipient(s). | 
**senders** | [**CreateCoinsTransactionRequestFromAddressRISenders**](CreateCoinsTransactionRequestFromAddressRISenders.md) |  | 
**token_type_specific_data** | [**CreateFungibleTokensTransactionRequestFromAddressRIS**](CreateFungibleTokensTransactionRequestFromAddressRIS.md) |  | 
**transaction_request_id** | **str** | Represents a unique identifier of the transaction request (the request sent to make a transaction), which helps in identifying which callback and which &#x60;referenceId&#x60; concern that specific transaction request. | 

## Example

```python
from cryptoapis.models.create_fungible_tokens_transaction_request_from_address_ri import CreateFungibleTokensTransactionRequestFromAddressRI

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFungibleTokensTransactionRequestFromAddressRI from a JSON string
create_fungible_tokens_transaction_request_from_address_ri_instance = CreateFungibleTokensTransactionRequestFromAddressRI.from_json(json)
# print the JSON string representation of the object
print CreateFungibleTokensTransactionRequestFromAddressRI.to_json()

# convert the object into a dict
create_fungible_tokens_transaction_request_from_address_ri_dict = create_fungible_tokens_transaction_request_from_address_ri_instance.to_dict()
# create an instance of CreateFungibleTokensTransactionRequestFromAddressRI from a dict
create_fungible_tokens_transaction_request_from_address_ri_form_dict = create_fungible_tokens_transaction_request_from_address_ri.from_dict(create_fungible_tokens_transaction_request_from_address_ri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


