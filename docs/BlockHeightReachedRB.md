# BlockHeightReachedRB


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **str** | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional] 
**data** | [**BlockHeightReachedRBData**](BlockHeightReachedRBData.md) |  | 

## Example

```python
from cryptoapis.models.block_height_reached_rb import BlockHeightReachedRB

# TODO update the JSON string below
json = "{}"
# create an instance of BlockHeightReachedRB from a JSON string
block_height_reached_rb_instance = BlockHeightReachedRB.from_json(json)
# print the JSON string representation of the object
print BlockHeightReachedRB.to_json()

# convert the object into a dict
block_height_reached_rb_dict = block_height_reached_rb_instance.to_dict()
# create an instance of BlockHeightReachedRB from a dict
block_height_reached_rb_form_dict = block_height_reached_rb.from_dict(block_height_reached_rb_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


