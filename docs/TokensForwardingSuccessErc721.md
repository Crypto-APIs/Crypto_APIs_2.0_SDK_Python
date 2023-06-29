# TokensForwardingSuccessErc721

ERC-721

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Specifies the name of the token. | 
**symbol** | **str** | Specifies an identifier of the token, where up to five alphanumeric characters can be used for it. | 
**token_id** | **str** | Specifies the ID of the token. | 
**contract_address** | **str** | Specifies the address of the contract. | 

## Example

```python
from cryptoapis.models.tokens_forwarding_success_erc721 import TokensForwardingSuccessErc721

# TODO update the JSON string below
json = "{}"
# create an instance of TokensForwardingSuccessErc721 from a JSON string
tokens_forwarding_success_erc721_instance = TokensForwardingSuccessErc721.from_json(json)
# print the JSON string representation of the object
print TokensForwardingSuccessErc721.to_json()

# convert the object into a dict
tokens_forwarding_success_erc721_dict = tokens_forwarding_success_erc721_instance.to_dict()
# create an instance of TokensForwardingSuccessErc721 from a dict
tokens_forwarding_success_erc721_form_dict = tokens_forwarding_success_erc721.from_dict(tokens_forwarding_success_erc721_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


