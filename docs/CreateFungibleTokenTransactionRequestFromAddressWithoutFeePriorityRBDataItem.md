# CreateFungibleTokenTransactionRequestFromAddressWithoutFeePriorityRBDataItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Represents the specific amount of the transaction. | 
**callback_secret_key** | **str** | Represents the Secret Key value provided by the customer. This field is used for security purposes during the callback notification, in order to prove the sender of the callback as Crypto APIs. For more information please see our [Documentation](https://developers.cryptoapis.io/technical-documentation/general-information/callbacks#callback-security). | [optional] 
**callback_url** | **str** | Represents the URL that is set by the customer where the callback will be received at. The callback notification will be received only if and when the event occurs. &#x60;We support ONLY httpS type of protocol&#x60;. | [optional] 
**fee_limit** | **str** | Fee limit of the smart contract. If \&quot;OUT_OF_ENERGY\&quot; error appears - It is necessary to check whether the address of the calling contract has TRX and whether it is enough to pay for the burning energy or bandwidth cost, otherwise the address needs to obtain enough TRX. If there is enough TRX, the feeLimit set by the transaction is smaller, and it needs to be increased. | [optional] 
**note** | **str** | Represents an optional note to add a free text in, explaining or providing additional detail on the transaction request. | [optional] 
**recipient_address** | **str** | Defines the specific recipient address for the transaction. | 
**token_identifier** | **str** | Token identifier - for BITCOIN BASED should be property id e.g 31 for ETHEREUM BASED shoud be contract e.g 0xdac17f958d2ee523a2206206994597c13d831ec7 | 

## Example

```python
from cryptoapis.models.create_fungible_token_transaction_request_from_address_without_fee_priority_rb_data_item import CreateFungibleTokenTransactionRequestFromAddressWithoutFeePriorityRBDataItem

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFungibleTokenTransactionRequestFromAddressWithoutFeePriorityRBDataItem from a JSON string
create_fungible_token_transaction_request_from_address_without_fee_priority_rb_data_item_instance = CreateFungibleTokenTransactionRequestFromAddressWithoutFeePriorityRBDataItem.from_json(json)
# print the JSON string representation of the object
print CreateFungibleTokenTransactionRequestFromAddressWithoutFeePriorityRBDataItem.to_json()

# convert the object into a dict
create_fungible_token_transaction_request_from_address_without_fee_priority_rb_data_item_dict = create_fungible_token_transaction_request_from_address_without_fee_priority_rb_data_item_instance.to_dict()
# create an instance of CreateFungibleTokenTransactionRequestFromAddressWithoutFeePriorityRBDataItem from a dict
create_fungible_token_transaction_request_from_address_without_fee_priority_rb_data_item_form_dict = create_fungible_token_transaction_request_from_address_without_fee_priority_rb_data_item.from_dict(create_fungible_token_transaction_request_from_address_without_fee_priority_rb_data_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


