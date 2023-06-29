# ListUnconfirmedTransactionsByAddressRIBSBC

Bitcoin Cash

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locktime** | **int** | Represents the locktime on the transaction on the specific blockchain, i.e. the blockheight at which the transaction is valid. | 
**size** | **int** | Represents the total size of this transaction. | 
**version** | **int** | Represents the transaction&#39;s version number. | 
**vin** | [**List[ListUnconfirmedTransactionsByAddressRIBSBCVinInner]**](ListUnconfirmedTransactionsByAddressRIBSBCVinInner.md) | Represents the transaction inputs. | 
**vout** | [**List[ListUnconfirmedTransactionsByAddressRIBSBCVoutInner]**](ListUnconfirmedTransactionsByAddressRIBSBCVoutInner.md) | Represents the transaction outputs. | 

## Example

```python
from cryptoapis.models.list_unconfirmed_transactions_by_address_ribsbc import ListUnconfirmedTransactionsByAddressRIBSBC

# TODO update the JSON string below
json = "{}"
# create an instance of ListUnconfirmedTransactionsByAddressRIBSBC from a JSON string
list_unconfirmed_transactions_by_address_ribsbc_instance = ListUnconfirmedTransactionsByAddressRIBSBC.from_json(json)
# print the JSON string representation of the object
print ListUnconfirmedTransactionsByAddressRIBSBC.to_json()

# convert the object into a dict
list_unconfirmed_transactions_by_address_ribsbc_dict = list_unconfirmed_transactions_by_address_ribsbc_instance.to_dict()
# create an instance of ListUnconfirmedTransactionsByAddressRIBSBC from a dict
list_unconfirmed_transactions_by_address_ribsbc_form_dict = list_unconfirmed_transactions_by_address_ribsbc.from_dict(list_unconfirmed_transactions_by_address_ribsbc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


