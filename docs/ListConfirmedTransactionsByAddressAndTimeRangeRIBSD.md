# ListConfirmedTransactionsByAddressAndTimeRangeRIBSD

Dogecoin

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locktime** | **int** | Represents the locktime on the transaction on the specific blockchain, i.e. the blockheight at which the transaction is valid. | 
**size** | **int** | Represents the total size of this transaction. | 
**version** | **int** | Represents the transaction&#39;s version number. | 
**vin** | [**List[ListConfirmedTransactionsByAddressRIBSDVinInner]**](ListConfirmedTransactionsByAddressRIBSDVinInner.md) | Represents the transaction inputs. | 
**vout** | [**List[GetTransactionDetailsByTransactionIDRIBSDVoutInner]**](GetTransactionDetailsByTransactionIDRIBSDVoutInner.md) | Represents the transaction outputs. | 

## Example

```python
from cryptoapis.models.list_confirmed_transactions_by_address_and_time_range_ribsd import ListConfirmedTransactionsByAddressAndTimeRangeRIBSD

# TODO update the JSON string below
json = "{}"
# create an instance of ListConfirmedTransactionsByAddressAndTimeRangeRIBSD from a JSON string
list_confirmed_transactions_by_address_and_time_range_ribsd_instance = ListConfirmedTransactionsByAddressAndTimeRangeRIBSD.from_json(json)
# print the JSON string representation of the object
print ListConfirmedTransactionsByAddressAndTimeRangeRIBSD.to_json()

# convert the object into a dict
list_confirmed_transactions_by_address_and_time_range_ribsd_dict = list_confirmed_transactions_by_address_and_time_range_ribsd_instance.to_dict()
# create an instance of ListConfirmedTransactionsByAddressAndTimeRangeRIBSD from a dict
list_confirmed_transactions_by_address_and_time_range_ribsd_form_dict = list_confirmed_transactions_by_address_and_time_range_ribsd.from_dict(list_confirmed_transactions_by_address_and_time_range_ribsd_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


