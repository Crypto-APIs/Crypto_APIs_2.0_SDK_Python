# GenerateDepositAddressRB


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **str** | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional] 
**data** | [**GenerateDepositAddressRBData**](GenerateDepositAddressRBData.md) |  | 

## Example

```python
from cryptoapis.models.generate_deposit_address_rb import GenerateDepositAddressRB

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateDepositAddressRB from a JSON string
generate_deposit_address_rb_instance = GenerateDepositAddressRB.from_json(json)
# print the JSON string representation of the object
print GenerateDepositAddressRB.to_json()

# convert the object into a dict
generate_deposit_address_rb_dict = generate_deposit_address_rb_instance.to_dict()
# create an instance of GenerateDepositAddressRB from a dict
generate_deposit_address_rb_form_dict = generate_deposit_address_rb.from_dict(generate_deposit_address_rb_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


