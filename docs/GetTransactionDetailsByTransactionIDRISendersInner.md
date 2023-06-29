# GetTransactionDetailsByTransactionIDRISendersInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Represents the address which sends this transaction. In UTXO-based protocols like Bitcoin there could be several senders while in account-based protocols like Ethereum there is always only one sender. | 
**amount** | **str** | Represents the total amount sent by this address including the fee. | 

## Example

```python
from cryptoapis.models.get_transaction_details_by_transaction_idri_senders_inner import GetTransactionDetailsByTransactionIDRISendersInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetTransactionDetailsByTransactionIDRISendersInner from a JSON string
get_transaction_details_by_transaction_idri_senders_inner_instance = GetTransactionDetailsByTransactionIDRISendersInner.from_json(json)
# print the JSON string representation of the object
print GetTransactionDetailsByTransactionIDRISendersInner.to_json()

# convert the object into a dict
get_transaction_details_by_transaction_idri_senders_inner_dict = get_transaction_details_by_transaction_idri_senders_inner_instance.to_dict()
# create an instance of GetTransactionDetailsByTransactionIDRISendersInner from a dict
get_transaction_details_by_transaction_idri_senders_inner_form_dict = get_transaction_details_by_transaction_idri_senders_inner.from_dict(get_transaction_details_by_transaction_idri_senders_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


