# ListTokensByAddressRI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confirmed_balance** | **str** | Defines the token balance that has been confirmed. | 
**contract_address** | **str** | Represents the contract address of the token, which controls its logic. It is not the address that holds the tokens. | 
**name** | **str** | Defines the token&#39;s name as a string. | 
**symbol** | **str** | Defines the token symbol by which the token contract is known. It is usually 3-4 characters in length. | 
**type** | **str** | Defines the specific token type. | 

## Example

```python
from cryptoapis.models.list_tokens_by_address_ri import ListTokensByAddressRI

# TODO update the JSON string below
json = "{}"
# create an instance of ListTokensByAddressRI from a JSON string
list_tokens_by_address_ri_instance = ListTokensByAddressRI.from_json(json)
# print the JSON string representation of the object
print ListTokensByAddressRI.to_json()

# convert the object into a dict
list_tokens_by_address_ri_dict = list_tokens_by_address_ri_instance.to_dict()
# create an instance of ListTokensByAddressRI from a dict
list_tokens_by_address_ri_form_dict = list_tokens_by_address_ri.from_dict(list_tokens_by_address_ri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


