# WalletAsAServiceNoDepositAddressesFound

wallet_as_a_service_no_deposit_addresses_found

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Specifies an error code, e.g. error 404. | 
**message** | **str** | Specifies the message of the error, i.e. why the error was returned, e.g. error 404 stands for “not found”. | 
**details** | [**List[BannedIpAddressDetailsInner]**](BannedIpAddressDetailsInner.md) |  | [optional] 

## Example

```python
from cryptoapis.models.wallet_as_a_service_no_deposit_addresses_found import WalletAsAServiceNoDepositAddressesFound

# TODO update the JSON string below
json = "{}"
# create an instance of WalletAsAServiceNoDepositAddressesFound from a JSON string
wallet_as_a_service_no_deposit_addresses_found_instance = WalletAsAServiceNoDepositAddressesFound.from_json(json)
# print the JSON string representation of the object
print WalletAsAServiceNoDepositAddressesFound.to_json()

# convert the object into a dict
wallet_as_a_service_no_deposit_addresses_found_dict = wallet_as_a_service_no_deposit_addresses_found_instance.to_dict()
# create an instance of WalletAsAServiceNoDepositAddressesFound from a dict
wallet_as_a_service_no_deposit_addresses_found_form_dict = wallet_as_a_service_no_deposit_addresses_found.from_dict(wallet_as_a_service_no_deposit_addresses_found_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


