# PrepareTransactionFromAddressRB


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **str** | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional] 
**data** | [**PrepareTransactionFromAddressRBData**](PrepareTransactionFromAddressRBData.md) |  | 

## Example

```python
from cryptoapis.models.prepare_transaction_from_address_rb import PrepareTransactionFromAddressRB

# TODO update the JSON string below
json = "{}"
# create an instance of PrepareTransactionFromAddressRB from a JSON string
prepare_transaction_from_address_rb_instance = PrepareTransactionFromAddressRB.from_json(json)
# print the JSON string representation of the object
print PrepareTransactionFromAddressRB.to_json()

# convert the object into a dict
prepare_transaction_from_address_rb_dict = prepare_transaction_from_address_rb_instance.to_dict()
# create an instance of PrepareTransactionFromAddressRB from a dict
prepare_transaction_from_address_rb_form_dict = prepare_transaction_from_address_rb.from_dict(prepare_transaction_from_address_rb_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


