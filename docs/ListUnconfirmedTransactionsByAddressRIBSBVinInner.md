# ListUnconfirmedTransactionsByAddressRIBSBVinInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | **List[str]** |  | 
**script_sig** | [**ListUnconfirmedTransactionsByAddressRIBSBVinInnerScriptSig**](ListUnconfirmedTransactionsByAddressRIBSBVinInnerScriptSig.md) |  | 
**sequence** | **str** | Represents the script sequence number. | 
**txid** | **str** | Represents the reference transaction identifier. | [optional] 
**txinwitness** | **List[str]** |  | [optional] 
**value** | **str** | Represents the sent/received amount. | [optional] 
**vout** | **int** | Defines the vout of the transaction output, i.e. which output to spend. | [optional] 

## Example

```python
from cryptoapis.models.list_unconfirmed_transactions_by_address_ribsb_vin_inner import ListUnconfirmedTransactionsByAddressRIBSBVinInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListUnconfirmedTransactionsByAddressRIBSBVinInner from a JSON string
list_unconfirmed_transactions_by_address_ribsb_vin_inner_instance = ListUnconfirmedTransactionsByAddressRIBSBVinInner.from_json(json)
# print the JSON string representation of the object
print ListUnconfirmedTransactionsByAddressRIBSBVinInner.to_json()

# convert the object into a dict
list_unconfirmed_transactions_by_address_ribsb_vin_inner_dict = list_unconfirmed_transactions_by_address_ribsb_vin_inner_instance.to_dict()
# create an instance of ListUnconfirmedTransactionsByAddressRIBSBVinInner from a dict
list_unconfirmed_transactions_by_address_ribsb_vin_inner_form_dict = list_unconfirmed_transactions_by_address_ribsb_vin_inner.from_dict(list_unconfirmed_transactions_by_address_ribsb_vin_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


