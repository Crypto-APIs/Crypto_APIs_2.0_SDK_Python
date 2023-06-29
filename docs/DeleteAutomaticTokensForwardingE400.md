# DeleteAutomaticTokensForwardingE400


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Specifies an error code, e.g. error 404. | 
**message** | **str** | Specifies the message of the error, i.e. why the error was returned, e.g. error 404 stands for “not found”. | 
**details** | [**List[BannedIpAddressDetailsInner]**](BannedIpAddressDetailsInner.md) |  | [optional] 

## Example

```python
from cryptoapis.models.delete_automatic_tokens_forwarding_e400 import DeleteAutomaticTokensForwardingE400

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteAutomaticTokensForwardingE400 from a JSON string
delete_automatic_tokens_forwarding_e400_instance = DeleteAutomaticTokensForwardingE400.from_json(json)
# print the JSON string representation of the object
print DeleteAutomaticTokensForwardingE400.to_json()

# convert the object into a dict
delete_automatic_tokens_forwarding_e400_dict = delete_automatic_tokens_forwarding_e400_instance.to_dict()
# create an instance of DeleteAutomaticTokensForwardingE400 from a dict
delete_automatic_tokens_forwarding_e400_form_dict = delete_automatic_tokens_forwarding_e400.from_dict(delete_automatic_tokens_forwarding_e400_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


