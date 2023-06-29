# CreateCoinsTransactionFromAddressForWholeAmountRB


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **str** | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional] 
**data** | [**CreateCoinsTransactionFromAddressForWholeAmountRBData**](CreateCoinsTransactionFromAddressForWholeAmountRBData.md) |  | 

## Example

```python
from cryptoapis.models.create_coins_transaction_from_address_for_whole_amount_rb import CreateCoinsTransactionFromAddressForWholeAmountRB

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCoinsTransactionFromAddressForWholeAmountRB from a JSON string
create_coins_transaction_from_address_for_whole_amount_rb_instance = CreateCoinsTransactionFromAddressForWholeAmountRB.from_json(json)
# print the JSON string representation of the object
print CreateCoinsTransactionFromAddressForWholeAmountRB.to_json()

# convert the object into a dict
create_coins_transaction_from_address_for_whole_amount_rb_dict = create_coins_transaction_from_address_for_whole_amount_rb_instance.to_dict()
# create an instance of CreateCoinsTransactionFromAddressForWholeAmountRB from a dict
create_coins_transaction_from_address_for_whole_amount_rb_form_dict = create_coins_transaction_from_address_for_whole_amount_rb.from_dict(create_coins_transaction_from_address_for_whole_amount_rb_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


