# BroadcastTransactionFailDataItem

Defines an `item` as one result.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blockchain** | **str** | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. | 
**network** | **str** | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot;, \&quot;rinkeby\&quot; are test networks. | 
**transaction_id** | **str** | Defines the unique ID of the specific transaction, i.e. its identification number. | 
**error_message** | **str** | Represents the error message received for the transaction. | 

## Example

```python
from cryptoapis.models.broadcast_transaction_fail_data_item import BroadcastTransactionFailDataItem

# TODO update the JSON string below
json = "{}"
# create an instance of BroadcastTransactionFailDataItem from a JSON string
broadcast_transaction_fail_data_item_instance = BroadcastTransactionFailDataItem.from_json(json)
# print the JSON string representation of the object
print BroadcastTransactionFailDataItem.to_json()

# convert the object into a dict
broadcast_transaction_fail_data_item_dict = broadcast_transaction_fail_data_item_instance.to_dict()
# create an instance of BroadcastTransactionFailDataItem from a dict
broadcast_transaction_fail_data_item_form_dict = broadcast_transaction_fail_data_item.from_dict(broadcast_transaction_fail_data_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


