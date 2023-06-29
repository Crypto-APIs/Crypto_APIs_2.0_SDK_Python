# CreateCoinsTransactionRequestFromWalletRBDataItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callback_secret_key** | **str** | Represents the Secret Key value provided by the customer. This field is used for security purposes during the callback notification, in order to prove the sender of the callback as Crypto APIs. For more information please see our [Documentation](https://developers.cryptoapis.io/technical-documentation/general-information/callbacks#callback-security). | [optional] 
**callback_url** | **str** | Represents the URL that is set by the customer where the callback will be received at. The callback notification will be received only if and when the event occurs. &#x60;We support ONLY httpS type of protocol&#x60;. | [optional] 
**fee_priority** | **str** | Represents the fee priority of the automation, whether it is \&quot;slow\&quot;, \&quot;standard\&quot; or \&quot;fast\&quot;. | 
**note** | **str** | Represents an optional note to add a free text in, explaining or providing additional detail on the transaction request. | [optional] 
**prepare_strategy** | **str** | Refers to a model of a UTXO spending strategy, where customers can choose how to spend their transaction outputs from multiple Bitcoin addresses. Two options available - \&quot;minimize-dust\&quot; (select lower amounts from multiple addresses) or \&quot;optimize-size\&quot; (select higher amounts from less addresses). | [optional] [default to 'minimize-dust']
**recipients** | [**List[CreateCoinsTransactionRequestFromWalletRBDataItemRecipientsInner]**](CreateCoinsTransactionRequestFromWalletRBDataItemRecipientsInner.md) | Defines the destination of the transaction, whether it is incoming or outgoing. | 

## Example

```python
from cryptoapis.models.create_coins_transaction_request_from_wallet_rb_data_item import CreateCoinsTransactionRequestFromWalletRBDataItem

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCoinsTransactionRequestFromWalletRBDataItem from a JSON string
create_coins_transaction_request_from_wallet_rb_data_item_instance = CreateCoinsTransactionRequestFromWalletRBDataItem.from_json(json)
# print the JSON string representation of the object
print CreateCoinsTransactionRequestFromWalletRBDataItem.to_json()

# convert the object into a dict
create_coins_transaction_request_from_wallet_rb_data_item_dict = create_coins_transaction_request_from_wallet_rb_data_item_instance.to_dict()
# create an instance of CreateCoinsTransactionRequestFromWalletRBDataItem from a dict
create_coins_transaction_request_from_wallet_rb_data_item_form_dict = create_coins_transaction_request_from_wallet_rb_data_item.from_dict(create_coins_transaction_request_from_wallet_rb_data_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


