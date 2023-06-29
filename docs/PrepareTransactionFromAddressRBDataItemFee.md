# PrepareTransactionFromAddressRBDataItemFee

Defines the amount of the transaction fee.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exact_amount** | **str** | String representation of the exact amount | [optional] 
**priority** | **str** | Enum representation of the fee priority | 
**substract_from_amount** | **bool** | Representation of the subtract from amount whether it is \&quot;true\&quot;,  or \&quot;false\&quot;. | [optional] 

## Example

```python
from cryptoapis.models.prepare_transaction_from_address_rb_data_item_fee import PrepareTransactionFromAddressRBDataItemFee

# TODO update the JSON string below
json = "{}"
# create an instance of PrepareTransactionFromAddressRBDataItemFee from a JSON string
prepare_transaction_from_address_rb_data_item_fee_instance = PrepareTransactionFromAddressRBDataItemFee.from_json(json)
# print the JSON string representation of the object
print PrepareTransactionFromAddressRBDataItemFee.to_json()

# convert the object into a dict
prepare_transaction_from_address_rb_data_item_fee_dict = prepare_transaction_from_address_rb_data_item_fee_instance.to_dict()
# create an instance of PrepareTransactionFromAddressRBDataItemFee from a dict
prepare_transaction_from_address_rb_data_item_fee_form_dict = prepare_transaction_from_address_rb_data_item_fee.from_dict(prepare_transaction_from_address_rb_data_item_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


