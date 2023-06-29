# ValidateAddressRB


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **str** | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional] 
**data** | [**ValidateAddressRBData**](ValidateAddressRBData.md) |  | 

## Example

```python
from cryptoapis.models.validate_address_rb import ValidateAddressRB

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateAddressRB from a JSON string
validate_address_rb_instance = ValidateAddressRB.from_json(json)
# print the JSON string representation of the object
print ValidateAddressRB.to_json()

# convert the object into a dict
validate_address_rb_dict = validate_address_rb_instance.to_dict()
# create an instance of ValidateAddressRB from a dict
validate_address_rb_form_dict = validate_address_rb.from_dict(validate_address_rb_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


