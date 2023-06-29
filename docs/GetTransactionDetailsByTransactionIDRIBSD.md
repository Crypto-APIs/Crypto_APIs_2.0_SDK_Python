# GetTransactionDetailsByTransactionIDRIBSD

Dogecoin

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locktime** | **int** | Represents the time at which a particular transaction can be added to the blockchain. | 
**size** | **int** | Represents the total size of this transaction. | 
**version** | **int** | Represents transaction version number. | 
**vin** | [**List[GetTransactionDetailsByTransactionIDRIBSDVinInner]**](GetTransactionDetailsByTransactionIDRIBSDVinInner.md) | Represents the transaction inputs. | 
**vout** | [**List[GetTransactionDetailsByTransactionIDRIBSDVoutInner]**](GetTransactionDetailsByTransactionIDRIBSDVoutInner.md) | Represents the transaction outputs. | 

## Example

```python
from cryptoapis.models.get_transaction_details_by_transaction_idribsd import GetTransactionDetailsByTransactionIDRIBSD

# TODO update the JSON string below
json = "{}"
# create an instance of GetTransactionDetailsByTransactionIDRIBSD from a JSON string
get_transaction_details_by_transaction_idribsd_instance = GetTransactionDetailsByTransactionIDRIBSD.from_json(json)
# print the JSON string representation of the object
print GetTransactionDetailsByTransactionIDRIBSD.to_json()

# convert the object into a dict
get_transaction_details_by_transaction_idribsd_dict = get_transaction_details_by_transaction_idribsd_instance.to_dict()
# create an instance of GetTransactionDetailsByTransactionIDRIBSD from a dict
get_transaction_details_by_transaction_idribsd_form_dict = get_transaction_details_by_transaction_idribsd.from_dict(get_transaction_details_by_transaction_idribsd_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


