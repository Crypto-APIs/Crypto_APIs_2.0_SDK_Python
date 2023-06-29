# GetTransactionDetailsByTransactionIDRIBSZVinInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | **List[str]** |  | 
**script_sig** | [**GetTransactionDetailsByTransactionIDRIBSZVinInnerScriptSig**](GetTransactionDetailsByTransactionIDRIBSZVinInnerScriptSig.md) |  | 
**sequence** | **int** | Represents the script sequence number. | 
**txid** | **str** | Represents the reference transaction identifier. | 
**txinwitness** | **List[str]** |  | 
**value** | **str** | Defines the specific amount. | 
**vout** | **int** | It refers to the index of the output address of this transaction. The index starts from 0. | 

## Example

```python
from cryptoapis.models.get_transaction_details_by_transaction_idribsz_vin_inner import GetTransactionDetailsByTransactionIDRIBSZVinInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetTransactionDetailsByTransactionIDRIBSZVinInner from a JSON string
get_transaction_details_by_transaction_idribsz_vin_inner_instance = GetTransactionDetailsByTransactionIDRIBSZVinInner.from_json(json)
# print the JSON string representation of the object
print GetTransactionDetailsByTransactionIDRIBSZVinInner.to_json()

# convert the object into a dict
get_transaction_details_by_transaction_idribsz_vin_inner_dict = get_transaction_details_by_transaction_idribsz_vin_inner_instance.to_dict()
# create an instance of GetTransactionDetailsByTransactionIDRIBSZVinInner from a dict
get_transaction_details_by_transaction_idribsz_vin_inner_form_dict = get_transaction_details_by_transaction_idribsz_vin_inner.from_dict(get_transaction_details_by_transaction_idribsz_vin_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


