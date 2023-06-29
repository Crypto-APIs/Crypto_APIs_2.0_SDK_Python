# GetTokenDetailsByContractAddressRI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_decimals** | **str** | Defines the number of decimals that the token possesses. | 
**token_name** | **str** | Specifies the token&#39;s name. | [optional] 
**token_symbol** | **str** | Defines the unique symbol of the token. | [optional] 
**token_type** | **str** | Defines the type of the token. | 
**total_supply** | **str** | Defines the total number of tokens created that exist on the market minus the ones that have been burned. | 

## Example

```python
from cryptoapis.models.get_token_details_by_contract_address_ri import GetTokenDetailsByContractAddressRI

# TODO update the JSON string below
json = "{}"
# create an instance of GetTokenDetailsByContractAddressRI from a JSON string
get_token_details_by_contract_address_ri_instance = GetTokenDetailsByContractAddressRI.from_json(json)
# print the JSON string representation of the object
print GetTokenDetailsByContractAddressRI.to_json()

# convert the object into a dict
get_token_details_by_contract_address_ri_dict = get_token_details_by_contract_address_ri_instance.to_dict()
# create an instance of GetTokenDetailsByContractAddressRI from a dict
get_token_details_by_contract_address_ri_form_dict = get_token_details_by_contract_address_ri.from_dict(get_token_details_by_contract_address_ri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


