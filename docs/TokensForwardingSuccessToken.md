# TokensForwardingSuccessToken


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Specifies the name of the token. | 
**symbol** | **str** | Specifies an identifier of the token, where up to five alphanumeric characters can be used for it. | 
**decimals** | **str** | Defines how many decimals can be used to break the token. | [optional] 
**amount** | **str** | Defines the amount of tokens sent with the confirmed transaction. | 
**contract_address** | **str** | Specifies the address of the contract. | 
**token_id** | **str** | Specifies the ID of the token. | 
**property_id** | **str** | Defines the ID of the property for Omni Layer. | 
**transaction_type** | **str** | Defines the type of the transaction. | 
**created_by_transaction_id** | **str** | The transaction ID used to create the token. | 

## Example

```python
from cryptoapis.models.tokens_forwarding_success_token import TokensForwardingSuccessToken

# TODO update the JSON string below
json = "{}"
# create an instance of TokensForwardingSuccessToken from a JSON string
tokens_forwarding_success_token_instance = TokensForwardingSuccessToken.from_json(json)
# print the JSON string representation of the object
print TokensForwardingSuccessToken.to_json()

# convert the object into a dict
tokens_forwarding_success_token_dict = tokens_forwarding_success_token_instance.to_dict()
# create an instance of TokensForwardingSuccessToken from a dict
tokens_forwarding_success_token_form_dict = tokens_forwarding_success_token.from_dict(tokens_forwarding_success_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


