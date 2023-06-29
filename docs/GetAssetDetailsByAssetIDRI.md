# GetAssetDetailsByAssetIDRI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **str** | Defines the unique ID of the specific asset. | 
**asset_logo** | [**GetAssetDetailsByAssetIDRIAssetLogo**](GetAssetDetailsByAssetIDRIAssetLogo.md) |  | 
**asset_name** | **str** | Specifies the name of the asset in question. | 
**asset_original_symbol** | **str** | Specifies the asset&#39;s original symbol as introduced by its founders. | 
**asset_symbol** | **str** | Specifies the asset&#39;s unique symbol in the Crypto APIs listings. | 
**asset_type** | **str** | Defines the type of the supported asset. This could be either \&quot;crypto\&quot; or \&quot;fiat\&quot;. | 
**latest_rate** | [**GetAssetDetailsByAssetIDRILatestRate**](GetAssetDetailsByAssetIDRILatestRate.md) |  | 
**slug** | **str** | Represents the asset&#x60;s unique slug string in Crypto APIs listings. | [optional] 
**specific_data** | [**GetAssetDetailsByAssetIDRIS**](GetAssetDetailsByAssetIDRIS.md) |  | 

## Example

```python
from cryptoapis.models.get_asset_details_by_asset_idri import GetAssetDetailsByAssetIDRI

# TODO update the JSON string below
json = "{}"
# create an instance of GetAssetDetailsByAssetIDRI from a JSON string
get_asset_details_by_asset_idri_instance = GetAssetDetailsByAssetIDRI.from_json(json)
# print the JSON string representation of the object
print GetAssetDetailsByAssetIDRI.to_json()

# convert the object into a dict
get_asset_details_by_asset_idri_dict = get_asset_details_by_asset_idri_instance.to_dict()
# create an instance of GetAssetDetailsByAssetIDRI from a dict
get_asset_details_by_asset_idri_form_dict = get_asset_details_by_asset_idri.from_dict(get_asset_details_by_asset_idri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


