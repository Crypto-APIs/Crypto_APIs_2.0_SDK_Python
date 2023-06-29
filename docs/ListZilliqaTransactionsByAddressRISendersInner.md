# ListZilliqaTransactionsByAddressRISendersInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Represents the sender&#39;s address. | 
**amount** | **str** | Represents the total amount sent by this address including the fee. | 

## Example

```python
from cryptoapis.models.list_zilliqa_transactions_by_address_ri_senders_inner import ListZilliqaTransactionsByAddressRISendersInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListZilliqaTransactionsByAddressRISendersInner from a JSON string
list_zilliqa_transactions_by_address_ri_senders_inner_instance = ListZilliqaTransactionsByAddressRISendersInner.from_json(json)
# print the JSON string representation of the object
print ListZilliqaTransactionsByAddressRISendersInner.to_json()

# convert the object into a dict
list_zilliqa_transactions_by_address_ri_senders_inner_dict = list_zilliqa_transactions_by_address_ri_senders_inner_instance.to_dict()
# create an instance of ListZilliqaTransactionsByAddressRISendersInner from a dict
list_zilliqa_transactions_by_address_ri_senders_inner_form_dict = list_zilliqa_transactions_by_address_ri_senders_inner.from_dict(list_zilliqa_transactions_by_address_ri_senders_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


