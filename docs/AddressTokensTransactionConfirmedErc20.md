# AddressTokensTransactionConfirmedErc20

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
from cryptoapis.models.address_tokens_transaction_confirmed_erc20 import AddressTokensTransactionConfirmedErc20

# TODO update the JSON string below
json = "{}"
# create an instance of AddressTokensTransactionConfirmedErc20 from a JSON string
address_tokens_transaction_confirmed_erc20_instance = AddressTokensTransactionConfirmedErc20.from_json(json)
# print the JSON string representation of the object
print AddressTokensTransactionConfirmedErc20.to_json()

# convert the object into a dict
address_tokens_transaction_confirmed_erc20_dict = address_tokens_transaction_confirmed_erc20_instance.to_dict()
# create an instance of AddressTokensTransactionConfirmedErc20 from a dict
address_tokens_transaction_confirmed_erc20_form_dict = address_tokens_transaction_confirmed_erc20.from_dict(address_tokens_transaction_confirmed_erc20_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


