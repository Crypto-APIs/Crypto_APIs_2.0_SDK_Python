# DecodeRawTransactionHexRISBVinInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Represents the address which send/receive the amount. | [optional] 
**input_hash** | **str** | Represents the transaction inputs&#39; indentifier. | [optional] 
**output_index** | **int** | Represents the output of a transaction. | [optional] 
**script_sig** | [**DecodeRawTransactionHexRISBVinInnerScriptSig**](DecodeRawTransactionHexRISBVinInnerScriptSig.md) |  | 
**sequence** | **str** | Represents the script sequence number. | [optional] 
**txinwitness** | **List[str]** |  | [optional] 

## Example

```python
from cryptoapis.models.decode_raw_transaction_hex_risb_vin_inner import DecodeRawTransactionHexRISBVinInner

# TODO update the JSON string below
json = "{}"
# create an instance of DecodeRawTransactionHexRISBVinInner from a JSON string
decode_raw_transaction_hex_risb_vin_inner_instance = DecodeRawTransactionHexRISBVinInner.from_json(json)
# print the JSON string representation of the object
print DecodeRawTransactionHexRISBVinInner.to_json()

# convert the object into a dict
decode_raw_transaction_hex_risb_vin_inner_dict = decode_raw_transaction_hex_risb_vin_inner_instance.to_dict()
# create an instance of DecodeRawTransactionHexRISBVinInner from a dict
decode_raw_transaction_hex_risb_vin_inner_form_dict = decode_raw_transaction_hex_risb_vin_inner.from_dict(decode_raw_transaction_hex_risb_vin_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


