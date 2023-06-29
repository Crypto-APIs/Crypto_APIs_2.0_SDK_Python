# AddressTokensTransactionConfirmedEachConfirmationErc721

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
from cryptoapis.models.address_tokens_transaction_confirmed_each_confirmation_erc721 import AddressTokensTransactionConfirmedEachConfirmationErc721

# TODO update the JSON string below
json = "{}"
# create an instance of AddressTokensTransactionConfirmedEachConfirmationErc721 from a JSON string
address_tokens_transaction_confirmed_each_confirmation_erc721_instance = AddressTokensTransactionConfirmedEachConfirmationErc721.from_json(json)
# print the JSON string representation of the object
print AddressTokensTransactionConfirmedEachConfirmationErc721.to_json()

# convert the object into a dict
address_tokens_transaction_confirmed_each_confirmation_erc721_dict = address_tokens_transaction_confirmed_each_confirmation_erc721_instance.to_dict()
# create an instance of AddressTokensTransactionConfirmedEachConfirmationErc721 from a dict
address_tokens_transaction_confirmed_each_confirmation_erc721_form_dict = address_tokens_transaction_confirmed_each_confirmation_erc721.from_dict(address_tokens_transaction_confirmed_each_confirmation_erc721_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


