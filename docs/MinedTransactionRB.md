# MinedTransactionRB


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **str** | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional] 
**data** | [**MinedTransactionRBData**](MinedTransactionRBData.md) |  | 

## Example

```python
from cryptoapis.models.mined_transaction_rb import MinedTransactionRB

# TODO update the JSON string below
json = "{}"
# create an instance of MinedTransactionRB from a JSON string
mined_transaction_rb_instance = MinedTransactionRB.from_json(json)
# print the JSON string representation of the object
print MinedTransactionRB.to_json()

# convert the object into a dict
mined_transaction_rb_dict = mined_transaction_rb_instance.to_dict()
# create an instance of MinedTransactionRB from a dict
mined_transaction_rb_form_dict = mined_transaction_rb.from_dict(mined_transaction_rb_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


