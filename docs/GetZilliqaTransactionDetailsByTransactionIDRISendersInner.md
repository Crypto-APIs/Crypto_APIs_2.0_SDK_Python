# GetZilliqaTransactionDetailsByTransactionIDRISendersInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Represents the hash of the address that provides the funds. | 
**amount** | **str** | Represents the total amount sent by this address including the fee. | 

## Example

```python
from cryptoapis.models.get_zilliqa_transaction_details_by_transaction_idri_senders_inner import GetZilliqaTransactionDetailsByTransactionIDRISendersInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetZilliqaTransactionDetailsByTransactionIDRISendersInner from a JSON string
get_zilliqa_transaction_details_by_transaction_idri_senders_inner_instance = GetZilliqaTransactionDetailsByTransactionIDRISendersInner.from_json(json)
# print the JSON string representation of the object
print GetZilliqaTransactionDetailsByTransactionIDRISendersInner.to_json()

# convert the object into a dict
get_zilliqa_transaction_details_by_transaction_idri_senders_inner_dict = get_zilliqa_transaction_details_by_transaction_idri_senders_inner_instance.to_dict()
# create an instance of GetZilliqaTransactionDetailsByTransactionIDRISendersInner from a dict
get_zilliqa_transaction_details_by_transaction_idri_senders_inner_form_dict = get_zilliqa_transaction_details_by_transaction_idri_senders_inner.from_dict(get_zilliqa_transaction_details_by_transaction_idri_senders_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


