# GetZilliqaTransactionDetailsByTransactionIDRIRecipientsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Represents the hash of the address that receives the funds. | 
**amount** | **str** | Defines the amount of the received funds as a string. | 

## Example

```python
from cryptoapis.models.get_zilliqa_transaction_details_by_transaction_idri_recipients_inner import GetZilliqaTransactionDetailsByTransactionIDRIRecipientsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetZilliqaTransactionDetailsByTransactionIDRIRecipientsInner from a JSON string
get_zilliqa_transaction_details_by_transaction_idri_recipients_inner_instance = GetZilliqaTransactionDetailsByTransactionIDRIRecipientsInner.from_json(json)
# print the JSON string representation of the object
print GetZilliqaTransactionDetailsByTransactionIDRIRecipientsInner.to_json()

# convert the object into a dict
get_zilliqa_transaction_details_by_transaction_idri_recipients_inner_dict = get_zilliqa_transaction_details_by_transaction_idri_recipients_inner_instance.to_dict()
# create an instance of GetZilliqaTransactionDetailsByTransactionIDRIRecipientsInner from a dict
get_zilliqa_transaction_details_by_transaction_idri_recipients_inner_form_dict = get_zilliqa_transaction_details_by_transaction_idri_recipients_inner.from_dict(get_zilliqa_transaction_details_by_transaction_idri_recipients_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


