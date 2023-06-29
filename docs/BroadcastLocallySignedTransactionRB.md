# BroadcastLocallySignedTransactionRB


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **str** | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional] 
**data** | [**BroadcastLocallySignedTransactionRBData**](BroadcastLocallySignedTransactionRBData.md) |  | 

## Example

```python
from cryptoapis.models.broadcast_locally_signed_transaction_rb import BroadcastLocallySignedTransactionRB

# TODO update the JSON string below
json = "{}"
# create an instance of BroadcastLocallySignedTransactionRB from a JSON string
broadcast_locally_signed_transaction_rb_instance = BroadcastLocallySignedTransactionRB.from_json(json)
# print the JSON string representation of the object
print BroadcastLocallySignedTransactionRB.to_json()

# convert the object into a dict
broadcast_locally_signed_transaction_rb_dict = broadcast_locally_signed_transaction_rb_instance.to_dict()
# create an instance of BroadcastLocallySignedTransactionRB from a dict
broadcast_locally_signed_transaction_rb_form_dict = broadcast_locally_signed_transaction_rb.from_dict(broadcast_locally_signed_transaction_rb_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


