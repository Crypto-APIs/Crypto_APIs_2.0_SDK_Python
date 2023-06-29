# ListConfirmedTransactionsByAddressRISendersInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Represents the address which sends this transaction. In UTXO-based protocols like Bitcoin there could be several senders while in account-based protocols like Ethereum there is always only one sender. | 
**amount** | **str** | Represents the total amount sent by this address including the fee | 

## Example

```python
from cryptoapis.models.list_confirmed_transactions_by_address_ri_senders_inner import ListConfirmedTransactionsByAddressRISendersInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListConfirmedTransactionsByAddressRISendersInner from a JSON string
list_confirmed_transactions_by_address_ri_senders_inner_instance = ListConfirmedTransactionsByAddressRISendersInner.from_json(json)
# print the JSON string representation of the object
print ListConfirmedTransactionsByAddressRISendersInner.to_json()

# convert the object into a dict
list_confirmed_transactions_by_address_ri_senders_inner_dict = list_confirmed_transactions_by_address_ri_senders_inner_instance.to_dict()
# create an instance of ListConfirmedTransactionsByAddressRISendersInner from a dict
list_confirmed_transactions_by_address_ri_senders_inner_form_dict = list_confirmed_transactions_by_address_ri_senders_inner.from_dict(list_confirmed_transactions_by_address_ri_senders_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


