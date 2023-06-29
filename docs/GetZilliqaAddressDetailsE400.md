# GetZilliqaAddressDetailsE400


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Specifies an error code, e.g. error 404. | 
**message** | **str** | Specifies the message of the error, i.e. why the error was returned, e.g. error 404 stands for “not found”. | 
**details** | [**List[BannedIpAddressDetailsInner]**](BannedIpAddressDetailsInner.md) |  | [optional] 

## Example

```python
from cryptoapis.models.get_zilliqa_address_details_e400 import GetZilliqaAddressDetailsE400

# TODO update the JSON string below
json = "{}"
# create an instance of GetZilliqaAddressDetailsE400 from a JSON string
get_zilliqa_address_details_e400_instance = GetZilliqaAddressDetailsE400.from_json(json)
# print the JSON string representation of the object
print GetZilliqaAddressDetailsE400.to_json()

# convert the object into a dict
get_zilliqa_address_details_e400_dict = get_zilliqa_address_details_e400_instance.to_dict()
# create an instance of GetZilliqaAddressDetailsE400 from a dict
get_zilliqa_address_details_e400_form_dict = get_zilliqa_address_details_e400.from_dict(get_zilliqa_address_details_e400_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


