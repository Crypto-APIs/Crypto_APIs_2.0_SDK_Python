# CreateCoinsTransactionRequestFromWalletRBDataItemRecipientsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Defines the specific recipient/destination address. | 
**amount** | **str** | Represents the specific amount of the transaction&#39;s destination. | 

## Example

```python
from cryptoapis.models.create_coins_transaction_request_from_wallet_rb_data_item_recipients_inner import CreateCoinsTransactionRequestFromWalletRBDataItemRecipientsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCoinsTransactionRequestFromWalletRBDataItemRecipientsInner from a JSON string
create_coins_transaction_request_from_wallet_rb_data_item_recipients_inner_instance = CreateCoinsTransactionRequestFromWalletRBDataItemRecipientsInner.from_json(json)
# print the JSON string representation of the object
print CreateCoinsTransactionRequestFromWalletRBDataItemRecipientsInner.to_json()

# convert the object into a dict
create_coins_transaction_request_from_wallet_rb_data_item_recipients_inner_dict = create_coins_transaction_request_from_wallet_rb_data_item_recipients_inner_instance.to_dict()
# create an instance of CreateCoinsTransactionRequestFromWalletRBDataItemRecipientsInner from a dict
create_coins_transaction_request_from_wallet_rb_data_item_recipients_inner_form_dict = create_coins_transaction_request_from_wallet_rb_data_item_recipients_inner.from_dict(create_coins_transaction_request_from_wallet_rb_data_item_recipients_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


