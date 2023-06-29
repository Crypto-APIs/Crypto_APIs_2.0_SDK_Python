# ListXRPRippleTransactionsByBlockHeightRI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_data** | **str** |  | [optional] 
**destination_tag** | **int** |  | [optional] 
**index** | **int** |  | 
**mined_in_block_hash** | **str** |  | 
**recipients** | [**List[ListXRPRippleTransactionsByBlockHeightRIRecipientsInner]**](ListXRPRippleTransactionsByBlockHeightRIRecipientsInner.md) | Object Array representation of transaction receivers | 
**senders** | [**List[ListXRPRippleTransactionsByBlockHeightRISendersInner]**](ListXRPRippleTransactionsByBlockHeightRISendersInner.md) | Object Array representation of transaction senders | 
**sequence** | **int** |  | 
**status** | **str** |  | 
**timestamp** | **int** | Defines the exact date/time in Unix Timestamp when this transaction was mined, confirmed or first seen in Mempool, if it is unconfirmed. | 
**transaction_hash** | **str** |  | 
**type** | **str** |  | 
**fee** | [**ListXRPRippleTransactionsByBlockHeightRIFee**](ListXRPRippleTransactionsByBlockHeightRIFee.md) |  | 
**offer** | [**ListXRPRippleTransactionsByBlockHeightRIOffer**](ListXRPRippleTransactionsByBlockHeightRIOffer.md) |  | 
**receive** | [**ListXRPRippleTransactionsByBlockHeightRIReceive**](ListXRPRippleTransactionsByBlockHeightRIReceive.md) |  | 
**value** | [**ListXRPRippleTransactionsByBlockHeightRIValue**](ListXRPRippleTransactionsByBlockHeightRIValue.md) |  | 

## Example

```python
from cryptoapis.models.list_xrp_ripple_transactions_by_block_height_ri import ListXRPRippleTransactionsByBlockHeightRI

# TODO update the JSON string below
json = "{}"
# create an instance of ListXRPRippleTransactionsByBlockHeightRI from a JSON string
list_xrp_ripple_transactions_by_block_height_ri_instance = ListXRPRippleTransactionsByBlockHeightRI.from_json(json)
# print the JSON string representation of the object
print ListXRPRippleTransactionsByBlockHeightRI.to_json()

# convert the object into a dict
list_xrp_ripple_transactions_by_block_height_ri_dict = list_xrp_ripple_transactions_by_block_height_ri_instance.to_dict()
# create an instance of ListXRPRippleTransactionsByBlockHeightRI from a dict
list_xrp_ripple_transactions_by_block_height_ri_form_dict = list_xrp_ripple_transactions_by_block_height_ri.from_dict(list_xrp_ripple_transactions_by_block_height_ri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


