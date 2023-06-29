# ListSupportedAssetsRData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | Defines how many items should be returned in the response per page basis. | 
**offset** | **int** | The starting index of the response items, i.e. where the response should start listing the returned items. | 
**total** | **int** | Defines the total number of items returned in the response. | 
**items** | [**List[ListSupportedAssetsRI]**](ListSupportedAssetsRI.md) |  | 

## Example

```python
from cryptoapis.models.list_supported_assets_r_data import ListSupportedAssetsRData

# TODO update the JSON string below
json = "{}"
# create an instance of ListSupportedAssetsRData from a JSON string
list_supported_assets_r_data_instance = ListSupportedAssetsRData.from_json(json)
# print the JSON string representation of the object
print ListSupportedAssetsRData.to_json()

# convert the object into a dict
list_supported_assets_r_data_dict = list_supported_assets_r_data_instance.to_dict()
# create an instance of ListSupportedAssetsRData from a dict
list_supported_assets_r_data_form_dict = list_supported_assets_r_data.from_dict(list_supported_assets_r_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


