# ValidateAddressRI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Represents the specific address that will be checked if it&#39;s valid or not. | 
**is_valid** | **bool** | Defines whether the address is valid or not. Set as boolean. | 

## Example

```python
from cryptoapis.models.validate_address_ri import ValidateAddressRI

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateAddressRI from a JSON string
validate_address_ri_instance = ValidateAddressRI.from_json(json)
# print the JSON string representation of the object
print ValidateAddressRI.to_json()

# convert the object into a dict
validate_address_ri_dict = validate_address_ri_instance.to_dict()
# create an instance of ValidateAddressRI from a dict
validate_address_ri_form_dict = validate_address_ri.from_dict(validate_address_ri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


