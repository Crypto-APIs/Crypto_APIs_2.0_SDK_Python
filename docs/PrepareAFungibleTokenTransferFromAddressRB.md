# PrepareAFungibleTokenTransferFromAddressRB


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **str** | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional] 
**data** | [**PrepareAFungibleTokenTransferFromAddressRBData**](PrepareAFungibleTokenTransferFromAddressRBData.md) |  | 

## Example

```python
from cryptoapis.models.prepare_a_fungible_token_transfer_from_address_rb import PrepareAFungibleTokenTransferFromAddressRB

# TODO update the JSON string below
json = "{}"
# create an instance of PrepareAFungibleTokenTransferFromAddressRB from a JSON string
prepare_a_fungible_token_transfer_from_address_rb_instance = PrepareAFungibleTokenTransferFromAddressRB.from_json(json)
# print the JSON string representation of the object
print PrepareAFungibleTokenTransferFromAddressRB.to_json()

# convert the object into a dict
prepare_a_fungible_token_transfer_from_address_rb_dict = prepare_a_fungible_token_transfer_from_address_rb_instance.to_dict()
# create an instance of PrepareAFungibleTokenTransferFromAddressRB from a dict
prepare_a_fungible_token_transfer_from_address_rb_form_dict = prepare_a_fungible_token_transfer_from_address_rb.from_dict(prepare_a_fungible_token_transfer_from_address_rb_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


