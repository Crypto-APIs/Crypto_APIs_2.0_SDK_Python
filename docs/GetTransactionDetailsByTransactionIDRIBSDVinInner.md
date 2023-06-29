# GetTransactionDetailsByTransactionIDRIBSDVinInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | **List[str]** |  | 
**coinbase** | **str** | Represents the coinbase hex. | [optional] 
**script_sig** | [**GetTransactionDetailsByTransactionIDRIBSDVinInnerScriptSig**](GetTransactionDetailsByTransactionIDRIBSDVinInnerScriptSig.md) |  | 
**sequence** | **int** | Represents the script sequence number. | 
**txid** | **str** | Represents the reference transaction identifier. | [optional] 
**txinwitness** | **List[str]** |  | 
**value** | **str** | Represents the sent/received amount. | 
**vout** | **int** | It refers to the index of the output address of this transaction. The index starts from 0. | [optional] 

## Example

```python
from cryptoapis.models.get_transaction_details_by_transaction_idribsd_vin_inner import GetTransactionDetailsByTransactionIDRIBSDVinInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetTransactionDetailsByTransactionIDRIBSDVinInner from a JSON string
get_transaction_details_by_transaction_idribsd_vin_inner_instance = GetTransactionDetailsByTransactionIDRIBSDVinInner.from_json(json)
# print the JSON string representation of the object
print GetTransactionDetailsByTransactionIDRIBSDVinInner.to_json()

# convert the object into a dict
get_transaction_details_by_transaction_idribsd_vin_inner_dict = get_transaction_details_by_transaction_idribsd_vin_inner_instance.to_dict()
# create an instance of GetTransactionDetailsByTransactionIDRIBSDVinInner from a dict
get_transaction_details_by_transaction_idribsd_vin_inner_form_dict = get_transaction_details_by_transaction_idribsd_vin_inner.from_dict(get_transaction_details_by_transaction_idribsd_vin_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


