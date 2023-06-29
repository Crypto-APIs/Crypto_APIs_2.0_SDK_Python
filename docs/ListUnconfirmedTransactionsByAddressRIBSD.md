# ListUnconfirmedTransactionsByAddressRIBSD

Dogecoin

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locktime** | **int** | Represents the locktime on the transaction on the specific blockchain, i.e. the blockheight at which the transaction is valid. | 
**size** | **int** | Represents the total size of this transaction. | 
**version** | **int** | Numeric representation of the transaction version | 
**vin** | [**List[ListUnconfirmedTransactionsByAddressRIBSDVinInner]**](ListUnconfirmedTransactionsByAddressRIBSDVinInner.md) | Represents the transaction inputs. | 
**vout** | [**List[GetTransactionDetailsByTransactionIDRIBSDVoutInner]**](GetTransactionDetailsByTransactionIDRIBSDVoutInner.md) | Represents the transaction outputs. | 

## Example

```python
from cryptoapis.models.list_unconfirmed_transactions_by_address_ribsd import ListUnconfirmedTransactionsByAddressRIBSD

# TODO update the JSON string below
json = "{}"
# create an instance of ListUnconfirmedTransactionsByAddressRIBSD from a JSON string
list_unconfirmed_transactions_by_address_ribsd_instance = ListUnconfirmedTransactionsByAddressRIBSD.from_json(json)
# print the JSON string representation of the object
print ListUnconfirmedTransactionsByAddressRIBSD.to_json()

# convert the object into a dict
list_unconfirmed_transactions_by_address_ribsd_dict = list_unconfirmed_transactions_by_address_ribsd_instance.to_dict()
# create an instance of ListUnconfirmedTransactionsByAddressRIBSD from a dict
list_unconfirmed_transactions_by_address_ribsd_form_dict = list_unconfirmed_transactions_by_address_ribsd.from_dict(list_unconfirmed_transactions_by_address_ribsd_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


