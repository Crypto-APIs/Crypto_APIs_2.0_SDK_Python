# DecodeRawTransactionHexRI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blockchain_speficic_data** | [**DecodeRawTransactionHexRIS**](DecodeRawTransactionHexRIS.md) |  | 
**size** | **int** | Represents the total size of this transaction. | 
**transaction_id** | **str** | Represents the decoded transaction hex. | 

## Example

```python
from cryptoapis.models.decode_raw_transaction_hex_ri import DecodeRawTransactionHexRI

# TODO update the JSON string below
json = "{}"
# create an instance of DecodeRawTransactionHexRI from a JSON string
decode_raw_transaction_hex_ri_instance = DecodeRawTransactionHexRI.from_json(json)
# print the JSON string representation of the object
print DecodeRawTransactionHexRI.to_json()

# convert the object into a dict
decode_raw_transaction_hex_ri_dict = decode_raw_transaction_hex_ri_instance.to_dict()
# create an instance of DecodeRawTransactionHexRI from a dict
decode_raw_transaction_hex_ri_form_dict = decode_raw_transaction_hex_ri.from_dict(decode_raw_transaction_hex_ri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


