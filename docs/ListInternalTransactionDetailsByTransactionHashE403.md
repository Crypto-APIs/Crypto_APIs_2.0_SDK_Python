# ListInternalTransactionDetailsByTransactionHashE403


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Specifies an error code, e.g. error 404. | 
**message** | **str** | Specifies the message of the error, i.e. why the error was returned, e.g. error 404 stands for “not found”. | 
**details** | [**List[BannedIpAddressDetailsInner]**](BannedIpAddressDetailsInner.md) |  | [optional] 

## Example

```python
from cryptoapis.models.list_internal_transaction_details_by_transaction_hash_e403 import ListInternalTransactionDetailsByTransactionHashE403

# TODO update the JSON string below
json = "{}"
# create an instance of ListInternalTransactionDetailsByTransactionHashE403 from a JSON string
list_internal_transaction_details_by_transaction_hash_e403_instance = ListInternalTransactionDetailsByTransactionHashE403.from_json(json)
# print the JSON string representation of the object
print ListInternalTransactionDetailsByTransactionHashE403.to_json()

# convert the object into a dict
list_internal_transaction_details_by_transaction_hash_e403_dict = list_internal_transaction_details_by_transaction_hash_e403_instance.to_dict()
# create an instance of ListInternalTransactionDetailsByTransactionHashE403 from a dict
list_internal_transaction_details_by_transaction_hash_e403_form_dict = list_internal_transaction_details_by_transaction_hash_e403.from_dict(list_internal_transaction_details_by_transaction_hash_e403_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


