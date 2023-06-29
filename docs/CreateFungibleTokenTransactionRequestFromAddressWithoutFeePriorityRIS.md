# CreateFungibleTokenTransactionRequestFromAddressWithoutFeePriorityRIS

Represents the specific token data which depends on its type - if it is a Coin or Token.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract_address** | **str** | Defines the contract address in the blockchain for an ERC20 token. | 
**fee_limit** | **str** | Defines the fee limit value. | 
**symbol** | **str** | Defines the Token symbol. | 

## Example

```python
from cryptoapis.models.create_fungible_token_transaction_request_from_address_without_fee_priority_ris import CreateFungibleTokenTransactionRequestFromAddressWithoutFeePriorityRIS

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFungibleTokenTransactionRequestFromAddressWithoutFeePriorityRIS from a JSON string
create_fungible_token_transaction_request_from_address_without_fee_priority_ris_instance = CreateFungibleTokenTransactionRequestFromAddressWithoutFeePriorityRIS.from_json(json)
# print the JSON string representation of the object
print CreateFungibleTokenTransactionRequestFromAddressWithoutFeePriorityRIS.to_json()

# convert the object into a dict
create_fungible_token_transaction_request_from_address_without_fee_priority_ris_dict = create_fungible_token_transaction_request_from_address_without_fee_priority_ris_instance.to_dict()
# create an instance of CreateFungibleTokenTransactionRequestFromAddressWithoutFeePriorityRIS from a dict
create_fungible_token_transaction_request_from_address_without_fee_priority_ris_form_dict = create_fungible_token_transaction_request_from_address_without_fee_priority_ris.from_dict(create_fungible_token_transaction_request_from_address_without_fee_priority_ris_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


