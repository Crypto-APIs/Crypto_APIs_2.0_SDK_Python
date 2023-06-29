# PrepareTransactionFromAddressRIBS


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee** | [**PrepareTransactionFromAddressRIBSBSCFee**](PrepareTransactionFromAddressRIBSBSCFee.md) |  | 
**transaction_type** | **str** | Representation of the transaction type | 
**unit** | **str** | Represents the unit of the amount transacted. | 

## Example

```python
from cryptoapis.models.prepare_transaction_from_address_ribs import PrepareTransactionFromAddressRIBS

# TODO update the JSON string below
json = "{}"
# create an instance of PrepareTransactionFromAddressRIBS from a JSON string
prepare_transaction_from_address_ribs_instance = PrepareTransactionFromAddressRIBS.from_json(json)
# print the JSON string representation of the object
print PrepareTransactionFromAddressRIBS.to_json()

# convert the object into a dict
prepare_transaction_from_address_ribs_dict = prepare_transaction_from_address_ribs_instance.to_dict()
# create an instance of PrepareTransactionFromAddressRIBS from a dict
prepare_transaction_from_address_ribs_form_dict = prepare_transaction_from_address_ribs.from_dict(prepare_transaction_from_address_ribs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


