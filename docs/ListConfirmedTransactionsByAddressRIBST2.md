# ListConfirmedTransactionsByAddressRIBST2

Tezos

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | **List[str]** |  | 
**counter** | **int** | Representation of the counter value | 
**gas_limit** | **str** | Represents the amount of gas used by this specific transaction alone. | 
**gas_used** | **str** | Represents the exact unit of gas that was used for the transaction. | 
**has_internal_transactions** | **bool** | Represents the presence of internal transactions | 
**is_confirmed** | **bool** | Representation of the confirmation status of the transfer | 
**nonce** | **int** | Defines the nonce | [optional] 
**token_transfers_count** | **int** | Representation of the  token transfers count | 
**transaction_status** | **str** | Defines the transaction status | 

## Example

```python
from cryptoapis.models.list_confirmed_transactions_by_address_ribst2 import ListConfirmedTransactionsByAddressRIBST2

# TODO update the JSON string below
json = "{}"
# create an instance of ListConfirmedTransactionsByAddressRIBST2 from a JSON string
list_confirmed_transactions_by_address_ribst2_instance = ListConfirmedTransactionsByAddressRIBST2.from_json(json)
# print the JSON string representation of the object
print ListConfirmedTransactionsByAddressRIBST2.to_json()

# convert the object into a dict
list_confirmed_transactions_by_address_ribst2_dict = list_confirmed_transactions_by_address_ribst2_instance.to_dict()
# create an instance of ListConfirmedTransactionsByAddressRIBST2 from a dict
list_confirmed_transactions_by_address_ribst2_form_dict = list_confirmed_transactions_by_address_ribst2.from_dict(list_confirmed_transactions_by_address_ribst2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


