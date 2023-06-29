# GetFeeAddressDetailsRI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Represents the specific fee address, which is always automatically generated. Users must fund it. | 
**balance** | [**GetFeeAddressDetailsRIBalance**](GetFeeAddressDetailsRIBalance.md) |  | 
**minimum_transfer_amount** | **str** | Represents the minimum transfer amount of the currency in the &#x60;fromAddress&#x60; that can be allowed for an automatic forwarding. | 

## Example

```python
from cryptoapis.models.get_fee_address_details_ri import GetFeeAddressDetailsRI

# TODO update the JSON string below
json = "{}"
# create an instance of GetFeeAddressDetailsRI from a JSON string
get_fee_address_details_ri_instance = GetFeeAddressDetailsRI.from_json(json)
# print the JSON string representation of the object
print GetFeeAddressDetailsRI.to_json()

# convert the object into a dict
get_fee_address_details_ri_dict = get_fee_address_details_ri_instance.to_dict()
# create an instance of GetFeeAddressDetailsRI from a dict
get_fee_address_details_ri_form_dict = get_fee_address_details_ri.from_dict(get_fee_address_details_ri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


