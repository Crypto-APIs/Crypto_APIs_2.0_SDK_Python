# ListXRPRippleTransactionsByAddressAndTimeRangeRI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_tag** | **int** | A destination tag is a value used to discern the holder of the Ripple (XRP) being deposited or withdrawn. | [optional] 
**index** | **int** | Represents the index position of the transaction in the block. | 
**mined_in_block_hash** | **str** | Represents the hash of the block where this transaction was mined/confirmed for first time. The hash is defined as a cryptographic digital fingerprint made by hashing the block header twice through the SHA256 algorithm. | 
**mined_in_block_height** | **int** | Represents the hight of the block where this transaction was mined/confirmed for first time. The height is defined as the number of blocks in the blockchain preceding this specific block. | 
**recipients** | [**List[GetXRPRippleTransactionDetailsByTransactionIDRIRecipientsInner]**](GetXRPRippleTransactionDetailsByTransactionIDRIRecipientsInner.md) | Represents an object of addresses that receive the transactions. | 
**senders** | [**List[GetXRPRippleTransactionDetailsByTransactionIDRISendersInner]**](GetXRPRippleTransactionDetailsByTransactionIDRISendersInner.md) | Represents an object of addresses that provide the funds. | 
**sequence** | **int** | Defines the transaction input&#39;s sequence as an integer, which is is used when transactions are replaced with newer versions before LockTime. | 
**status** | **str** | Defines the status of the transaction. | 
**timestamp** | **int** | Defines the exact date/time in Unix Timestamp when this transaction was mined, confirmed or first seen in Mempool, if it is unconfirmed. | 
**transaction_hash** | **str** | Represents the hash of the XRP transaction. | 
**type** | **str** | Specifies the type of the transaction. | 
**fee** | [**ListXRPRippleTransactionsByAddressRIFee**](ListXRPRippleTransactionsByAddressRIFee.md) |  | 
**offer** | [**ListXRPRippleTransactionsByAddressRIOffer**](ListXRPRippleTransactionsByAddressRIOffer.md) |  | 
**receive** | [**ListXRPRippleTransactionsByAddressRIReceive**](ListXRPRippleTransactionsByAddressRIReceive.md) |  | 
**value** | [**ListXRPRippleTransactionsByAddressRIValue**](ListXRPRippleTransactionsByAddressRIValue.md) |  | 

## Example

```python
from cryptoapis.models.list_xrp_ripple_transactions_by_address_and_time_range_ri import ListXRPRippleTransactionsByAddressAndTimeRangeRI

# TODO update the JSON string below
json = "{}"
# create an instance of ListXRPRippleTransactionsByAddressAndTimeRangeRI from a JSON string
list_xrp_ripple_transactions_by_address_and_time_range_ri_instance = ListXRPRippleTransactionsByAddressAndTimeRangeRI.from_json(json)
# print the JSON string representation of the object
print ListXRPRippleTransactionsByAddressAndTimeRangeRI.to_json()

# convert the object into a dict
list_xrp_ripple_transactions_by_address_and_time_range_ri_dict = list_xrp_ripple_transactions_by_address_and_time_range_ri_instance.to_dict()
# create an instance of ListXRPRippleTransactionsByAddressAndTimeRangeRI from a dict
list_xrp_ripple_transactions_by_address_and_time_range_ri_form_dict = list_xrp_ripple_transactions_by_address_and_time_range_ri.from_dict(list_xrp_ripple_transactions_by_address_and_time_range_ri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


