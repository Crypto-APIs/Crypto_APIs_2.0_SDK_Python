# ListConfirmedTransactionsByAddressRIBST

Tron

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bandwidth_used** | **str** | Numeric representation of the transaction used bandwidth | 
**contract** | **str** | Numeric representation of the transaction contract | 
**energy_used** | **str** | String representation of the transaction used energy | 
**has_internal_transactions** | **bool** | Defines if there are internal transactions (true) or not (false) | 
**has_token_transfers** | **bool** | Defines if there are  tokens transfers (true) or not (false) | 
**input_data** | **str** | Numeric representation of the transaction input | 
**internal_transactions_count** | **int** | Representation of the internal transactions count | 
**token_transfers_count** | **int** | Representation of the token transfers count | 
**transaction_status** | **str** | Represents if the transaction is successfull or failed. | 

## Example

```python
from cryptoapis.models.list_confirmed_transactions_by_address_ribst import ListConfirmedTransactionsByAddressRIBST

# TODO update the JSON string below
json = "{}"
# create an instance of ListConfirmedTransactionsByAddressRIBST from a JSON string
list_confirmed_transactions_by_address_ribst_instance = ListConfirmedTransactionsByAddressRIBST.from_json(json)
# print the JSON string representation of the object
print ListConfirmedTransactionsByAddressRIBST.to_json()

# convert the object into a dict
list_confirmed_transactions_by_address_ribst_dict = list_confirmed_transactions_by_address_ribst_instance.to_dict()
# create an instance of ListConfirmedTransactionsByAddressRIBST from a dict
list_confirmed_transactions_by_address_ribst_form_dict = list_confirmed_transactions_by_address_ribst.from_dict(list_confirmed_transactions_by_address_ribst_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


