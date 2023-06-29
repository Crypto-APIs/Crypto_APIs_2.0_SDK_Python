# GetTransactionDetailsByTransactionIDFromCallbackRIBSD

Dash

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locktime** | **int** | Represents the time at which a particular transaction can be added to the blockchain. | 
**size** | **int** | Represents the total size of this transaction. | 
**version** | **int** | Represents transaction version number. | 
**vin** | [**List[GetTransactionDetailsByTransactionIDFromCallbackRIBSDVinInner]**](GetTransactionDetailsByTransactionIDFromCallbackRIBSDVinInner.md) | Represents the transaction inputs. | 
**vout** | [**List[GetTransactionDetailsByTransactionIDFromCallbackRIBSDVoutInner]**](GetTransactionDetailsByTransactionIDFromCallbackRIBSDVoutInner.md) | Represents the transaction outputs. | 

## Example

```python
from cryptoapis.models.get_transaction_details_by_transaction_id_from_callback_ribsd import GetTransactionDetailsByTransactionIDFromCallbackRIBSD

# TODO update the JSON string below
json = "{}"
# create an instance of GetTransactionDetailsByTransactionIDFromCallbackRIBSD from a JSON string
get_transaction_details_by_transaction_id_from_callback_ribsd_instance = GetTransactionDetailsByTransactionIDFromCallbackRIBSD.from_json(json)
# print the JSON string representation of the object
print GetTransactionDetailsByTransactionIDFromCallbackRIBSD.to_json()

# convert the object into a dict
get_transaction_details_by_transaction_id_from_callback_ribsd_dict = get_transaction_details_by_transaction_id_from_callback_ribsd_instance.to_dict()
# create an instance of GetTransactionDetailsByTransactionIDFromCallbackRIBSD from a dict
get_transaction_details_by_transaction_id_from_callback_ribsd_form_dict = get_transaction_details_by_transaction_id_from_callback_ribsd.from_dict(get_transaction_details_by_transaction_id_from_callback_ribsd_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


