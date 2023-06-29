# NewBlockRI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callback_secret_key** | **str** | Represents the Secret Key value provided by the customer. This field is used for security purposes during the callback notification, in order to prove the sender of the callback as Crypto APIs. For more information please see our [Documentation](https://developers.cryptoapis.io/technical-documentation/general-information/callbacks#callback-security). | 
**callback_url** | **str** | Represents the URL that is set by the customer where the callback will be received at. The callback notification will be received only if and when the event occurs. &#x60;We support ONLY httpS type of protocol&#x60;. | 
**created_timestamp** | **int** | Defines the specific time/date when the subscription was created in Unix Timestamp. | 
**is_active** | **bool** | Defines whether the subscription is active or not. Set as boolean. | 
**reference_id** | **str** | Represents a unique ID used to reference the specific callback subscription. | 

## Example

```python
from cryptoapis.models.new_block_ri import NewBlockRI

# TODO update the JSON string below
json = "{}"
# create an instance of NewBlockRI from a JSON string
new_block_ri_instance = NewBlockRI.from_json(json)
# print the JSON string representation of the object
print NewBlockRI.to_json()

# convert the object into a dict
new_block_ri_dict = new_block_ri_instance.to_dict()
# create an instance of NewBlockRI from a dict
new_block_ri_form_dict = new_block_ri.from_dict(new_block_ri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


