# GetTransactionDetailsByTransactionIDRIBSBC

Bitcoin Cash

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locktime** | **int** | Represents the time at which a particular transaction can be added to the blockchain. | 
**size** | **int** | Represents the total size of this transaction. | 
**version** | **int** | Represents transaction version number. | 
**vin** | [**List[GetTransactionDetailsByTransactionIDRIBSBCVinInner]**](GetTransactionDetailsByTransactionIDRIBSBCVinInner.md) | Represents the transaction inputs. | 
**vout** | [**List[GetTransactionDetailsByTransactionIDRIBSBCVoutInner]**](GetTransactionDetailsByTransactionIDRIBSBCVoutInner.md) | Represents the transaction outputs. | 

## Example

```python
from cryptoapis.models.get_transaction_details_by_transaction_idribsbc import GetTransactionDetailsByTransactionIDRIBSBC

# TODO update the JSON string below
json = "{}"
# create an instance of GetTransactionDetailsByTransactionIDRIBSBC from a JSON string
get_transaction_details_by_transaction_idribsbc_instance = GetTransactionDetailsByTransactionIDRIBSBC.from_json(json)
# print the JSON string representation of the object
print GetTransactionDetailsByTransactionIDRIBSBC.to_json()

# convert the object into a dict
get_transaction_details_by_transaction_idribsbc_dict = get_transaction_details_by_transaction_idribsbc_instance.to_dict()
# create an instance of GetTransactionDetailsByTransactionIDRIBSBC from a dict
get_transaction_details_by_transaction_idribsbc_form_dict = get_transaction_details_by_transaction_idribsbc.from_dict(get_transaction_details_by_transaction_idribsbc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


