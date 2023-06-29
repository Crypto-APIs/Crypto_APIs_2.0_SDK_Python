# GetWalletTransactionDetailsByTransactionIDRISendersInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | String array representation of the sender address | [optional] 
**amount** | **str** | String representation of the amount | [optional] 

## Example

```python
from cryptoapis.models.get_wallet_transaction_details_by_transaction_idri_senders_inner import GetWalletTransactionDetailsByTransactionIDRISendersInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetWalletTransactionDetailsByTransactionIDRISendersInner from a JSON string
get_wallet_transaction_details_by_transaction_idri_senders_inner_instance = GetWalletTransactionDetailsByTransactionIDRISendersInner.from_json(json)
# print the JSON string representation of the object
print GetWalletTransactionDetailsByTransactionIDRISendersInner.to_json()

# convert the object into a dict
get_wallet_transaction_details_by_transaction_idri_senders_inner_dict = get_wallet_transaction_details_by_transaction_idri_senders_inner_instance.to_dict()
# create an instance of GetWalletTransactionDetailsByTransactionIDRISendersInner from a dict
get_wallet_transaction_details_by_transaction_idri_senders_inner_form_dict = get_wallet_transaction_details_by_transaction_idri_senders_inner.from_dict(get_wallet_transaction_details_by_transaction_idri_senders_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


