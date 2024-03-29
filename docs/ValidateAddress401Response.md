# ValidateAddress401Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | Specifies the version of the API that incorporates this endpoint. | 
**request_id** | **str** | Defines the ID of the request. The &#x60;requestId&#x60; is generated by Crypto APIs and it&#39;s unique for every request. | 
**context** | **str** | In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. &#x60;context&#x60; is specified by the user. | [optional] 
**error** | [**ValidateAddressE401**](ValidateAddressE401.md) |  | 

## Example

```python
from cryptoapis.models.validate_address401_response import ValidateAddress401Response

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateAddress401Response from a JSON string
validate_address401_response_instance = ValidateAddress401Response.from_json(json)
# print the JSON string representation of the object
print ValidateAddress401Response.to_json()

# convert the object into a dict
validate_address401_response_dict = validate_address401_response_instance.to_dict()
# create an instance of ValidateAddress401Response from a dict
validate_address401_response_form_dict = validate_address401_response.from_dict(validate_address401_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


