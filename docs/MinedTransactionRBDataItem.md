# MinedTransactionRBDataItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_duplicates** | **bool** | Specifies a flag that permits or denies the creation of duplicate addresses. | [optional] 
**callback_secret_key** | **str** | Represents the Secret Key value provided by the customer. This field is used for security purposes during the callback notification, in order to prove the sender of the callback as Crypto APIs. For more information please see our [Documentation](https://developers.cryptoapis.io/technical-documentation/general-information/callbacks#callback-security). | [optional] 
**callback_url** | **str** | Represents the URL that is set by the customer where the callback will be received at. The callback notification will be received only if and when the event occurs. &#x60;We support ONLY httpS type of protocol&#x60;. | 
**transaction_id** | **str** | Represents the unique identification string that defines the transaction. | 

## Example

```python
from cryptoapis.models.mined_transaction_rb_data_item import MinedTransactionRBDataItem

# TODO update the JSON string below
json = "{}"
# create an instance of MinedTransactionRBDataItem from a JSON string
mined_transaction_rb_data_item_instance = MinedTransactionRBDataItem.from_json(json)
# print the JSON string representation of the object
print MinedTransactionRBDataItem.to_json()

# convert the object into a dict
mined_transaction_rb_data_item_dict = mined_transaction_rb_data_item_instance.to_dict()
# create an instance of MinedTransactionRBDataItem from a dict
mined_transaction_rb_data_item_form_dict = mined_transaction_rb_data_item.from_dict(mined_transaction_rb_data_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


