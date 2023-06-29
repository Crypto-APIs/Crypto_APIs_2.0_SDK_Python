# ListAllAssetsByWalletIDE400


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Specifies an error code, e.g. error 404. | 
**message** | **str** | Specifies the message of the error, i.e. why the error was returned, e.g. error 404 stands for “not found”. | 
**details** | [**List[BannedIpAddressDetailsInner]**](BannedIpAddressDetailsInner.md) |  | [optional] 

## Example

```python
from cryptoapis.models.list_all_assets_by_wallet_ide400 import ListAllAssetsByWalletIDE400

# TODO update the JSON string below
json = "{}"
# create an instance of ListAllAssetsByWalletIDE400 from a JSON string
list_all_assets_by_wallet_ide400_instance = ListAllAssetsByWalletIDE400.from_json(json)
# print the JSON string representation of the object
print ListAllAssetsByWalletIDE400.to_json()

# convert the object into a dict
list_all_assets_by_wallet_ide400_dict = list_all_assets_by_wallet_ide400_instance.to_dict()
# create an instance of ListAllAssetsByWalletIDE400 from a dict
list_all_assets_by_wallet_ide400_form_dict = list_all_assets_by_wallet_ide400.from_dict(list_all_assets_by_wallet_ide400_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


