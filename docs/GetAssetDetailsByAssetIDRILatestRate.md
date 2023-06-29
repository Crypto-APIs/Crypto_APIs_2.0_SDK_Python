# GetAssetDetailsByAssetIDRILatestRate

Specifies the latest price of the asset.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Represents the amount of the latest rate. | 
**calculation_timestamp** | **int** | Defines when the price was calculated in UNIX timestamp. Oldest possible timestamp is 30 days. | [optional] 
**unit** | **str** | Specifies the unit of the latest price of the asset. | 

## Example

```python
from cryptoapis.models.get_asset_details_by_asset_idri_latest_rate import GetAssetDetailsByAssetIDRILatestRate

# TODO update the JSON string below
json = "{}"
# create an instance of GetAssetDetailsByAssetIDRILatestRate from a JSON string
get_asset_details_by_asset_idri_latest_rate_instance = GetAssetDetailsByAssetIDRILatestRate.from_json(json)
# print the JSON string representation of the object
print GetAssetDetailsByAssetIDRILatestRate.to_json()

# convert the object into a dict
get_asset_details_by_asset_idri_latest_rate_dict = get_asset_details_by_asset_idri_latest_rate_instance.to_dict()
# create an instance of GetAssetDetailsByAssetIDRILatestRate from a dict
get_asset_details_by_asset_idri_latest_rate_form_dict = get_asset_details_by_asset_idri_latest_rate.from_dict(get_asset_details_by_asset_idri_latest_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


