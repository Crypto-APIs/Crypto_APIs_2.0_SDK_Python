# GenerateDepositAddressRBDataItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | Represents a custom tag that customers can set up for their Wallets and addresses. E.g. custom label named \&quot;Special addresses\&quot;. | 

## Example

```python
from cryptoapis.models.generate_deposit_address_rb_data_item import GenerateDepositAddressRBDataItem

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateDepositAddressRBDataItem from a JSON string
generate_deposit_address_rb_data_item_instance = GenerateDepositAddressRBDataItem.from_json(json)
# print the JSON string representation of the object
print GenerateDepositAddressRBDataItem.to_json()

# convert the object into a dict
generate_deposit_address_rb_data_item_dict = generate_deposit_address_rb_data_item_instance.to_dict()
# create an instance of GenerateDepositAddressRBDataItem from a dict
generate_deposit_address_rb_data_item_form_dict = generate_deposit_address_rb_data_item.from_dict(generate_deposit_address_rb_data_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


