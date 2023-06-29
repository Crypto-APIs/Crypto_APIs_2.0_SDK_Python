# AddressTokensTransactionUnconfirmedToken


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Specifies the name of the token. | 
**symbol** | **str** | Specifies an identifier of the token, where up to five alphanumeric characters can be used for it. | 
**decimals** | **str** | Defines how many decimals can be used to break the token. | [optional] 
**amount** | **str** | Defines the amount of tokens sent with the transaction that is pending confirmation. | 
**contract_address** | **str** | Specifies the address of the contract. | 
**token_id** | **str** | Specifies the unique ID of the token. | 
**property_id** | **str** | Defines the ID of the property for Omni Layer. | 
**transaction_type** | **str** | Defines the type of the transaction made. | 
**created_by_transaction_id** | **str** | The transaction ID used to create the token. | 

## Example

```python
from cryptoapis.models.address_tokens_transaction_unconfirmed_token import AddressTokensTransactionUnconfirmedToken

# TODO update the JSON string below
json = "{}"
# create an instance of AddressTokensTransactionUnconfirmedToken from a JSON string
address_tokens_transaction_unconfirmed_token_instance = AddressTokensTransactionUnconfirmedToken.from_json(json)
# print the JSON string representation of the object
print AddressTokensTransactionUnconfirmedToken.to_json()

# convert the object into a dict
address_tokens_transaction_unconfirmed_token_dict = address_tokens_transaction_unconfirmed_token_instance.to_dict()
# create an instance of AddressTokensTransactionUnconfirmedToken from a dict
address_tokens_transaction_unconfirmed_token_form_dict = address_tokens_transaction_unconfirmed_token.from_dict(address_tokens_transaction_unconfirmed_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


