# ListConfirmedTransactionsByAddressAndTimeRangeE400


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Specifies an error code, e.g. error 404. | 
**message** | **str** | Specifies the message of the error, i.e. why the error was returned, e.g. error 404 stands for “not found”. | 
**details** | [**List[BannedIpAddressDetailsInner]**](BannedIpAddressDetailsInner.md) |  | [optional] 

## Example

```python
from cryptoapis.models.list_confirmed_transactions_by_address_and_time_range_e400 import ListConfirmedTransactionsByAddressAndTimeRangeE400

# TODO update the JSON string below
json = "{}"
# create an instance of ListConfirmedTransactionsByAddressAndTimeRangeE400 from a JSON string
list_confirmed_transactions_by_address_and_time_range_e400_instance = ListConfirmedTransactionsByAddressAndTimeRangeE400.from_json(json)
# print the JSON string representation of the object
print ListConfirmedTransactionsByAddressAndTimeRangeE400.to_json()

# convert the object into a dict
list_confirmed_transactions_by_address_and_time_range_e400_dict = list_confirmed_transactions_by_address_and_time_range_e400_instance.to_dict()
# create an instance of ListConfirmedTransactionsByAddressAndTimeRangeE400 from a dict
list_confirmed_transactions_by_address_and_time_range_e400_form_dict = list_confirmed_transactions_by_address_and_time_range_e400.from_dict(list_confirmed_transactions_by_address_and_time_range_e400_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


