# NewRevertedBlockE401


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Specifies an error code, e.g. error 404. | 
**message** | **str** | Specifies the message of the error, i.e. why the error was returned, e.g. error 404 stands for “not found”. | 
**details** | [**List[BannedIpAddressDetailsInner]**](BannedIpAddressDetailsInner.md) |  | [optional] 

## Example

```python
from cryptoapis.models.new_reverted_block_e401 import NewRevertedBlockE401

# TODO update the JSON string below
json = "{}"
# create an instance of NewRevertedBlockE401 from a JSON string
new_reverted_block_e401_instance = NewRevertedBlockE401.from_json(json)
# print the JSON string representation of the object
print NewRevertedBlockE401.to_json()

# convert the object into a dict
new_reverted_block_e401_dict = new_reverted_block_e401_instance.to_dict()
# create an instance of NewRevertedBlockE401 from a dict
new_reverted_block_e401_form_dict = new_reverted_block_e401.from_dict(new_reverted_block_e401_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

