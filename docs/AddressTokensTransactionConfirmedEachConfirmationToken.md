# AddressTokensTransactionConfirmedEachConfirmationToken


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**symbol** | **str** |  | 
**decimals** | **str** |  | [optional] 
**amount** | **str** |  | 
**contract_address** | **str** |  | 
**token_id** | **str** |  | 
**property_id** | **str** | Defines the ID of the property for Omni Layer. | 
**transaction_type** | **str** | Defines the type of the transaction. | 
**created_by_transaction_id** | **str** | The transaction ID used to create the token. | 

## Example

```python
from cryptoapis.models.address_tokens_transaction_confirmed_each_confirmation_token import AddressTokensTransactionConfirmedEachConfirmationToken

# TODO update the JSON string below
json = "{}"
# create an instance of AddressTokensTransactionConfirmedEachConfirmationToken from a JSON string
address_tokens_transaction_confirmed_each_confirmation_token_instance = AddressTokensTransactionConfirmedEachConfirmationToken.from_json(json)
# print the JSON string representation of the object
print AddressTokensTransactionConfirmedEachConfirmationToken.to_json()

# convert the object into a dict
address_tokens_transaction_confirmed_each_confirmation_token_dict = address_tokens_transaction_confirmed_each_confirmation_token_instance.to_dict()
# create an instance of AddressTokensTransactionConfirmedEachConfirmationToken from a dict
address_tokens_transaction_confirmed_each_confirmation_token_form_dict = address_tokens_transaction_confirmed_each_confirmation_token.from_dict(address_tokens_transaction_confirmed_each_confirmation_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


