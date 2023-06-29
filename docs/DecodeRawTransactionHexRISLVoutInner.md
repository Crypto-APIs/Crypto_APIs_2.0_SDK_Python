# DecodeRawTransactionHexRISLVoutInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**script_pub_key** | [**DecodeRawTransactionHexRISLVoutInnerScriptPubKey**](DecodeRawTransactionHexRISLVoutInnerScriptPubKey.md) |  | 
**value** | **str** | Represents the sent/received amount. | [optional] 

## Example

```python
from cryptoapis.models.decode_raw_transaction_hex_risl_vout_inner import DecodeRawTransactionHexRISLVoutInner

# TODO update the JSON string below
json = "{}"
# create an instance of DecodeRawTransactionHexRISLVoutInner from a JSON string
decode_raw_transaction_hex_risl_vout_inner_instance = DecodeRawTransactionHexRISLVoutInner.from_json(json)
# print the JSON string representation of the object
print DecodeRawTransactionHexRISLVoutInner.to_json()

# convert the object into a dict
decode_raw_transaction_hex_risl_vout_inner_dict = decode_raw_transaction_hex_risl_vout_inner_instance.to_dict()
# create an instance of DecodeRawTransactionHexRISLVoutInner from a dict
decode_raw_transaction_hex_risl_vout_inner_form_dict = decode_raw_transaction_hex_risl_vout_inner.from_dict(decode_raw_transaction_hex_risl_vout_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


