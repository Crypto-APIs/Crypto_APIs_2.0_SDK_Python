# PrepareTransactionFromAddressRIBSE

Ethereum

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee** | [**PrepareTransactionFromAddressRIBSBSCFee**](PrepareTransactionFromAddressRIBSBSCFee.md) |  | 
**transaction_type** | **str** | Representation of the transaction type | 
**unit** | **str** | Represents the unit of the amount transacted. | 

## Example

```python
from cryptoapis.models.prepare_transaction_from_address_ribse import PrepareTransactionFromAddressRIBSE

# TODO update the JSON string below
json = "{}"
# create an instance of PrepareTransactionFromAddressRIBSE from a JSON string
prepare_transaction_from_address_ribse_instance = PrepareTransactionFromAddressRIBSE.from_json(json)
# print the JSON string representation of the object
print PrepareTransactionFromAddressRIBSE.to_json()

# convert the object into a dict
prepare_transaction_from_address_ribse_dict = prepare_transaction_from_address_ribse_instance.to_dict()
# create an instance of PrepareTransactionFromAddressRIBSE from a dict
prepare_transaction_from_address_ribse_form_dict = prepare_transaction_from_address_ribse.from_dict(prepare_transaction_from_address_ribse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


