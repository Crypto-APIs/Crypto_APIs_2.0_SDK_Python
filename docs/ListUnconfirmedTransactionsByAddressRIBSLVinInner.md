# ListUnconfirmedTransactionsByAddressRIBSLVinInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | **List[str]** |  | 
**script_sig** | [**ListUnconfirmedTransactionsByAddressRIBSLVinInnerScriptSig**](ListUnconfirmedTransactionsByAddressRIBSLVinInnerScriptSig.md) |  | 
**sequence** | **str** | Represents the script sequence number. | 
**txid** | **str** | Represents the reference transaction identifier. | 
**txinwitness** | **List[str]** |  | 
**value** | **str** | Represents the sent/received amount. | 
**vout** | **int** | Defines the vout of the transaction output, i.e. which output to spend. | [optional] 

## Example

```python
from cryptoapis.models.list_unconfirmed_transactions_by_address_ribsl_vin_inner import ListUnconfirmedTransactionsByAddressRIBSLVinInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListUnconfirmedTransactionsByAddressRIBSLVinInner from a JSON string
list_unconfirmed_transactions_by_address_ribsl_vin_inner_instance = ListUnconfirmedTransactionsByAddressRIBSLVinInner.from_json(json)
# print the JSON string representation of the object
print ListUnconfirmedTransactionsByAddressRIBSLVinInner.to_json()

# convert the object into a dict
list_unconfirmed_transactions_by_address_ribsl_vin_inner_dict = list_unconfirmed_transactions_by_address_ribsl_vin_inner_instance.to_dict()
# create an instance of ListUnconfirmedTransactionsByAddressRIBSLVinInner from a dict
list_unconfirmed_transactions_by_address_ribsl_vin_inner_form_dict = list_unconfirmed_transactions_by_address_ribsl_vin_inner.from_dict(list_unconfirmed_transactions_by_address_ribsl_vin_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


