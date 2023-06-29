# WalletAsAServiceTokenNotSupported

wallet_as_a_service_token_not_supported

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Specifies an error code, e.g. error 404. | 
**message** | **str** | Specifies the message of the error, i.e. why the error was returned, e.g. error 404 stands for “not found”. | 
**details** | [**List[BannedIpAddressDetailsInner]**](BannedIpAddressDetailsInner.md) |  | [optional] 

## Example

```python
from cryptoapis.models.wallet_as_a_service_token_not_supported import WalletAsAServiceTokenNotSupported

# TODO update the JSON string below
json = "{}"
# create an instance of WalletAsAServiceTokenNotSupported from a JSON string
wallet_as_a_service_token_not_supported_instance = WalletAsAServiceTokenNotSupported.from_json(json)
# print the JSON string representation of the object
print WalletAsAServiceTokenNotSupported.to_json()

# convert the object into a dict
wallet_as_a_service_token_not_supported_dict = wallet_as_a_service_token_not_supported_instance.to_dict()
# create an instance of WalletAsAServiceTokenNotSupported from a dict
wallet_as_a_service_token_not_supported_form_dict = wallet_as_a_service_token_not_supported.from_dict(wallet_as_a_service_token_not_supported_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


