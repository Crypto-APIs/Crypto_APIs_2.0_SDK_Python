# ListWalletTransactionsRI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | **str** | Defines the direction of the transaction, e.g. incoming. | 
**fee** | [**ListWalletTransactionsRIFee**](ListWalletTransactionsRIFee.md) |  | 
**fungible_tokens** | [**List[ListWalletTransactionsRIFungibleTokensInner]**](ListWalletTransactionsRIFungibleTokensInner.md) | Represents fungible tokens&#39;es detailed information | [optional] 
**internal_transactions** | [**List[ListWalletTransactionsRIInternalTransactionsInner]**](ListWalletTransactionsRIInternalTransactionsInner.md) |  | [optional] 
**non_fungible_tokens** | [**List[ListWalletTransactionsRINonFungibleTokensInner]**](ListWalletTransactionsRINonFungibleTokensInner.md) | Represents non-fungible tokens&#39;es detailed information. | [optional] 
**recipients** | [**List[ListWalletTransactionsRIRecipientsInner]**](ListWalletTransactionsRIRecipientsInner.md) | Represents a list of recipient addresses with the respective amounts. In account-based protocols like Ethereum there is only one address in this list. | 
**senders** | [**List[ListWalletTransactionsRISendersInner]**](ListWalletTransactionsRISendersInner.md) | Represents a list of sender addresses with the respective amounts. In account-based protocols like Ethereum there is only one address in this list. | 
**status** | **str** | Defines the status of the transaction, if it is confirmed or unconfirmed. | 
**timestamp** | **int** | Defines the exact date/time in Unix Timestamp when this transaction was mined, confirmed or first seen in Mempool, if it is unconfirmed. | 
**transaction_id** | **str** | Represents the unique TD of the transaction. | 
**value** | [**ListWalletTransactionsRIValue**](ListWalletTransactionsRIValue.md) |  | 

## Example

```python
from cryptoapis.models.list_wallet_transactions_ri import ListWalletTransactionsRI

# TODO update the JSON string below
json = "{}"
# create an instance of ListWalletTransactionsRI from a JSON string
list_wallet_transactions_ri_instance = ListWalletTransactionsRI.from_json(json)
# print the JSON string representation of the object
print ListWalletTransactionsRI.to_json()

# convert the object into a dict
list_wallet_transactions_ri_dict = list_wallet_transactions_ri_instance.to_dict()
# create an instance of ListWalletTransactionsRI from a dict
list_wallet_transactions_ri_form_dict = list_wallet_transactions_ri.from_dict(list_wallet_transactions_ri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


