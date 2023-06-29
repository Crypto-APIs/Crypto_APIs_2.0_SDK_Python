# ListUnconfirmedTransactionsByAddressRIBSB

Bitcoin

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locktime** | **int** | Represents the locktime on the transaction on the specific blockchain, i.e. the blockheight at which the transaction is valid. | 
**size** | **int** | Represents the total size of this transaction. | 
**v_size** | **int** | Defines the transaction&#39;s virtual size. | 
**version** | **int** | Defines the version of the transaction. | 
**vin** | [**List[ListUnconfirmedTransactionsByAddressRIBSBVinInner]**](ListUnconfirmedTransactionsByAddressRIBSBVinInner.md) | Represents the transaction inputs. | 
**vout** | [**List[ListUnconfirmedTransactionsByAddressRIBSBVoutInner]**](ListUnconfirmedTransactionsByAddressRIBSBVoutInner.md) | Represents the transaction outputs. | 

## Example

```python
from cryptoapis.models.list_unconfirmed_transactions_by_address_ribsb import ListUnconfirmedTransactionsByAddressRIBSB

# TODO update the JSON string below
json = "{}"
# create an instance of ListUnconfirmedTransactionsByAddressRIBSB from a JSON string
list_unconfirmed_transactions_by_address_ribsb_instance = ListUnconfirmedTransactionsByAddressRIBSB.from_json(json)
# print the JSON string representation of the object
print ListUnconfirmedTransactionsByAddressRIBSB.to_json()

# convert the object into a dict
list_unconfirmed_transactions_by_address_ribsb_dict = list_unconfirmed_transactions_by_address_ribsb_instance.to_dict()
# create an instance of ListUnconfirmedTransactionsByAddressRIBSB from a dict
list_unconfirmed_transactions_by_address_ribsb_form_dict = list_unconfirmed_transactions_by_address_ribsb.from_dict(list_unconfirmed_transactions_by_address_ribsb_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


