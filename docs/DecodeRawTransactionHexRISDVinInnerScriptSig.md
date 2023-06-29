# DecodeRawTransactionHexRISDVinInnerScriptSig

Specifies the required signatures.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asm** | **str** | The asm strands for assembly, which is the symbolic representation of the Bitcoin&#39;s Script language op-codes. | [optional] 
**hex** | **str** | Represents the hex of the public key of the address | [optional] 
**type** | **str** | Represents the script type of the reference transaction identifier | [optional] 

## Example

```python
from cryptoapis.models.decode_raw_transaction_hex_risd_vin_inner_script_sig import DecodeRawTransactionHexRISDVinInnerScriptSig

# TODO update the JSON string below
json = "{}"
# create an instance of DecodeRawTransactionHexRISDVinInnerScriptSig from a JSON string
decode_raw_transaction_hex_risd_vin_inner_script_sig_instance = DecodeRawTransactionHexRISDVinInnerScriptSig.from_json(json)
# print the JSON string representation of the object
print DecodeRawTransactionHexRISDVinInnerScriptSig.to_json()

# convert the object into a dict
decode_raw_transaction_hex_risd_vin_inner_script_sig_dict = decode_raw_transaction_hex_risd_vin_inner_script_sig_instance.to_dict()
# create an instance of DecodeRawTransactionHexRISDVinInnerScriptSig from a dict
decode_raw_transaction_hex_risd_vin_inner_script_sig_form_dict = decode_raw_transaction_hex_risd_vin_inner_script_sig.from_dict(decode_raw_transaction_hex_risd_vin_inner_script_sig_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


