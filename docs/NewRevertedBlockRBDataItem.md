# NewRevertedBlockRBDataItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_duplicates** | **str** | Specifies a flag that permits or denies the creation of duplicate addresses. | [optional] 
**callback_secret_key** | **str** | Represents the Secret Key value provided by the customer. This field is used for security purposes during the callback notification, in order to prove the sender of the callback as Crypto APIs. For more information please see our Documentation. | 
**callback_url** | **str** | Represents the URL that is set by the customer where the callback will be received at. The callback notification will be received only if and when the event occurs. We support ONLY httpS type of protocol. | 

## Example

```python
from cryptoapis.models.new_reverted_block_rb_data_item import NewRevertedBlockRBDataItem

# TODO update the JSON string below
json = "{}"
# create an instance of NewRevertedBlockRBDataItem from a JSON string
new_reverted_block_rb_data_item_instance = NewRevertedBlockRBDataItem.from_json(json)
# print the JSON string representation of the object
print NewRevertedBlockRBDataItem.to_json()

# convert the object into a dict
new_reverted_block_rb_data_item_dict = new_reverted_block_rb_data_item_instance.to_dict()
# create an instance of NewRevertedBlockRBDataItem from a dict
new_reverted_block_rb_data_item_form_dict = new_reverted_block_rb_data_item.from_dict(new_reverted_block_rb_data_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


