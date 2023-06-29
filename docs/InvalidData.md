# InvalidData

invalid_data

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Specifies an error code, e.g. error 404. | 
**message** | **str** | Specifies the message of the error, i.e. why the error was returned, e.g. error 404 stands for “not found”. | 
**details** | [**List[BannedIpAddressDetailsInner]**](BannedIpAddressDetailsInner.md) |  | [optional] 

## Example

```python
from cryptoapis.models.invalid_data import InvalidData

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidData from a JSON string
invalid_data_instance = InvalidData.from_json(json)
# print the JSON string representation of the object
print InvalidData.to_json()

# convert the object into a dict
invalid_data_dict = invalid_data_instance.to_dict()
# create an instance of InvalidData from a dict
invalid_data_form_dict = invalid_data.from_dict(invalid_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


