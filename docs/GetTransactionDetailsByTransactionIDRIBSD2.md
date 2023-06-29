# GetTransactionDetailsByTransactionIDRIBSD2

Dash

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locktime** | **int** | Represents the time at which a particular transaction can be added to the blockchain. | 
**size** | **int** | Represents the total size of this transaction. | 
**version** | **int** | Represents transaction version number. | 
**vin** | [**List[GetTransactionDetailsByTransactionIDRIBSD2VinInner]**](GetTransactionDetailsByTransactionIDRIBSD2VinInner.md) | Represents the transaction inputs. | 
**vout** | [**List[GetTransactionDetailsByTransactionIDRIBSD2VoutInner]**](GetTransactionDetailsByTransactionIDRIBSD2VoutInner.md) | Represents the transaction outputs. | 

## Example

```python
from cryptoapis.models.get_transaction_details_by_transaction_idribsd2 import GetTransactionDetailsByTransactionIDRIBSD2

# TODO update the JSON string below
json = "{}"
# create an instance of GetTransactionDetailsByTransactionIDRIBSD2 from a JSON string
get_transaction_details_by_transaction_idribsd2_instance = GetTransactionDetailsByTransactionIDRIBSD2.from_json(json)
# print the JSON string representation of the object
print GetTransactionDetailsByTransactionIDRIBSD2.to_json()

# convert the object into a dict
get_transaction_details_by_transaction_idribsd2_dict = get_transaction_details_by_transaction_idribsd2_instance.to_dict()
# create an instance of GetTransactionDetailsByTransactionIDRIBSD2 from a dict
get_transaction_details_by_transaction_idribsd2_form_dict = get_transaction_details_by_transaction_idribsd2.from_dict(get_transaction_details_by_transaction_idribsd2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


