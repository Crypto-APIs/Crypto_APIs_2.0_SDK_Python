# ListWalletTransactionsRINonFungibleTokensInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**converted_amount** | **str** | Defines the tokens&#39; converted amount value. | 
**exchange_rate_unit** | **str** | Represents token&#39;s exchange rate unit. | 
**name** | **str** | Defines the token&#39;s name as a string. | 
**recipient** | **str** | Defines the address to which the recipient receives the transferred tokens. | 
**sender** | **str** | Defines the address from which the sender transfers tokens. | 
**symbol** | **str** | Defines the symbol of the non-fungible tokens. | 
**token_id** | **str** | Represents tokens&#39; unique identifier. | 
**type** | **str** | Defines the specific token type. | 

## Example

```python
from cryptoapis.models.list_wallet_transactions_ri_non_fungible_tokens_inner import ListWalletTransactionsRINonFungibleTokensInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListWalletTransactionsRINonFungibleTokensInner from a JSON string
list_wallet_transactions_ri_non_fungible_tokens_inner_instance = ListWalletTransactionsRINonFungibleTokensInner.from_json(json)
# print the JSON string representation of the object
print ListWalletTransactionsRINonFungibleTokensInner.to_json()

# convert the object into a dict
list_wallet_transactions_ri_non_fungible_tokens_inner_dict = list_wallet_transactions_ri_non_fungible_tokens_inner_instance.to_dict()
# create an instance of ListWalletTransactionsRINonFungibleTokensInner from a dict
list_wallet_transactions_ri_non_fungible_tokens_inner_form_dict = list_wallet_transactions_ri_non_fungible_tokens_inner.from_dict(list_wallet_transactions_ri_non_fungible_tokens_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


