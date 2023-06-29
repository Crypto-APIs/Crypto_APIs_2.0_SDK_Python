# AddressInternalTransactionConfirmedEachConfirmationDataItem

Defines an `item` as one result.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blockchain** | **str** | Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc. | 
**network** | **str** | Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \&quot;mainnet\&quot; is the live network with actual data while networks like \&quot;testnet\&quot;, \&quot;ropsten\&quot;, \&quot;rinkeby\&quot; are test networks. | 
**address** | **str** | Defines the specific address of the internal transaction. | 
**mined_in_block** | [**AddressInternalTransactionConfirmedEachConfirmationDataItemMinedInBlock**](AddressInternalTransactionConfirmedEachConfirmationDataItemMinedInBlock.md) |  | 
**parent_transaction_id** | **str** | Defines the Parent Transaction&#39;s unique ID. | 
**operation_id** | **str** | Defines the specific operation&#39;s unique ID. | 
**current_confirmations** | **int** | Defines the number of currently received confirmations for the transaction. | 
**target_confirmations** | **int** | Defines the number of confirmation transactions requested as callbacks, i.e. the system can notify till the n-th confirmation. | 
**amount** | **str** | Defines the amount of coins sent with the confirmed transaction. | 
**unit** | **str** | Defines the unit of the transaction, e.g. Gwei. | 
**direction** | **str** | Defines whether the transaction is \&quot;incoming\&quot; or \&quot;outgoing\&quot;. | 

## Example

```python
from cryptoapis.models.address_internal_transaction_confirmed_each_confirmation_data_item import AddressInternalTransactionConfirmedEachConfirmationDataItem

# TODO update the JSON string below
json = "{}"
# create an instance of AddressInternalTransactionConfirmedEachConfirmationDataItem from a JSON string
address_internal_transaction_confirmed_each_confirmation_data_item_instance = AddressInternalTransactionConfirmedEachConfirmationDataItem.from_json(json)
# print the JSON string representation of the object
print AddressInternalTransactionConfirmedEachConfirmationDataItem.to_json()

# convert the object into a dict
address_internal_transaction_confirmed_each_confirmation_data_item_dict = address_internal_transaction_confirmed_each_confirmation_data_item_instance.to_dict()
# create an instance of AddressInternalTransactionConfirmedEachConfirmationDataItem from a dict
address_internal_transaction_confirmed_each_confirmation_data_item_form_dict = address_internal_transaction_confirmed_each_confirmation_data_item.from_dict(address_internal_transaction_confirmed_each_confirmation_data_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


