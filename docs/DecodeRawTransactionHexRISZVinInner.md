# DecodeRawTransactionHexRISZVinInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Represents the addresses which send/receive the amount. | [optional] 
**input_hash** | **str** | Represents the transaction inputs&#39; indentifier. | [optional] 
**output_index** | **str** | Defines the output index of a transaction. | [optional] 
**script_sig** | [**DecodeRawTransactionHexRISZVinInnerScriptSig**](DecodeRawTransactionHexRISZVinInnerScriptSig.md) |  | 
**sequence** | **str** | Represents the script sequence number. | [optional] 

## Example

```python
from cryptoapis.models.decode_raw_transaction_hex_risz_vin_inner import DecodeRawTransactionHexRISZVinInner

# TODO update the JSON string below
json = "{}"
# create an instance of DecodeRawTransactionHexRISZVinInner from a JSON string
decode_raw_transaction_hex_risz_vin_inner_instance = DecodeRawTransactionHexRISZVinInner.from_json(json)
# print the JSON string representation of the object
print DecodeRawTransactionHexRISZVinInner.to_json()

# convert the object into a dict
decode_raw_transaction_hex_risz_vin_inner_dict = decode_raw_transaction_hex_risz_vin_inner_instance.to_dict()
# create an instance of DecodeRawTransactionHexRISZVinInner from a dict
decode_raw_transaction_hex_risz_vin_inner_form_dict = decode_raw_transaction_hex_risz_vin_inner.from_dict(decode_raw_transaction_hex_risz_vin_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


