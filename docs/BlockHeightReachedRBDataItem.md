# BlockHeightReachedRBDataItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_duplicates** | **bool** | Specifies a flag that permits or denies the creation of duplicate addresses. | [optional] [default to False]
**block_height_reached** | **int** | Represents the specified value of block height for which the callback will be received. | 
**callback_secret_key** | **str** | Represents the Secret Key value provided by the customer. This field is used for security purposes during the callback notification, in order to prove the sender of the callback as Crypto APIs. For more information please see our [Documentation](https://developers.cryptoapis.io/technical-documentation/general-information/callbacks#callback-security). | [optional] 
**callback_url** | **str** | Represents the URL that is set by the customer where the callback will be received at. The callback notification will be received only if and when the event occurs. &#x60;We support ONLY httpS type of protocol&#x60;. | 

## Example

```python
from cryptoapis.models.block_height_reached_rb_data_item import BlockHeightReachedRBDataItem

# TODO update the JSON string below
json = "{}"
# create an instance of BlockHeightReachedRBDataItem from a JSON string
block_height_reached_rb_data_item_instance = BlockHeightReachedRBDataItem.from_json(json)
# print the JSON string representation of the object
print BlockHeightReachedRBDataItem.to_json()

# convert the object into a dict
block_height_reached_rb_data_item_dict = block_height_reached_rb_data_item_instance.to_dict()
# create an instance of BlockHeightReachedRBDataItem from a dict
block_height_reached_rb_data_item_form_dict = block_height_reached_rb_data_item.from_dict(block_height_reached_rb_data_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


