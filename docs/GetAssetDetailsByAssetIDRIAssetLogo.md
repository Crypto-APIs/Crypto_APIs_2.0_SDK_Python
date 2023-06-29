# GetAssetDetailsByAssetIDRIAssetLogo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encoding** | **str** | Defines the encoding of the image data which is usually base64. | 
**image_data** | **str** | Defines the encoded image data as a string. | 
**mime_type** | **str** | Defines the image type of the logo - jpg, png, svg, etc. | 

## Example

```python
from cryptoapis.models.get_asset_details_by_asset_idri_asset_logo import GetAssetDetailsByAssetIDRIAssetLogo

# TODO update the JSON string below
json = "{}"
# create an instance of GetAssetDetailsByAssetIDRIAssetLogo from a JSON string
get_asset_details_by_asset_idri_asset_logo_instance = GetAssetDetailsByAssetIDRIAssetLogo.from_json(json)
# print the JSON string representation of the object
print GetAssetDetailsByAssetIDRIAssetLogo.to_json()

# convert the object into a dict
get_asset_details_by_asset_idri_asset_logo_dict = get_asset_details_by_asset_idri_asset_logo_instance.to_dict()
# create an instance of GetAssetDetailsByAssetIDRIAssetLogo from a dict
get_asset_details_by_asset_idri_asset_logo_form_dict = get_asset_details_by_asset_idri_asset_logo.from_dict(get_asset_details_by_asset_idri_asset_logo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


