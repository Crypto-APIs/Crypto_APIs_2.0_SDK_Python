# DecodeXAddressRI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_tag** | **int** | Defines a specific Tag that is an additional XRP address feature. It helps identifying a transaction recipient beyond a wallet address. | 
**classic_address** | **str** | Represents the public address, which is a compressed and shortened form of a public key. | 

## Example

```python
from cryptoapis.models.decode_x_address_ri import DecodeXAddressRI

# TODO update the JSON string below
json = "{}"
# create an instance of DecodeXAddressRI from a JSON string
decode_x_address_ri_instance = DecodeXAddressRI.from_json(json)
# print the JSON string representation of the object
print DecodeXAddressRI.to_json()

# convert the object into a dict
decode_x_address_ri_dict = decode_x_address_ri_instance.to_dict()
# create an instance of DecodeXAddressRI from a dict
decode_x_address_ri_form_dict = decode_x_address_ri.from_dict(decode_x_address_ri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


