# CreateFungibleTokensTransactionRequestFromAddressE401


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Specifies an error code, e.g. error 404. | 
**message** | **str** | Specifies the message of the error, i.e. why the error was returned, e.g. error 404 stands for “not found”. | 
**details** | [**List[BannedIpAddressDetailsInner]**](BannedIpAddressDetailsInner.md) |  | [optional] 

## Example

```python
from cryptoapis.models.create_fungible_tokens_transaction_request_from_address_e401 import CreateFungibleTokensTransactionRequestFromAddressE401

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFungibleTokensTransactionRequestFromAddressE401 from a JSON string
create_fungible_tokens_transaction_request_from_address_e401_instance = CreateFungibleTokensTransactionRequestFromAddressE401.from_json(json)
# print the JSON string representation of the object
print CreateFungibleTokensTransactionRequestFromAddressE401.to_json()

# convert the object into a dict
create_fungible_tokens_transaction_request_from_address_e401_dict = create_fungible_tokens_transaction_request_from_address_e401_instance.to_dict()
# create an instance of CreateFungibleTokensTransactionRequestFromAddressE401 from a dict
create_fungible_tokens_transaction_request_from_address_e401_form_dict = create_fungible_tokens_transaction_request_from_address_e401.from_dict(create_fungible_tokens_transaction_request_from_address_e401_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


