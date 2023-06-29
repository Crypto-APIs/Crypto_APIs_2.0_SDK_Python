# DecodeRawTransactionHexRISZVoutInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**script_pub_key** | [**DecodeRawTransactionHexRISZVoutInnerScriptPubKey**](DecodeRawTransactionHexRISZVoutInnerScriptPubKey.md) |  | 
**value** | **str** | Defines the specific amount. | [optional] 

## Example

```python
from cryptoapis.models.decode_raw_transaction_hex_risz_vout_inner import DecodeRawTransactionHexRISZVoutInner

# TODO update the JSON string below
json = "{}"
# create an instance of DecodeRawTransactionHexRISZVoutInner from a JSON string
decode_raw_transaction_hex_risz_vout_inner_instance = DecodeRawTransactionHexRISZVoutInner.from_json(json)
# print the JSON string representation of the object
print DecodeRawTransactionHexRISZVoutInner.to_json()

# convert the object into a dict
decode_raw_transaction_hex_risz_vout_inner_dict = decode_raw_transaction_hex_risz_vout_inner_instance.to_dict()
# create an instance of DecodeRawTransactionHexRISZVoutInner from a dict
decode_raw_transaction_hex_risz_vout_inner_form_dict = decode_raw_transaction_hex_risz_vout_inner.from_dict(decode_raw_transaction_hex_risz_vout_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


