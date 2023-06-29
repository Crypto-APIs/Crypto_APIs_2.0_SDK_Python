# ListConfirmedTransactionsByAddressRIBSLVinInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | **List[str]** |  | 
**coinbase** | **str** | Represents the coinbase hex. | [optional] 
**script_sig** | [**ListConfirmedTransactionsByAddressRIBSLVinInnerScriptSig**](ListConfirmedTransactionsByAddressRIBSLVinInnerScriptSig.md) |  | 
**sequence** | **str** | Represents the script sequence number. | 
**txid** | **str** | Represents the reference transaction identifier. | 
**txinwitness** | **List[str]** |  | 
**value** | **str** | Represents the sent/received amount. | [optional] 
**vout** | **int** | Defines the vout of the transaction output, i.e. which output to spend. | [optional] 

## Example

```python
from cryptoapis.models.list_confirmed_transactions_by_address_ribsl_vin_inner import ListConfirmedTransactionsByAddressRIBSLVinInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListConfirmedTransactionsByAddressRIBSLVinInner from a JSON string
list_confirmed_transactions_by_address_ribsl_vin_inner_instance = ListConfirmedTransactionsByAddressRIBSLVinInner.from_json(json)
# print the JSON string representation of the object
print ListConfirmedTransactionsByAddressRIBSLVinInner.to_json()

# convert the object into a dict
list_confirmed_transactions_by_address_ribsl_vin_inner_dict = list_confirmed_transactions_by_address_ribsl_vin_inner_instance.to_dict()
# create an instance of ListConfirmedTransactionsByAddressRIBSLVinInner from a dict
list_confirmed_transactions_by_address_ribsl_vin_inner_form_dict = list_confirmed_transactions_by_address_ribsl_vin_inner.from_dict(list_confirmed_transactions_by_address_ribsl_vin_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


