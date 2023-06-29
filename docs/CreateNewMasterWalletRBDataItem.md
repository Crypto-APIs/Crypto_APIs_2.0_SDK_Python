# CreateNewMasterWalletRBDataItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_name** | **str** | Defines the name of the wallet that will be generated. | 
**wallet_type** | **str** | Represents if the generated wallet is only for mainnet or only for testnet . | 

## Example

```python
from cryptoapis.models.create_new_master_wallet_rb_data_item import CreateNewMasterWalletRBDataItem

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNewMasterWalletRBDataItem from a JSON string
create_new_master_wallet_rb_data_item_instance = CreateNewMasterWalletRBDataItem.from_json(json)
# print the JSON string representation of the object
print CreateNewMasterWalletRBDataItem.to_json()

# convert the object into a dict
create_new_master_wallet_rb_data_item_dict = create_new_master_wallet_rb_data_item_instance.to_dict()
# create an instance of CreateNewMasterWalletRBDataItem from a dict
create_new_master_wallet_rb_data_item_form_dict = create_new_master_wallet_rb_data_item.from_dict(create_new_master_wallet_rb_data_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


