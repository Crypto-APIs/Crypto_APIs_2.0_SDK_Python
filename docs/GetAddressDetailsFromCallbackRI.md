# GetAddressDetailsFromCallbackRI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**incoming_transactions_count** | **int** | Defines the received transaction count to the address. | 
**outgoing_transactions_count** | **int** | Defines the sent transaction count from the address. | 
**transactions_count** | **int** | Represents the total number of confirmed coins transactions for this address, both incoming and outgoing. Applies for coins only and not tokens transfers e.g. for Ethereum. transactionsCount could result as less than incoming and outgoing transactions put together (e.g. in Bitcoin), due to the fact that one and the same address could be in senders and receivers addresses. | 
**confirmed_balance** | [**GetAddressDetailsFromCallbackRIConfirmedBalance**](GetAddressDetailsFromCallbackRIConfirmedBalance.md) |  | 
**total_received** | [**GetAddressDetailsFromCallbackRITotalReceived**](GetAddressDetailsFromCallbackRITotalReceived.md) |  | 
**total_spent** | [**GetAddressDetailsFromCallbackRITotalSpent**](GetAddressDetailsFromCallbackRITotalSpent.md) |  | 
**sequence** | **int** | Defines the transaction input&#39;s sequence as an integer, which is is used when transactions are replaced with newer versions before LockTime. | [optional] 

## Example

```python
from cryptoapis.models.get_address_details_from_callback_ri import GetAddressDetailsFromCallbackRI

# TODO update the JSON string below
json = "{}"
# create an instance of GetAddressDetailsFromCallbackRI from a JSON string
get_address_details_from_callback_ri_instance = GetAddressDetailsFromCallbackRI.from_json(json)
# print the JSON string representation of the object
print GetAddressDetailsFromCallbackRI.to_json()

# convert the object into a dict
get_address_details_from_callback_ri_dict = get_address_details_from_callback_ri_instance.to_dict()
# create an instance of GetAddressDetailsFromCallbackRI from a dict
get_address_details_from_callback_ri_form_dict = get_address_details_from_callback_ri.from_dict(get_address_details_from_callback_ri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


