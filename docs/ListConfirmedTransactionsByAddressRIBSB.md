# ListConfirmedTransactionsByAddressRIBSB

Bitcoin

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locktime** | **int** | Represents the locktime on the transaction on the specific blockchain, i.e. the blockheight at which the transaction is valid. | 
**size** | **int** | Represents the total size of this transaction. | 
**v_size** | **int** | Defines the transaction&#39;s virtual size. | 
**version** | **int** | Defines the version of the transaction. | 
**vin** | [**List[ListConfirmedTransactionsByAddressRIBSBVinInner]**](ListConfirmedTransactionsByAddressRIBSBVinInner.md) | Represents the transaction inputs. | 
**vout** | [**List[ListConfirmedTransactionsByAddressRIBSBVoutInner]**](ListConfirmedTransactionsByAddressRIBSBVoutInner.md) | Represents the transaction outputs. | 

## Example

```python
from cryptoapis.models.list_confirmed_transactions_by_address_ribsb import ListConfirmedTransactionsByAddressRIBSB

# TODO update the JSON string below
json = "{}"
# create an instance of ListConfirmedTransactionsByAddressRIBSB from a JSON string
list_confirmed_transactions_by_address_ribsb_instance = ListConfirmedTransactionsByAddressRIBSB.from_json(json)
# print the JSON string representation of the object
print ListConfirmedTransactionsByAddressRIBSB.to_json()

# convert the object into a dict
list_confirmed_transactions_by_address_ribsb_dict = list_confirmed_transactions_by_address_ribsb_instance.to_dict()
# create an instance of ListConfirmedTransactionsByAddressRIBSB from a dict
list_confirmed_transactions_by_address_ribsb_form_dict = list_confirmed_transactions_by_address_ribsb.from_dict(list_confirmed_transactions_by_address_ribsb_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


