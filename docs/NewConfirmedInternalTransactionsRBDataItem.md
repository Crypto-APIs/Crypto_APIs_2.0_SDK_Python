# NewConfirmedInternalTransactionsRBDataItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Defines the specific address of the internal transaction. | 
**allow_duplicates** | **bool** | Flag that permits or denies creation of duplicates | [default to False]
**callback_secret_key** | **str** | Represents the Secret Key value provided by the customer. This field is used for security purposes during the callback notification, in order to prove the sender of the callback as Crypto APIs. For more information please see our [Documentation](https://developers.cryptoapis.io/technical-documentation/general-information/callbacks#callback-security). | 
**callback_url** | **str** | Represents the URL that is set by the customer where the callback will be received at. The callback notification will be received only if and when the event occurs. &#x60;We support ONLY httpS type of protocol&#x60;. | 
**receive_callback_on** | **int** | Represents the exact confirmation, on which the user wants to receive callback. | [optional] 

## Example

```python
from cryptoapis.models.new_confirmed_internal_transactions_rb_data_item import NewConfirmedInternalTransactionsRBDataItem

# TODO update the JSON string below
json = "{}"
# create an instance of NewConfirmedInternalTransactionsRBDataItem from a JSON string
new_confirmed_internal_transactions_rb_data_item_instance = NewConfirmedInternalTransactionsRBDataItem.from_json(json)
# print the JSON string representation of the object
print NewConfirmedInternalTransactionsRBDataItem.to_json()

# convert the object into a dict
new_confirmed_internal_transactions_rb_data_item_dict = new_confirmed_internal_transactions_rb_data_item_instance.to_dict()
# create an instance of NewConfirmedInternalTransactionsRBDataItem from a dict
new_confirmed_internal_transactions_rb_data_item_form_dict = new_confirmed_internal_transactions_rb_data_item.from_dict(new_confirmed_internal_transactions_rb_data_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


