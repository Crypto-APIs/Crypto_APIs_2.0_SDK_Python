# GetTransactionDetailsByTransactionIDRIRecipientsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The address which receives this transaction. In UTXO-based protocols like Bitcoin there could be several senders while in account-based protocols like Ethereum there is always only one recipient. | 
**amount** | **str** | Represents the amount received to this address. | 

## Example

```python
from cryptoapis.models.get_transaction_details_by_transaction_idri_recipients_inner import GetTransactionDetailsByTransactionIDRIRecipientsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetTransactionDetailsByTransactionIDRIRecipientsInner from a JSON string
get_transaction_details_by_transaction_idri_recipients_inner_instance = GetTransactionDetailsByTransactionIDRIRecipientsInner.from_json(json)
# print the JSON string representation of the object
print GetTransactionDetailsByTransactionIDRIRecipientsInner.to_json()

# convert the object into a dict
get_transaction_details_by_transaction_idri_recipients_inner_dict = get_transaction_details_by_transaction_idri_recipients_inner_instance.to_dict()
# create an instance of GetTransactionDetailsByTransactionIDRIRecipientsInner from a dict
get_transaction_details_by_transaction_idri_recipients_inner_form_dict = get_transaction_details_by_transaction_idri_recipients_inner.from_dict(get_transaction_details_by_transaction_idri_recipients_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


