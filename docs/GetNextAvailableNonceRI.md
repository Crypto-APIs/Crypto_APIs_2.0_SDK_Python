# GetNextAvailableNonceRI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_available_nonce** | **int** | Represents the sequential running number for an address, starting from 0 for the first transaction. E.g., if the nonce of a transaction is 10, it would be the 11th transaction sent from the sender&#39;s address. | 

## Example

```python
from cryptoapis.models.get_next_available_nonce_ri import GetNextAvailableNonceRI

# TODO update the JSON string below
json = "{}"
# create an instance of GetNextAvailableNonceRI from a JSON string
get_next_available_nonce_ri_instance = GetNextAvailableNonceRI.from_json(json)
# print the JSON string representation of the object
print GetNextAvailableNonceRI.to_json()

# convert the object into a dict
get_next_available_nonce_ri_dict = get_next_available_nonce_ri_instance.to_dict()
# create an instance of GetNextAvailableNonceRI from a dict
get_next_available_nonce_ri_form_dict = get_next_available_nonce_ri.from_dict(get_next_available_nonce_ri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


