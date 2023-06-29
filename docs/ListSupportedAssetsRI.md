# ListSupportedAssetsRI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **str** | Defines the unique ID of the specific asset. | 
**asset_name** | **str** | Specifies the name of the asset in question. | 
**asset_symbol** | **str** | Specifies the asset&#39;s unique symbol in the Crypto APIs listings. | 
**asset_type** | **str** | Defines the type of the supported asset. This could be either \&quot;crypto\&quot; or \&quot;fiat\&quot;. | 
**original_symbol** | **str** | Specifies the asset&#39;s original symbol as introduced by its founders. | 

## Example

```python
from cryptoapis.models.list_supported_assets_ri import ListSupportedAssetsRI

# TODO update the JSON string below
json = "{}"
# create an instance of ListSupportedAssetsRI from a JSON string
list_supported_assets_ri_instance = ListSupportedAssetsRI.from_json(json)
# print the JSON string representation of the object
print ListSupportedAssetsRI.to_json()

# convert the object into a dict
list_supported_assets_ri_dict = list_supported_assets_ri_instance.to_dict()
# create an instance of ListSupportedAssetsRI from a dict
list_supported_assets_ri_form_dict = list_supported_assets_ri.from_dict(list_supported_assets_ri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


