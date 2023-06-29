# ListConfirmedTransactionsByAddressRIFee


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Defines the amount of the transaction fee. | 
**unit** | **str** | Represents the unit of the fee | 

## Example

```python
from cryptoapis.models.list_confirmed_transactions_by_address_ri_fee import ListConfirmedTransactionsByAddressRIFee

# TODO update the JSON string below
json = "{}"
# create an instance of ListConfirmedTransactionsByAddressRIFee from a JSON string
list_confirmed_transactions_by_address_ri_fee_instance = ListConfirmedTransactionsByAddressRIFee.from_json(json)
# print the JSON string representation of the object
print ListConfirmedTransactionsByAddressRIFee.to_json()

# convert the object into a dict
list_confirmed_transactions_by_address_ri_fee_dict = list_confirmed_transactions_by_address_ri_fee_instance.to_dict()
# create an instance of ListConfirmedTransactionsByAddressRIFee from a dict
list_confirmed_transactions_by_address_ri_fee_form_dict = list_confirmed_transactions_by_address_ri_fee.from_dict(list_confirmed_transactions_by_address_ri_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


