# NewConfirmedCoinsTransactionsAndEachConfirmationRBDataItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Represents the address of the transaction, per which the result is returned. | 
**allow_duplicates** | **bool** | Specifies a flag that permits or denies the creation of duplicate addresses. | [optional] [default to False]
**callback_secret_key** | **str** | Represents the Secret Key value provided by the customer. This field is used for security purposes during the callback notification, in order to prove the sender of the callback as Crypto APIs. For more information please see our [Documentation](https://developers.cryptoapis.io/technical-documentation/general-information/callbacks#callback-security). | [optional] 
**callback_url** | **str** | Represents the URL that is set by the customer where the callback will be received at. The callback notification will be received only if and when the event occurs. &#x60;We support ONLY httpS type of protocol&#x60;. | 
**confirmations_count** | **int** | Represents the number of confirmations, i.e. the amount of blocks that have been built on top of this block. | 

## Example

```python
from cryptoapis.models.new_confirmed_coins_transactions_and_each_confirmation_rb_data_item import NewConfirmedCoinsTransactionsAndEachConfirmationRBDataItem

# TODO update the JSON string below
json = "{}"
# create an instance of NewConfirmedCoinsTransactionsAndEachConfirmationRBDataItem from a JSON string
new_confirmed_coins_transactions_and_each_confirmation_rb_data_item_instance = NewConfirmedCoinsTransactionsAndEachConfirmationRBDataItem.from_json(json)
# print the JSON string representation of the object
print NewConfirmedCoinsTransactionsAndEachConfirmationRBDataItem.to_json()

# convert the object into a dict
new_confirmed_coins_transactions_and_each_confirmation_rb_data_item_dict = new_confirmed_coins_transactions_and_each_confirmation_rb_data_item_instance.to_dict()
# create an instance of NewConfirmedCoinsTransactionsAndEachConfirmationRBDataItem from a dict
new_confirmed_coins_transactions_and_each_confirmation_rb_data_item_form_dict = new_confirmed_coins_transactions_and_each_confirmation_rb_data_item.from_dict(new_confirmed_coins_transactions_and_each_confirmation_rb_data_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


