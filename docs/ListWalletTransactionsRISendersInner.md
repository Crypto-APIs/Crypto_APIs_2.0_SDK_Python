# ListWalletTransactionsRISendersInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Represents the address which sends this transaction. In UTXO-based protocols like Bitcoin there could be several senders while in account-based protocols like Ethereum there is always only one sender. | 
**amount** | **str** | Represents the total amount sent by this address including the fee. | 
**label** | **str** | Defines a plain text string as a label for the sender. | [optional] 

## Example

```python
from cryptoapis.models.list_wallet_transactions_ri_senders_inner import ListWalletTransactionsRISendersInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListWalletTransactionsRISendersInner from a JSON string
list_wallet_transactions_ri_senders_inner_instance = ListWalletTransactionsRISendersInner.from_json(json)
# print the JSON string representation of the object
print ListWalletTransactionsRISendersInner.to_json()

# convert the object into a dict
list_wallet_transactions_ri_senders_inner_dict = list_wallet_transactions_ri_senders_inner_instance.to_dict()
# create an instance of ListWalletTransactionsRISendersInner from a dict
list_wallet_transactions_ri_senders_inner_form_dict = list_wallet_transactions_ri_senders_inner.from_dict(list_wallet_transactions_ri_senders_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


