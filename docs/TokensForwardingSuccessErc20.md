# TokensForwardingSuccessErc20

ERC-20

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Specifies the name of the token. | 
**symbol** | **str** | Specifies an identifier of the token, where up to five alphanumeric characters can be used for it. | 
**decimals** | **str** | Defines how many decimals can be used to break the token. | [optional] 
**amount** | **str** | Defines the amount of tokens sent with the confirmed transaction. | 
**contract_address** | **str** | Defines the address of the contract. | 

## Example

```python
from cryptoapis.models.tokens_forwarding_success_erc20 import TokensForwardingSuccessErc20

# TODO update the JSON string below
json = "{}"
# create an instance of TokensForwardingSuccessErc20 from a JSON string
tokens_forwarding_success_erc20_instance = TokensForwardingSuccessErc20.from_json(json)
# print the JSON string representation of the object
print TokensForwardingSuccessErc20.to_json()

# convert the object into a dict
tokens_forwarding_success_erc20_dict = tokens_forwarding_success_erc20_instance.to_dict()
# create an instance of TokensForwardingSuccessErc20 from a dict
tokens_forwarding_success_erc20_form_dict = tokens_forwarding_success_erc20.from_dict(tokens_forwarding_success_erc20_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


