# ListCoinsForwardingAutomationsRData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | Defines how many items should be returned in the response per page basis. | 
**offset** | **int** | The starting index of the response items, i.e. where the response should start listing the returned items. | 
**total** | **int** | Defines the total number of items returned in the response. | 
**items** | [**List[ListCoinsForwardingAutomationsRI]**](ListCoinsForwardingAutomationsRI.md) |  | 

## Example

```python
from cryptoapis.models.list_coins_forwarding_automations_r_data import ListCoinsForwardingAutomationsRData

# TODO update the JSON string below
json = "{}"
# create an instance of ListCoinsForwardingAutomationsRData from a JSON string
list_coins_forwarding_automations_r_data_instance = ListCoinsForwardingAutomationsRData.from_json(json)
# print the JSON string representation of the object
print ListCoinsForwardingAutomationsRData.to_json()

# convert the object into a dict
list_coins_forwarding_automations_r_data_dict = list_coins_forwarding_automations_r_data_instance.to_dict()
# create an instance of ListCoinsForwardingAutomationsRData from a dict
list_coins_forwarding_automations_r_data_form_dict = list_coins_forwarding_automations_r_data.from_dict(list_coins_forwarding_automations_r_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


