# CreateCoinsTransactionRequestFromAddressRB


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **str** | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional] 
**data** | [**CreateCoinsTransactionRequestFromAddressRBData**](CreateCoinsTransactionRequestFromAddressRBData.md) |  | 

## Example

```python
from cryptoapis.models.create_coins_transaction_request_from_address_rb import CreateCoinsTransactionRequestFromAddressRB

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCoinsTransactionRequestFromAddressRB from a JSON string
create_coins_transaction_request_from_address_rb_instance = CreateCoinsTransactionRequestFromAddressRB.from_json(json)
# print the JSON string representation of the object
print CreateCoinsTransactionRequestFromAddressRB.to_json()

# convert the object into a dict
create_coins_transaction_request_from_address_rb_dict = create_coins_transaction_request_from_address_rb_instance.to_dict()
# create an instance of CreateCoinsTransactionRequestFromAddressRB from a dict
create_coins_transaction_request_from_address_rb_form_dict = create_coins_transaction_request_from_address_rb.from_dict(create_coins_transaction_request_from_address_rb_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


