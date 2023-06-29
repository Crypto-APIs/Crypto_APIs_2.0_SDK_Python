# ResourceNotFound

resource_not_found

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Specifies an error code, e.g. error 404. | 
**message** | **str** | Specifies the message of the error, i.e. why the error was returned, e.g. error 404 stands for “not found”. | 
**details** | [**List[BannedIpAddressDetailsInner]**](BannedIpAddressDetailsInner.md) |  | [optional] 

## Example

```python
from cryptoapis.models.resource_not_found import ResourceNotFound

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceNotFound from a JSON string
resource_not_found_instance = ResourceNotFound.from_json(json)
# print the JSON string representation of the object
print ResourceNotFound.to_json()

# convert the object into a dict
resource_not_found_dict = resource_not_found_instance.to_dict()
# create an instance of ResourceNotFound from a dict
resource_not_found_form_dict = resource_not_found.from_dict(resource_not_found_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


