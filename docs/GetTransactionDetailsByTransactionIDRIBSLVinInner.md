# GetTransactionDetailsByTransactionIDRIBSLVinInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | **List[str]** |  | 
**coinbase** | **str** | Represents the coinbase hex. | [optional] 
**script_sig** | [**GetTransactionDetailsByTransactionIDRIBSLVinInnerScriptSig**](GetTransactionDetailsByTransactionIDRIBSLVinInnerScriptSig.md) |  | 
**sequence** | **int** | Represents the script sequence number. | 
**txid** | **str** | Represents the reference transaction identifier. | [optional] 
**txinwitness** | **List[str]** |  | 
**value** | **str** | Represents the sent/received amount. | [optional] 
**vout** | **int** | It refers to the index of the output address of this transaction. The index starts from 0. | [optional] 

## Example

```python
from cryptoapis.models.get_transaction_details_by_transaction_idribsl_vin_inner import GetTransactionDetailsByTransactionIDRIBSLVinInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetTransactionDetailsByTransactionIDRIBSLVinInner from a JSON string
get_transaction_details_by_transaction_idribsl_vin_inner_instance = GetTransactionDetailsByTransactionIDRIBSLVinInner.from_json(json)
# print the JSON string representation of the object
print GetTransactionDetailsByTransactionIDRIBSLVinInner.to_json()

# convert the object into a dict
get_transaction_details_by_transaction_idribsl_vin_inner_dict = get_transaction_details_by_transaction_idribsl_vin_inner_instance.to_dict()
# create an instance of GetTransactionDetailsByTransactionIDRIBSLVinInner from a dict
get_transaction_details_by_transaction_idribsl_vin_inner_form_dict = get_transaction_details_by_transaction_idribsl_vin_inner.from_dict(get_transaction_details_by_transaction_idribsl_vin_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


