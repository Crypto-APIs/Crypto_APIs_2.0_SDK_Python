# DecodeRawTransactionHexRISZVoutInnerScriptPubKey

Represents the script public key.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Represents the address which send the amount. | [optional] 
**asm** | **str** | Represents the assembly of the script public key of the address. | [optional] 
**hex** | **str** | Represents the hex of the script public key of the address. | [optional] 
**type** | **str** | Represents the script type. | [optional] 

## Example

```python
from cryptoapis.models.decode_raw_transaction_hex_risz_vout_inner_script_pub_key import DecodeRawTransactionHexRISZVoutInnerScriptPubKey

# TODO update the JSON string below
json = "{}"
# create an instance of DecodeRawTransactionHexRISZVoutInnerScriptPubKey from a JSON string
decode_raw_transaction_hex_risz_vout_inner_script_pub_key_instance = DecodeRawTransactionHexRISZVoutInnerScriptPubKey.from_json(json)
# print the JSON string representation of the object
print DecodeRawTransactionHexRISZVoutInnerScriptPubKey.to_json()

# convert the object into a dict
decode_raw_transaction_hex_risz_vout_inner_script_pub_key_dict = decode_raw_transaction_hex_risz_vout_inner_script_pub_key_instance.to_dict()
# create an instance of DecodeRawTransactionHexRISZVoutInnerScriptPubKey from a dict
decode_raw_transaction_hex_risz_vout_inner_script_pub_key_form_dict = decode_raw_transaction_hex_risz_vout_inner_script_pub_key.from_dict(decode_raw_transaction_hex_risz_vout_inner_script_pub_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


