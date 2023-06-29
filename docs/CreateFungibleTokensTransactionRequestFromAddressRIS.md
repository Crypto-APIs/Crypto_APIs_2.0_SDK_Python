# CreateFungibleTokensTransactionRequestFromAddressRIS

Represents the specific token data which depends on its type - if it is a Coin or Token.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract_address** | **str** | Defines the contract address in the blockchain for an ERC20 token. | 

## Example

```python
from cryptoapis.models.create_fungible_tokens_transaction_request_from_address_ris import CreateFungibleTokensTransactionRequestFromAddressRIS

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFungibleTokensTransactionRequestFromAddressRIS from a JSON string
create_fungible_tokens_transaction_request_from_address_ris_instance = CreateFungibleTokensTransactionRequestFromAddressRIS.from_json(json)
# print the JSON string representation of the object
print CreateFungibleTokensTransactionRequestFromAddressRIS.to_json()

# convert the object into a dict
create_fungible_tokens_transaction_request_from_address_ris_dict = create_fungible_tokens_transaction_request_from_address_ris_instance.to_dict()
# create an instance of CreateFungibleTokensTransactionRequestFromAddressRIS from a dict
create_fungible_tokens_transaction_request_from_address_ris_form_dict = create_fungible_tokens_transaction_request_from_address_ris.from_dict(create_fungible_tokens_transaction_request_from_address_ris_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


