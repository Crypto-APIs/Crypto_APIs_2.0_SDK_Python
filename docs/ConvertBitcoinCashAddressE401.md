# ConvertBitcoinCashAddressE401


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Specifies an error code, e.g. error 404. | 
**message** | **str** | Specifies the message of the error, i.e. why the error was returned, e.g. error 404 stands for “not found”. | 
**details** | [**List[BannedIpAddressDetailsInner]**](BannedIpAddressDetailsInner.md) |  | [optional] 

## Example

```python
from cryptoapis.models.convert_bitcoin_cash_address_e401 import ConvertBitcoinCashAddressE401

# TODO update the JSON string below
json = "{}"
# create an instance of ConvertBitcoinCashAddressE401 from a JSON string
convert_bitcoin_cash_address_e401_instance = ConvertBitcoinCashAddressE401.from_json(json)
# print the JSON string representation of the object
print ConvertBitcoinCashAddressE401.to_json()

# convert the object into a dict
convert_bitcoin_cash_address_e401_dict = convert_bitcoin_cash_address_e401_instance.to_dict()
# create an instance of ConvertBitcoinCashAddressE401 from a dict
convert_bitcoin_cash_address_e401_form_dict = convert_bitcoin_cash_address_e401.from_dict(convert_bitcoin_cash_address_e401_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


