# ListUnconfirmedTransactionsByAddressRIBSL

Litecoin

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locktime** | **int** | Represents the locktime on the transaction on the specific blockchain, i.e. the blockheight at which the transaction is valid. | 
**size** | **int** | Represents the total size of this transaction. | 
**v_size** | **int** | Represents the virtual size of this transaction. | 
**version** | **int** | Represents the transaction&#39;s version number. | 
**vin** | [**List[ListUnconfirmedTransactionsByAddressRIBSLVinInner]**](ListUnconfirmedTransactionsByAddressRIBSLVinInner.md) | Represents the transaction inputs. | 
**vout** | [**List[ListUnconfirmedTransactionsByAddressRIBSLVoutInner]**](ListUnconfirmedTransactionsByAddressRIBSLVoutInner.md) | Represents the transaction outputs. | 

## Example

```python
from cryptoapis.models.list_unconfirmed_transactions_by_address_ribsl import ListUnconfirmedTransactionsByAddressRIBSL

# TODO update the JSON string below
json = "{}"
# create an instance of ListUnconfirmedTransactionsByAddressRIBSL from a JSON string
list_unconfirmed_transactions_by_address_ribsl_instance = ListUnconfirmedTransactionsByAddressRIBSL.from_json(json)
# print the JSON string representation of the object
print ListUnconfirmedTransactionsByAddressRIBSL.to_json()

# convert the object into a dict
list_unconfirmed_transactions_by_address_ribsl_dict = list_unconfirmed_transactions_by_address_ribsl_instance.to_dict()
# create an instance of ListUnconfirmedTransactionsByAddressRIBSL from a dict
list_unconfirmed_transactions_by_address_ribsl_form_dict = list_unconfirmed_transactions_by_address_ribsl.from_dict(list_unconfirmed_transactions_by_address_ribsl_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


