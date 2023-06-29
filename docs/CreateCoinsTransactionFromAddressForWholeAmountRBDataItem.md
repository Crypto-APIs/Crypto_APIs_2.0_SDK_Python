# CreateCoinsTransactionFromAddressForWholeAmountRBDataItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callback_secret_key** | **str** | Represents the Secret Key value provided by the customer. This field is used for security purposes during the callback notification, in order to prove the sender of the callback as Crypto APIs. For more information please see our [Documentation](https://developers.cryptoapis.io/technical-documentation/general-information/callbacks#callback-security). | [optional] 
**callback_url** | **str** | Represents the URL that is set by the customer where the callback will be received at. The callback notification will be received only if and when the event occurs. &#x60;We support ONLY httpS type of protocol&#x60;. | [optional] 
**fee_priority** | **str** | Represents the fee priority of the automation, whether it is \&quot;slow\&quot;, \&quot;standard\&quot; or \&quot;fast\&quot;. | 
**note** | **str** | Represents an optional note to add a free text in, explaining or providing additional detail on the transaction request. | [optional] 
**recipient_address** | **str** | Defines the specific recipient address for the transaction. | 

## Example

```python
from cryptoapis.models.create_coins_transaction_from_address_for_whole_amount_rb_data_item import CreateCoinsTransactionFromAddressForWholeAmountRBDataItem

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCoinsTransactionFromAddressForWholeAmountRBDataItem from a JSON string
create_coins_transaction_from_address_for_whole_amount_rb_data_item_instance = CreateCoinsTransactionFromAddressForWholeAmountRBDataItem.from_json(json)
# print the JSON string representation of the object
print CreateCoinsTransactionFromAddressForWholeAmountRBDataItem.to_json()

# convert the object into a dict
create_coins_transaction_from_address_for_whole_amount_rb_data_item_dict = create_coins_transaction_from_address_for_whole_amount_rb_data_item_instance.to_dict()
# create an instance of CreateCoinsTransactionFromAddressForWholeAmountRBDataItem from a dict
create_coins_transaction_from_address_for_whole_amount_rb_data_item_form_dict = create_coins_transaction_from_address_for_whole_amount_rb_data_item.from_dict(create_coins_transaction_from_address_for_whole_amount_rb_data_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


