# ListUnconfirmedTransactionsByAddressRIBSD2

Dash

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locktime** | **int** | Represents the locktime on the transaction on the specific blockchain, i.e. the blockheight at which the transaction is valid. | 
**size** | **int** | Represents the total size of this transaction. | 
**version** | **int** | Represents the transaction&#39;s version number. | 
**vin** | [**List[ListUnconfirmedTransactionsByAddressRIBSD2VinInner]**](ListUnconfirmedTransactionsByAddressRIBSD2VinInner.md) | Represents the transaction inputs. | 
**vout** | [**List[ListUnconfirmedTransactionsByAddressRIBSD2VoutInner]**](ListUnconfirmedTransactionsByAddressRIBSD2VoutInner.md) | Represents the transaction outputs. | 

## Example

```python
from cryptoapis.models.list_unconfirmed_transactions_by_address_ribsd2 import ListUnconfirmedTransactionsByAddressRIBSD2

# TODO update the JSON string below
json = "{}"
# create an instance of ListUnconfirmedTransactionsByAddressRIBSD2 from a JSON string
list_unconfirmed_transactions_by_address_ribsd2_instance = ListUnconfirmedTransactionsByAddressRIBSD2.from_json(json)
# print the JSON string representation of the object
print ListUnconfirmedTransactionsByAddressRIBSD2.to_json()

# convert the object into a dict
list_unconfirmed_transactions_by_address_ribsd2_dict = list_unconfirmed_transactions_by_address_ribsd2_instance.to_dict()
# create an instance of ListUnconfirmedTransactionsByAddressRIBSD2 from a dict
list_unconfirmed_transactions_by_address_ribsd2_form_dict = list_unconfirmed_transactions_by_address_ribsd2.from_dict(list_unconfirmed_transactions_by_address_ribsd2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


