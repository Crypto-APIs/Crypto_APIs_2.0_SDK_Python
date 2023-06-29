# GetTransactionDetailsByTransactionIDFromCallbackRIBSD2

Dogecoin

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locktime** | **int** | Represents the time at which a particular transaction can be added to the blockchain. | 
**size** | **int** | Represents the total size of this transaction. | 
**version** | **int** | Represents transaction version number. | 
**vin** | [**List[GetTransactionDetailsByTransactionIDFromCallbackRIBSD2VinInner]**](GetTransactionDetailsByTransactionIDFromCallbackRIBSD2VinInner.md) | Represents the transaction inputs. | 
**vout** | [**List[GetTransactionDetailsByTransactionIDFromCallbackRIBSD2VoutInner]**](GetTransactionDetailsByTransactionIDFromCallbackRIBSD2VoutInner.md) | Represents the transaction outputs. | 

## Example

```python
from cryptoapis.models.get_transaction_details_by_transaction_id_from_callback_ribsd2 import GetTransactionDetailsByTransactionIDFromCallbackRIBSD2

# TODO update the JSON string below
json = "{}"
# create an instance of GetTransactionDetailsByTransactionIDFromCallbackRIBSD2 from a JSON string
get_transaction_details_by_transaction_id_from_callback_ribsd2_instance = GetTransactionDetailsByTransactionIDFromCallbackRIBSD2.from_json(json)
# print the JSON string representation of the object
print GetTransactionDetailsByTransactionIDFromCallbackRIBSD2.to_json()

# convert the object into a dict
get_transaction_details_by_transaction_id_from_callback_ribsd2_dict = get_transaction_details_by_transaction_id_from_callback_ribsd2_instance.to_dict()
# create an instance of GetTransactionDetailsByTransactionIDFromCallbackRIBSD2 from a dict
get_transaction_details_by_transaction_id_from_callback_ribsd2_form_dict = get_transaction_details_by_transaction_id_from_callback_ribsd2.from_dict(get_transaction_details_by_transaction_id_from_callback_ribsd2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


