# BlockHeightReached


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | Specifies the version of the API that incorporates this endpoint. | 
**reference_id** | **str** | Represents a unique identifier that serves as reference to the specific request which prompts a callback, e.g. Blockchain Events Subscription, Blockchain Automation, etc. | 
**idempotency_key** | **str** | Specifies a unique ID generated by the system and attached to each callback. It is used by the server to recognize consecutive requests with the same data with the purpose not to perform the same operation twice. | 
**data** | [**BlockHeightReachedData**](BlockHeightReachedData.md) |  | 

## Example

```python
from cryptoapis.models.block_height_reached import BlockHeightReached

# TODO update the JSON string below
json = "{}"
# create an instance of BlockHeightReached from a JSON string
block_height_reached_instance = BlockHeightReached.from_json(json)
# print the JSON string representation of the object
print BlockHeightReached.to_json()

# convert the object into a dict
block_height_reached_dict = block_height_reached_instance.to_dict()
# create an instance of BlockHeightReached from a dict
block_height_reached_form_dict = block_height_reached.from_dict(block_height_reached_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

