# XpubNotSynced

xpub_not_synced

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Specifies an error code, e.g. error 404. | 
**message** | **str** | Specifies the message of the error, i.e. why the error was returned, e.g. error 404 stands for “not found”. | 
**details** | [**List[BannedIpAddressDetailsInner]**](BannedIpAddressDetailsInner.md) |  | [optional] 

## Example

```python
from cryptoapis.models.xpub_not_synced import XpubNotSynced

# TODO update the JSON string below
json = "{}"
# create an instance of XpubNotSynced from a JSON string
xpub_not_synced_instance = XpubNotSynced.from_json(json)
# print the JSON string representation of the object
print XpubNotSynced.to_json()

# convert the object into a dict
xpub_not_synced_dict = xpub_not_synced_instance.to_dict()
# create an instance of XpubNotSynced from a dict
xpub_not_synced_form_dict = xpub_not_synced.from_dict(xpub_not_synced_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


