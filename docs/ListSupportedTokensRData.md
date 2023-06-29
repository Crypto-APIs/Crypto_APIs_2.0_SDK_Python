# ListSupportedTokensRData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | Defines how many items should be returned in the response per page basis. | 
**offset** | **int** | The starting index of the response items, i.e. where the response should start listing the returned items. | 
**total** | **int** | Defines the total number of items returned in the response. | 
**items** | [**List[ListSupportedTokensRI]**](ListSupportedTokensRI.md) |  | 

## Example

```python
from cryptoapis.models.list_supported_tokens_r_data import ListSupportedTokensRData

# TODO update the JSON string below
json = "{}"
# create an instance of ListSupportedTokensRData from a JSON string
list_supported_tokens_r_data_instance = ListSupportedTokensRData.from_json(json)
# print the JSON string representation of the object
print ListSupportedTokensRData.to_json()

# convert the object into a dict
list_supported_tokens_r_data_dict = list_supported_tokens_r_data_instance.to_dict()
# create an instance of ListSupportedTokensRData from a dict
list_supported_tokens_r_data_form_dict = list_supported_tokens_r_data.from_dict(list_supported_tokens_r_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


