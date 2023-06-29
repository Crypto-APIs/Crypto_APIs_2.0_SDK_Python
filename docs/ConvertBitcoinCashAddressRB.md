# ConvertBitcoinCashAddressRB


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **str** | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional] 
**data** | [**ConvertBitcoinCashAddressRBData**](ConvertBitcoinCashAddressRBData.md) |  | 

## Example

```python
from cryptoapis.models.convert_bitcoin_cash_address_rb import ConvertBitcoinCashAddressRB

# TODO update the JSON string below
json = "{}"
# create an instance of ConvertBitcoinCashAddressRB from a JSON string
convert_bitcoin_cash_address_rb_instance = ConvertBitcoinCashAddressRB.from_json(json)
# print the JSON string representation of the object
print ConvertBitcoinCashAddressRB.to_json()

# convert the object into a dict
convert_bitcoin_cash_address_rb_dict = convert_bitcoin_cash_address_rb_instance.to_dict()
# create an instance of ConvertBitcoinCashAddressRB from a dict
convert_bitcoin_cash_address_rb_form_dict = convert_bitcoin_cash_address_rb.from_dict(convert_bitcoin_cash_address_rb_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


