# DecodeRawTransactionHexRB


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **str** | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional] 
**data** | [**DecodeRawTransactionHexRBData**](DecodeRawTransactionHexRBData.md) |  | 

## Example

```python
from cryptoapis.models.decode_raw_transaction_hex_rb import DecodeRawTransactionHexRB

# TODO update the JSON string below
json = "{}"
# create an instance of DecodeRawTransactionHexRB from a JSON string
decode_raw_transaction_hex_rb_instance = DecodeRawTransactionHexRB.from_json(json)
# print the JSON string representation of the object
print DecodeRawTransactionHexRB.to_json()

# convert the object into a dict
decode_raw_transaction_hex_rb_dict = decode_raw_transaction_hex_rb_instance.to_dict()
# create an instance of DecodeRawTransactionHexRB from a dict
decode_raw_transaction_hex_rb_form_dict = decode_raw_transaction_hex_rb.from_dict(decode_raw_transaction_hex_rb_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


