# ListUnconfirmedTransactionsByAddressRIBSD2VinInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | **List[str]** |  | 
**script_sig** | [**ListConfirmedTransactionsByAddressRIBSD2VinInnerScriptSig**](ListConfirmedTransactionsByAddressRIBSD2VinInnerScriptSig.md) |  | 
**sequence** | **str** | Represents the script sequence number. | 
**txid** | **str** | Represents the reference transaction identifier. | 
**txinwitness** | **List[str]** |  | 
**value** | **str** | String representation of the amount | [optional] 
**vout** | **int** | It refers to the index of the output address of this transaction. The index starts from 0. | 

## Example

```python
from cryptoapis.models.list_unconfirmed_transactions_by_address_ribsd2_vin_inner import ListUnconfirmedTransactionsByAddressRIBSD2VinInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListUnconfirmedTransactionsByAddressRIBSD2VinInner from a JSON string
list_unconfirmed_transactions_by_address_ribsd2_vin_inner_instance = ListUnconfirmedTransactionsByAddressRIBSD2VinInner.from_json(json)
# print the JSON string representation of the object
print ListUnconfirmedTransactionsByAddressRIBSD2VinInner.to_json()

# convert the object into a dict
list_unconfirmed_transactions_by_address_ribsd2_vin_inner_dict = list_unconfirmed_transactions_by_address_ribsd2_vin_inner_instance.to_dict()
# create an instance of ListUnconfirmedTransactionsByAddressRIBSD2VinInner from a dict
list_unconfirmed_transactions_by_address_ribsd2_vin_inner_form_dict = list_unconfirmed_transactions_by_address_ribsd2_vin_inner.from_dict(list_unconfirmed_transactions_by_address_ribsd2_vin_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


