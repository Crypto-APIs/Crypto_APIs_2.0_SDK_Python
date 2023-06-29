# DecodeRawTransactionHexE403


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Specifies an error code, e.g. error 404. | 
**message** | **str** | Specifies the message of the error, i.e. why the error was returned, e.g. error 404 stands for “not found”. | 
**details** | [**List[BannedIpAddressDetailsInner]**](BannedIpAddressDetailsInner.md) |  | [optional] 

## Example

```python
from cryptoapis.models.decode_raw_transaction_hex_e403 import DecodeRawTransactionHexE403

# TODO update the JSON string below
json = "{}"
# create an instance of DecodeRawTransactionHexE403 from a JSON string
decode_raw_transaction_hex_e403_instance = DecodeRawTransactionHexE403.from_json(json)
# print the JSON string representation of the object
print DecodeRawTransactionHexE403.to_json()

# convert the object into a dict
decode_raw_transaction_hex_e403_dict = decode_raw_transaction_hex_e403_instance.to_dict()
# create an instance of DecodeRawTransactionHexE403 from a dict
decode_raw_transaction_hex_e403_form_dict = decode_raw_transaction_hex_e403.from_dict(decode_raw_transaction_hex_e403_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


