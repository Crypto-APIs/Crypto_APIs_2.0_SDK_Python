# ListUnconfirmedTransactionsByAddressRISendersInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Represents the address of the sender. | 
**amount** | **str** | Represents the total amount sent by this address including the fee. | 

## Example

```python
from cryptoapis.models.list_unconfirmed_transactions_by_address_ri_senders_inner import ListUnconfirmedTransactionsByAddressRISendersInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListUnconfirmedTransactionsByAddressRISendersInner from a JSON string
list_unconfirmed_transactions_by_address_ri_senders_inner_instance = ListUnconfirmedTransactionsByAddressRISendersInner.from_json(json)
# print the JSON string representation of the object
print ListUnconfirmedTransactionsByAddressRISendersInner.to_json()

# convert the object into a dict
list_unconfirmed_transactions_by_address_ri_senders_inner_dict = list_unconfirmed_transactions_by_address_ri_senders_inner_instance.to_dict()
# create an instance of ListUnconfirmedTransactionsByAddressRISendersInner from a dict
list_unconfirmed_transactions_by_address_ri_senders_inner_form_dict = list_unconfirmed_transactions_by_address_ri_senders_inner.from_dict(list_unconfirmed_transactions_by_address_ri_senders_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


