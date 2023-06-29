# DecodeRawTransactionHexRISD2VoutInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**script_pub_key** | [**DecodeRawTransactionHexRISD2VoutInnerScriptPubKey**](DecodeRawTransactionHexRISD2VoutInnerScriptPubKey.md) |  | 
**value** | **str** | Represents the sent/received amount. | [optional] 

## Example

```python
from cryptoapis.models.decode_raw_transaction_hex_risd2_vout_inner import DecodeRawTransactionHexRISD2VoutInner

# TODO update the JSON string below
json = "{}"
# create an instance of DecodeRawTransactionHexRISD2VoutInner from a JSON string
decode_raw_transaction_hex_risd2_vout_inner_instance = DecodeRawTransactionHexRISD2VoutInner.from_json(json)
# print the JSON string representation of the object
print DecodeRawTransactionHexRISD2VoutInner.to_json()

# convert the object into a dict
decode_raw_transaction_hex_risd2_vout_inner_dict = decode_raw_transaction_hex_risd2_vout_inner_instance.to_dict()
# create an instance of DecodeRawTransactionHexRISD2VoutInner from a dict
decode_raw_transaction_hex_risd2_vout_inner_form_dict = decode_raw_transaction_hex_risd2_vout_inner.from_dict(decode_raw_transaction_hex_risd2_vout_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


