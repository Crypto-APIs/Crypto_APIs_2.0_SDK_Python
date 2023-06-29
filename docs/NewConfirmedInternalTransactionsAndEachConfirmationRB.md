# NewConfirmedInternalTransactionsAndEachConfirmationRB


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **str** | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional] 
**data** | [**NewConfirmedInternalTransactionsAndEachConfirmationRBData**](NewConfirmedInternalTransactionsAndEachConfirmationRBData.md) |  | 

## Example

```python
from cryptoapis.models.new_confirmed_internal_transactions_and_each_confirmation_rb import NewConfirmedInternalTransactionsAndEachConfirmationRB

# TODO update the JSON string below
json = "{}"
# create an instance of NewConfirmedInternalTransactionsAndEachConfirmationRB from a JSON string
new_confirmed_internal_transactions_and_each_confirmation_rb_instance = NewConfirmedInternalTransactionsAndEachConfirmationRB.from_json(json)
# print the JSON string representation of the object
print NewConfirmedInternalTransactionsAndEachConfirmationRB.to_json()

# convert the object into a dict
new_confirmed_internal_transactions_and_each_confirmation_rb_dict = new_confirmed_internal_transactions_and_each_confirmation_rb_instance.to_dict()
# create an instance of NewConfirmedInternalTransactionsAndEachConfirmationRB from a dict
new_confirmed_internal_transactions_and_each_confirmation_rb_form_dict = new_confirmed_internal_transactions_and_each_confirmation_rb.from_dict(new_confirmed_internal_transactions_and_each_confirmation_rb_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


