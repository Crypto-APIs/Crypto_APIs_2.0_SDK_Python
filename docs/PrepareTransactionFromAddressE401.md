# PrepareTransactionFromAddressE401


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Specifies an error code, e.g. error 404. | 
**message** | **str** | Specifies the message of the error, i.e. why the error was returned, e.g. error 404 stands for “not found”. | 
**details** | [**List[BannedIpAddressDetailsInner]**](BannedIpAddressDetailsInner.md) |  | [optional] 

## Example

```python
from cryptoapis.models.prepare_transaction_from_address_e401 import PrepareTransactionFromAddressE401

# TODO update the JSON string below
json = "{}"
# create an instance of PrepareTransactionFromAddressE401 from a JSON string
prepare_transaction_from_address_e401_instance = PrepareTransactionFromAddressE401.from_json(json)
# print the JSON string representation of the object
print PrepareTransactionFromAddressE401.to_json()

# convert the object into a dict
prepare_transaction_from_address_e401_dict = prepare_transaction_from_address_e401_instance.to_dict()
# create an instance of PrepareTransactionFromAddressE401 from a dict
prepare_transaction_from_address_e401_form_dict = prepare_transaction_from_address_e401.from_dict(prepare_transaction_from_address_e401_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


