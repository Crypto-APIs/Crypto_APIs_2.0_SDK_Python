# CreateAutomaticTokensForwardingRBTokenData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_id** | **int** | Represents the specific &#x60;propertyId&#x60; of the token data that will be forwarded. | 
**contract_address** | **str** | Represents the specific &#x60;contractAddress&#x60; of the Token that will be forwarded. | 

## Example

```python
from cryptoapis.models.create_automatic_tokens_forwarding_rb_token_data import CreateAutomaticTokensForwardingRBTokenData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAutomaticTokensForwardingRBTokenData from a JSON string
create_automatic_tokens_forwarding_rb_token_data_instance = CreateAutomaticTokensForwardingRBTokenData.from_json(json)
# print the JSON string representation of the object
print CreateAutomaticTokensForwardingRBTokenData.to_json()

# convert the object into a dict
create_automatic_tokens_forwarding_rb_token_data_dict = create_automatic_tokens_forwarding_rb_token_data_instance.to_dict()
# create an instance of CreateAutomaticTokensForwardingRBTokenData from a dict
create_automatic_tokens_forwarding_rb_token_data_form_dict = create_automatic_tokens_forwarding_rb_token_data.from_dict(create_automatic_tokens_forwarding_rb_token_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


