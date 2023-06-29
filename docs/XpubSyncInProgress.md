# XpubSyncInProgress

xpub_sync_in_progress

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Specifies an error code, e.g. error 404. | 
**message** | **str** | Specifies the message of the error, i.e. why the error was returned, e.g. error 404 stands for “not found”. | 
**details** | [**List[BannedIpAddressDetailsInner]**](BannedIpAddressDetailsInner.md) |  | [optional] 

## Example

```python
from cryptoapis.models.xpub_sync_in_progress import XpubSyncInProgress

# TODO update the JSON string below
json = "{}"
# create an instance of XpubSyncInProgress from a JSON string
xpub_sync_in_progress_instance = XpubSyncInProgress.from_json(json)
# print the JSON string representation of the object
print XpubSyncInProgress.to_json()

# convert the object into a dict
xpub_sync_in_progress_dict = xpub_sync_in_progress_instance.to_dict()
# create an instance of XpubSyncInProgress from a dict
xpub_sync_in_progress_form_dict = xpub_sync_in_progress.from_dict(xpub_sync_in_progress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


