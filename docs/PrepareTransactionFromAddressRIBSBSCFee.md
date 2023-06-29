# PrepareTransactionFromAddressRIBSBSCFee

Defines the amount of the transaction fee.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gas_limit** | **str** | Represents the amount of gas used by this specific transaction alone. | 
**gas_price** | **str** | Represents the price offered to the miner to purchase this amount of gas. | 

## Example

```python
from cryptoapis.models.prepare_transaction_from_address_ribsbsc_fee import PrepareTransactionFromAddressRIBSBSCFee

# TODO update the JSON string below
json = "{}"
# create an instance of PrepareTransactionFromAddressRIBSBSCFee from a JSON string
prepare_transaction_from_address_ribsbsc_fee_instance = PrepareTransactionFromAddressRIBSBSCFee.from_json(json)
# print the JSON string representation of the object
print PrepareTransactionFromAddressRIBSBSCFee.to_json()

# convert the object into a dict
prepare_transaction_from_address_ribsbsc_fee_dict = prepare_transaction_from_address_ribsbsc_fee_instance.to_dict()
# create an instance of PrepareTransactionFromAddressRIBSBSCFee from a dict
prepare_transaction_from_address_ribsbsc_fee_form_dict = prepare_transaction_from_address_ribsbsc_fee.from_dict(prepare_transaction_from_address_ribsbsc_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


