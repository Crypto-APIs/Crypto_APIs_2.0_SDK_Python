# AddTokensToExistingFromAddressRB


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **str** | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional] 
**data** | [**AddTokensToExistingFromAddressRBData**](AddTokensToExistingFromAddressRBData.md) |  | 

## Example

```python
from cryptoapis.models.add_tokens_to_existing_from_address_rb import AddTokensToExistingFromAddressRB

# TODO update the JSON string below
json = "{}"
# create an instance of AddTokensToExistingFromAddressRB from a JSON string
add_tokens_to_existing_from_address_rb_instance = AddTokensToExistingFromAddressRB.from_json(json)
# print the JSON string representation of the object
print AddTokensToExistingFromAddressRB.to_json()

# convert the object into a dict
add_tokens_to_existing_from_address_rb_dict = add_tokens_to_existing_from_address_rb_instance.to_dict()
# create an instance of AddTokensToExistingFromAddressRB from a dict
add_tokens_to_existing_from_address_rb_form_dict = add_tokens_to_existing_from_address_rb.from_dict(add_tokens_to_existing_from_address_rb_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


