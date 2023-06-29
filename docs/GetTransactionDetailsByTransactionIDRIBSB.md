# GetTransactionDetailsByTransactionIDRIBSB

Bitcoin

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locktime** | **int** | Represents the time at which a particular transaction can be added to the blockchain. | 
**size** | **int** | Represents the total size of this transaction. | 
**v_size** | **int** | Represents the virtual size of this transaction. | 
**version** | **int** | Represents the transaction version number. | 
**vin** | [**List[GetTransactionDetailsByTransactionIDRIBSBVinInner]**](GetTransactionDetailsByTransactionIDRIBSBVinInner.md) | Represents the transaction inputs. | 
**vout** | [**List[GetTransactionDetailsByTransactionIDRIBSBVoutInner]**](GetTransactionDetailsByTransactionIDRIBSBVoutInner.md) | Represents the transaction outputs. | 

## Example

```python
from cryptoapis.models.get_transaction_details_by_transaction_idribsb import GetTransactionDetailsByTransactionIDRIBSB

# TODO update the JSON string below
json = "{}"
# create an instance of GetTransactionDetailsByTransactionIDRIBSB from a JSON string
get_transaction_details_by_transaction_idribsb_instance = GetTransactionDetailsByTransactionIDRIBSB.from_json(json)
# print the JSON string representation of the object
print GetTransactionDetailsByTransactionIDRIBSB.to_json()

# convert the object into a dict
get_transaction_details_by_transaction_idribsb_dict = get_transaction_details_by_transaction_idribsb_instance.to_dict()
# create an instance of GetTransactionDetailsByTransactionIDRIBSB from a dict
get_transaction_details_by_transaction_idribsb_form_dict = get_transaction_details_by_transaction_idribsb.from_dict(get_transaction_details_by_transaction_idribsb_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


