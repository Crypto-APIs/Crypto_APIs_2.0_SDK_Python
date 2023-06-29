# ListWalletTransactionsRIFungibleTokensInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Defines the amount of the fungible tokens. | 
**converted_amount** | **str** | Defines the tokens&#39; converted amount value. | 
**exchange_rate_unit** | **str** | Represents token&#39;s exchange rate unit. | 
**name** | **str** | Defines the token&#39;s name as a string. | 
**recipient** | **str** | The address which receives this transaction. In UTXO-based protocols like Bitcoin there could be several senders while in account-based protocols like Ethereum there is always only one | 
**sender** | **str** | Represents the address which sends this transaction. In UTXO-based protocols like Bitcoin there could be several senders while in account-based protocols like Ethereum there is always only one sender. | 
**symbol** | **str** | Defines the symbol of the fungible tokens. | 
**token_decimals** | **int** | Defines the decimals of the token, i.e. the number of digits that come after the decimal coma of the token. | 
**type** | **str** | Defines the specific token type. | 

## Example

```python
from cryptoapis.models.list_wallet_transactions_ri_fungible_tokens_inner import ListWalletTransactionsRIFungibleTokensInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListWalletTransactionsRIFungibleTokensInner from a JSON string
list_wallet_transactions_ri_fungible_tokens_inner_instance = ListWalletTransactionsRIFungibleTokensInner.from_json(json)
# print the JSON string representation of the object
print ListWalletTransactionsRIFungibleTokensInner.to_json()

# convert the object into a dict
list_wallet_transactions_ri_fungible_tokens_inner_dict = list_wallet_transactions_ri_fungible_tokens_inner_instance.to_dict()
# create an instance of ListWalletTransactionsRIFungibleTokensInner from a dict
list_wallet_transactions_ri_fungible_tokens_inner_form_dict = list_wallet_transactions_ri_fungible_tokens_inner.from_dict(list_wallet_transactions_ri_fungible_tokens_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


