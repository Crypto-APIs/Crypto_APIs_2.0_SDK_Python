# TransactionRequestFailDataItem

Defines an `item` as one result.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blockchain** | **str** | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. | 
**network** | **str** | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;goerli\&quot;, \&quot;mordor\&quot; are test networks. | 
**required_approvals** | **int** | The required number of approvals needed to approve the transaction. | 
**required_rejections** | **int** | The required number of rejections needed to reject the transaction. | 
**current_approvals** | **int** | The current number of approvals given for the transaction. | 
**current_rejections** | **int** | The current number of rejections given for the transaction. | 
**error_message** | **str** | Represents the error message received for the transaction. | 

## Example

```python
from cryptoapis.models.transaction_request_fail_data_item import TransactionRequestFailDataItem

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionRequestFailDataItem from a JSON string
transaction_request_fail_data_item_instance = TransactionRequestFailDataItem.from_json(json)
# print the JSON string representation of the object
print TransactionRequestFailDataItem.to_json()

# convert the object into a dict
transaction_request_fail_data_item_dict = transaction_request_fail_data_item_instance.to_dict()
# create an instance of TransactionRequestFailDataItem from a dict
transaction_request_fail_data_item_form_dict = transaction_request_fail_data_item.from_dict(transaction_request_fail_data_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


