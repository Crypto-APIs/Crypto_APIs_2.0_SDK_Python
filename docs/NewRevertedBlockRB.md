# NewRevertedBlockRB


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **str** | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional] 
**data** | [**NewRevertedBlockRBData**](NewRevertedBlockRBData.md) |  | 

## Example

```python
from cryptoapis.models.new_reverted_block_rb import NewRevertedBlockRB

# TODO update the JSON string below
json = "{}"
# create an instance of NewRevertedBlockRB from a JSON string
new_reverted_block_rb_instance = NewRevertedBlockRB.from_json(json)
# print the JSON string representation of the object
print NewRevertedBlockRB.to_json()

# convert the object into a dict
new_reverted_block_rb_dict = new_reverted_block_rb_instance.to_dict()
# create an instance of NewRevertedBlockRB from a dict
new_reverted_block_rb_form_dict = new_reverted_block_rb.from_dict(new_reverted_block_rb_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


