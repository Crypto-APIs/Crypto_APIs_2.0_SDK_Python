# ListSupportedTokensRI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**decimals** | **int** | Defines the token&#39;s decimal number or all of its points after the zero. | 
**identifier** | **str** | Represents a unique identifier for the specific blockchain and network, e.g. smart contract address, property ID, etc. | 
**name** | **str** | Defines the token name. | 
**symbol** | **str** | Defines the token&#39;s unique symbol in the Crypto APIs listings. | 
**type** | **str** | Represents the token&#39;s type representation, e.g. ERC-20, Omni, etc. | 

## Example

```python
from cryptoapis.models.list_supported_tokens_ri import ListSupportedTokensRI

# TODO update the JSON string below
json = "{}"
# create an instance of ListSupportedTokensRI from a JSON string
list_supported_tokens_ri_instance = ListSupportedTokensRI.from_json(json)
# print the JSON string representation of the object
print ListSupportedTokensRI.to_json()

# convert the object into a dict
list_supported_tokens_ri_dict = list_supported_tokens_ri_instance.to_dict()
# create an instance of ListSupportedTokensRI from a dict
list_supported_tokens_ri_form_dict = list_supported_tokens_ri.from_dict(list_supported_tokens_ri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


