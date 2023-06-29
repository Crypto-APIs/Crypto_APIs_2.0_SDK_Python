# CreateSingleTransactionRequestFromAddressWithoutFeePriorityRBDataItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Represents the specific amount of the transaction&#39;s destination. | 
**callback_secret_key** | **str** | Represents the Secret Key value provided by the customer. This field is used for security purposes during the callback notification, in order to prove the sender of the callback as Crypto APIs. For more information please see our [Documentation](https://developers.cryptoapis.io/technical-documentation/general-information/callbacks#callback-security). | [optional] 
**callback_url** | **str** | Represents the URL that is set by the customer where the callback will be received at. The callback notification will be received only if and when the event occurs. &#x60;We support ONLY httpS type of protocol&#x60;. | [optional] 
**note** | **str** | Represents an optional note to add a free text in, explaining or providing additional detail on the transaction request. | [optional] 
**recipient_address** | **str** | Defines the specific recipient/destination address. | 

## Example

```python
from cryptoapis.models.create_single_transaction_request_from_address_without_fee_priority_rb_data_item import CreateSingleTransactionRequestFromAddressWithoutFeePriorityRBDataItem

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSingleTransactionRequestFromAddressWithoutFeePriorityRBDataItem from a JSON string
create_single_transaction_request_from_address_without_fee_priority_rb_data_item_instance = CreateSingleTransactionRequestFromAddressWithoutFeePriorityRBDataItem.from_json(json)
# print the JSON string representation of the object
print CreateSingleTransactionRequestFromAddressWithoutFeePriorityRBDataItem.to_json()

# convert the object into a dict
create_single_transaction_request_from_address_without_fee_priority_rb_data_item_dict = create_single_transaction_request_from_address_without_fee_priority_rb_data_item_instance.to_dict()
# create an instance of CreateSingleTransactionRequestFromAddressWithoutFeePriorityRBDataItem from a dict
create_single_transaction_request_from_address_without_fee_priority_rb_data_item_form_dict = create_single_transaction_request_from_address_without_fee_priority_rb_data_item.from_dict(create_single_transaction_request_from_address_without_fee_priority_rb_data_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


