# ListInternalTransactionsByAddressAndTimeRangeRI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Defines the specific amount of the transaction. | 
**mined_in_block_hash** | **str** | Represents the hash of the block where this transaction was mined/confirmed for first time. The hash is defined as a cryptographic digital fingerprint made by hashing the block header twice through the SHA256 algorithm. | 
**mined_in_block_height** | **int** | Represents the hight of the block where this transaction was mined/confirmed for first time. The height is defined as the number of blocks in the blockchain preceding this specific block. | 
**operation_id** | **str** | Represents the unique internal transaction ID in regards to the parent transaction (type trace address). | 
**operation_type** | **str** | Defines the call type of the internal transaction. | 
**parent_hash** | **str** | Defines the specific hash of the parent transaction. | 
**recipient** | **str** | Represents the recipient address with the respective amount. | 
**sender** | **str** | Represents the sender address with the respective amount. | 
**timestamp** | **int** |  | 

## Example

```python
from cryptoapis.models.list_internal_transactions_by_address_and_time_range_ri import ListInternalTransactionsByAddressAndTimeRangeRI

# TODO update the JSON string below
json = "{}"
# create an instance of ListInternalTransactionsByAddressAndTimeRangeRI from a JSON string
list_internal_transactions_by_address_and_time_range_ri_instance = ListInternalTransactionsByAddressAndTimeRangeRI.from_json(json)
# print the JSON string representation of the object
print ListInternalTransactionsByAddressAndTimeRangeRI.to_json()

# convert the object into a dict
list_internal_transactions_by_address_and_time_range_ri_dict = list_internal_transactions_by_address_and_time_range_ri_instance.to_dict()
# create an instance of ListInternalTransactionsByAddressAndTimeRangeRI from a dict
list_internal_transactions_by_address_and_time_range_ri_form_dict = list_internal_transactions_by_address_and_time_range_ri.from_dict(list_internal_transactions_by_address_and_time_range_ri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


