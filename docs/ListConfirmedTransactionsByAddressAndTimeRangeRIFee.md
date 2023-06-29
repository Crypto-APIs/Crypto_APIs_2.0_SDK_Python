# ListConfirmedTransactionsByAddressAndTimeRangeRIFee


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Defines the amount of the transaction fee. | 
**unit** | **str** | Defines the specific unit of the fee. | 

## Example

```python
from cryptoapis.models.list_confirmed_transactions_by_address_and_time_range_ri_fee import ListConfirmedTransactionsByAddressAndTimeRangeRIFee

# TODO update the JSON string below
json = "{}"
# create an instance of ListConfirmedTransactionsByAddressAndTimeRangeRIFee from a JSON string
list_confirmed_transactions_by_address_and_time_range_ri_fee_instance = ListConfirmedTransactionsByAddressAndTimeRangeRIFee.from_json(json)
# print the JSON string representation of the object
print ListConfirmedTransactionsByAddressAndTimeRangeRIFee.to_json()

# convert the object into a dict
list_confirmed_transactions_by_address_and_time_range_ri_fee_dict = list_confirmed_transactions_by_address_and_time_range_ri_fee_instance.to_dict()
# create an instance of ListConfirmedTransactionsByAddressAndTimeRangeRIFee from a dict
list_confirmed_transactions_by_address_and_time_range_ri_fee_form_dict = list_confirmed_transactions_by_address_and_time_range_ri_fee.from_dict(list_confirmed_transactions_by_address_and_time_range_ri_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


