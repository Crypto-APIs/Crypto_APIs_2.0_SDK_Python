# ListUnconfirmedTransactionsByAddressRIBSBCVoutInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_spent** | **bool** | Defines whether the output is spent or not. | 
**script_pub_key** | [**ListUnconfirmedTransactionsByAddressRIBSBCVoutInnerScriptPubKey**](ListUnconfirmedTransactionsByAddressRIBSBCVoutInnerScriptPubKey.md) |  | 
**value** | **str** | Represents the sent/received amount. | 

## Example

```python
from cryptoapis.models.list_unconfirmed_transactions_by_address_ribsbc_vout_inner import ListUnconfirmedTransactionsByAddressRIBSBCVoutInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListUnconfirmedTransactionsByAddressRIBSBCVoutInner from a JSON string
list_unconfirmed_transactions_by_address_ribsbc_vout_inner_instance = ListUnconfirmedTransactionsByAddressRIBSBCVoutInner.from_json(json)
# print the JSON string representation of the object
print ListUnconfirmedTransactionsByAddressRIBSBCVoutInner.to_json()

# convert the object into a dict
list_unconfirmed_transactions_by_address_ribsbc_vout_inner_dict = list_unconfirmed_transactions_by_address_ribsbc_vout_inner_instance.to_dict()
# create an instance of ListUnconfirmedTransactionsByAddressRIBSBCVoutInner from a dict
list_unconfirmed_transactions_by_address_ribsbc_vout_inner_form_dict = list_unconfirmed_transactions_by_address_ribsbc_vout_inner.from_dict(list_unconfirmed_transactions_by_address_ribsbc_vout_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


