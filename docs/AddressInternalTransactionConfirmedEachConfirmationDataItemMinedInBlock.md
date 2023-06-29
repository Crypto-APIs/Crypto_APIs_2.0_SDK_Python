# AddressInternalTransactionConfirmedEachConfirmationDataItemMinedInBlock

Refers to the specific block the transaction was mined in.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**height** | **int** | Defines the number of blocks in the blockchain preceding this specific block. | 
**hash** | **str** | Represents the hash of the block&#39;s header, i.e. an output that has a fixed length. | 
**timestamp** | **int** | Defines the exact date/time when this transaction was mined in seconds since Unix Epoch time. | 

## Example

```python
from cryptoapis.models.address_internal_transaction_confirmed_each_confirmation_data_item_mined_in_block import AddressInternalTransactionConfirmedEachConfirmationDataItemMinedInBlock

# TODO update the JSON string below
json = "{}"
# create an instance of AddressInternalTransactionConfirmedEachConfirmationDataItemMinedInBlock from a JSON string
address_internal_transaction_confirmed_each_confirmation_data_item_mined_in_block_instance = AddressInternalTransactionConfirmedEachConfirmationDataItemMinedInBlock.from_json(json)
# print the JSON string representation of the object
print AddressInternalTransactionConfirmedEachConfirmationDataItemMinedInBlock.to_json()

# convert the object into a dict
address_internal_transaction_confirmed_each_confirmation_data_item_mined_in_block_dict = address_internal_transaction_confirmed_each_confirmation_data_item_mined_in_block_instance.to_dict()
# create an instance of AddressInternalTransactionConfirmedEachConfirmationDataItemMinedInBlock from a dict
address_internal_transaction_confirmed_each_confirmation_data_item_mined_in_block_form_dict = address_internal_transaction_confirmed_each_confirmation_data_item_mined_in_block.from_dict(address_internal_transaction_confirmed_each_confirmation_data_item_mined_in_block_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


