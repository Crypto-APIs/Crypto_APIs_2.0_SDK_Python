# ListWalletTransactionsRIRecipientsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The address which receives this transaction. In UTXO-based protocols like Bitcoin there could be several senders while in account-based protocols like Ethereum there is always only one recipient. | 
**amount** | **str** | Represents the amount received to this address. | 
**label** | **str** | Defines a plain text string as a label for the recipient. | [optional] 

## Example

```python
from cryptoapis.models.list_wallet_transactions_ri_recipients_inner import ListWalletTransactionsRIRecipientsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListWalletTransactionsRIRecipientsInner from a JSON string
list_wallet_transactions_ri_recipients_inner_instance = ListWalletTransactionsRIRecipientsInner.from_json(json)
# print the JSON string representation of the object
print ListWalletTransactionsRIRecipientsInner.to_json()

# convert the object into a dict
list_wallet_transactions_ri_recipients_inner_dict = list_wallet_transactions_ri_recipients_inner_instance.to_dict()
# create an instance of ListWalletTransactionsRIRecipientsInner from a dict
list_wallet_transactions_ri_recipients_inner_form_dict = list_wallet_transactions_ri_recipients_inner.from_dict(list_wallet_transactions_ri_recipients_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


