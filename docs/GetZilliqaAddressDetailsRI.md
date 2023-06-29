# GetZilliqaAddressDetailsRI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance** | [**GetZilliqaAddressDetailsRIBalance**](GetZilliqaAddressDetailsRIBalance.md) |  | 
**incoming_transactions_count** | **int** | Defines the received transaction count to the address. | 
**outgoing_transactions_count** | **int** | Defines the sent transaction count from the address. | 
**transactions_count** | **int** | Defines the entire count of the transactions. | 

## Example

```python
from cryptoapis.models.get_zilliqa_address_details_ri import GetZilliqaAddressDetailsRI

# TODO update the JSON string below
json = "{}"
# create an instance of GetZilliqaAddressDetailsRI from a JSON string
get_zilliqa_address_details_ri_instance = GetZilliqaAddressDetailsRI.from_json(json)
# print the JSON string representation of the object
print GetZilliqaAddressDetailsRI.to_json()

# convert the object into a dict
get_zilliqa_address_details_ri_dict = get_zilliqa_address_details_ri_instance.to_dict()
# create an instance of GetZilliqaAddressDetailsRI from a dict
get_zilliqa_address_details_ri_form_dict = get_zilliqa_address_details_ri.from_dict(get_zilliqa_address_details_ri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


