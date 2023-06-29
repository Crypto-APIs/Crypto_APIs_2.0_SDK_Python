# ListConfirmedTransactionsByAddressRIBSBVoutInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_spent** | **bool** | Defines whether the output is spent or not. | 
**script_pub_key** | [**ListConfirmedTransactionsByAddressRIBSBVoutInnerScriptPubKey**](ListConfirmedTransactionsByAddressRIBSBVoutInnerScriptPubKey.md) |  | 
**value** | **str** | Represents the sent/received amount. | 

## Example

```python
from cryptoapis.models.list_confirmed_transactions_by_address_ribsb_vout_inner import ListConfirmedTransactionsByAddressRIBSBVoutInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListConfirmedTransactionsByAddressRIBSBVoutInner from a JSON string
list_confirmed_transactions_by_address_ribsb_vout_inner_instance = ListConfirmedTransactionsByAddressRIBSBVoutInner.from_json(json)
# print the JSON string representation of the object
print ListConfirmedTransactionsByAddressRIBSBVoutInner.to_json()

# convert the object into a dict
list_confirmed_transactions_by_address_ribsb_vout_inner_dict = list_confirmed_transactions_by_address_ribsb_vout_inner_instance.to_dict()
# create an instance of ListConfirmedTransactionsByAddressRIBSBVoutInner from a dict
list_confirmed_transactions_by_address_ribsb_vout_inner_form_dict = list_confirmed_transactions_by_address_ribsb_vout_inner.from_dict(list_confirmed_transactions_by_address_ribsb_vout_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


