# GenerateDepositAddressRI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Specifies the specific address&#39;s unique string value. | 
**created_timestamp** | **int** | Defines the specific UNIX time when the deposit address was created. | 
**label** | **str** | Represents a custom tag that customers can set up for their Wallets and addresses. E.g. custom label named \&quot;Special addresses\&quot;. | 

## Example

```python
from cryptoapis.models.generate_deposit_address_ri import GenerateDepositAddressRI

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateDepositAddressRI from a JSON string
generate_deposit_address_ri_instance = GenerateDepositAddressRI.from_json(json)
# print the JSON string representation of the object
print GenerateDepositAddressRI.to_json()

# convert the object into a dict
generate_deposit_address_ri_dict = generate_deposit_address_ri_instance.to_dict()
# create an instance of GenerateDepositAddressRI from a dict
generate_deposit_address_ri_form_dict = generate_deposit_address_ri.from_dict(generate_deposit_address_ri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


